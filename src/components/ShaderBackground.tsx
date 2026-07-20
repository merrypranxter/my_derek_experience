import { useEffect, useRef } from 'react';

export default function ShaderBackground() {
  const canvasRef = useRef<HTMLCanvasElement>(null);

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const gl = canvas.getContext('webgl');
    if (!gl) return;

    const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    const vs = 'attribute vec2 p;void main(){gl_Position=vec4(p,0.,1.);}';
    const fs = `
precision highp float;
uniform vec2 u_res; uniform float u_time;
float hash(vec2 p){p=fract(p*vec2(123.34,456.21));p+=dot(p,p+45.32);return fract(p.x*p.y);}
vec3 hash3(vec2 p){return vec3(hash(p),hash(p+17.17),hash(p+31.31));}
void main(){
  vec2 frag=gl_FragCoord.xy; vec2 uv=frag/u_res;

  // --- neutral LED-blue screen surface ---
  vec3 base=vec3(0.075,0.095,0.155);

  // large soft unevenness, like panel brightness drift
  vec2 g=uv-vec2(0.5,0.45); g.x*=u_res.x/u_res.y;
  float glow=exp(-dot(g,g)*3.0);
  base*=0.85+0.35*glow;

  // --- subpixel color static: each channel jitters on its own ---
  // slow temporal re-roll so it shimmers rather than buzzes
  float tQ=floor(u_time*7.0);
  vec3 n=hash3(frag+vec2(tQ*0.0,tQ*13.7));
  vec3 n2=hash3(frag+vec2(tQ*7.3,0.0));
  vec3 static_rgb=(mix(n,n2,0.5)-0.5)*0.11;  // barely-there amplitude
  base+=static_rgb*vec3(1.0,1.0,1.3);        // slightly blue-leaning grain

  // --- LED cell grid: faint dark seams between pixel cells ---
  vec2 cellmod=mod(frag,3.0);
  float seam=1.0;
  if(cellmod.x<0.8) seam*=0.92;
  if(cellmod.y<0.8) seam*=0.92;
  base*=seam;

  // gentle vignette so the edges fall off like a real screen
  float vig=1.0-0.45*dot(g,g);
  gl_FragColor=vec4(base*vig,1.0);
}`;

    function sh(type: number, src: string) {
      const s = gl.createShader(type);
      if (!s) return null;
      gl.shaderSource(s, src);
      gl.compileShader(s);
      if (!gl.getShaderParameter(s, gl.COMPILE_STATUS)) {
        console.error(gl.getShaderInfoLog(s));
      }
      return s;
    }
    const prog = gl.createProgram();
    if (!prog) return;
    
    const vShader = sh(gl.VERTEX_SHADER, vs);
    const fShader = sh(gl.FRAGMENT_SHADER, fs);
    if (!vShader || !fShader) return;

    gl.attachShader(prog, vShader);
    gl.attachShader(prog, fShader);
    gl.linkProgram(prog);
    gl.useProgram(prog);

    const buf = gl.createBuffer();
    gl.bindBuffer(gl.ARRAY_BUFFER, buf);
    gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([-1,-1, 3,-1, -1,3]), gl.STATIC_DRAW);
    const loc = gl.getAttribLocation(prog, 'p');
    gl.enableVertexAttribArray(loc);
    gl.vertexAttribPointer(loc, 2, gl.FLOAT, false, 0, 0);

    const uRes = gl.getUniformLocation(prog, 'u_res');
    const uTime = gl.getUniformLocation(prog, 'u_time');

    function resize() {
      const dpr = Math.min(window.devicePixelRatio || 1, 1.5);
      canvas.width = window.innerWidth * dpr;
      canvas.height = window.innerHeight * dpr;
      gl.viewport(0, 0, canvas.width, canvas.height);
    }
    window.addEventListener('resize', resize);
    resize();

    const t0 = performance.now();
    let frameId: number;
    let timeoutId: number;
    
    function frame() {
      gl.uniform2f(uRes, canvas.width, canvas.height);
      gl.uniform1f(uTime, (performance.now() - t0) / 1000);
      gl.drawArrays(gl.TRIANGLES, 0, 3);
      if (!reduceMotion && !document.hidden) {
        frameId = requestAnimationFrame(frame);
      } else {
        timeoutId = window.setTimeout(frame, 500);
      }
    }
    frame();

    return () => {
      window.removeEventListener('resize', resize);
      cancelAnimationFrame(frameId);
      clearTimeout(timeoutId);
    };
  }, []);

  return (
    <canvas 
      ref={canvasRef} 
      className="fixed inset-0 w-full h-full block pointer-events-none z-0" 
      aria-hidden="true"
    />
  );
}
