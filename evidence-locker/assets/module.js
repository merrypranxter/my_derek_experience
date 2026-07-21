/* ============================================================
   EVIDENCE LOCKER — module case-file renderer
   Reads window.MODULE, builds the docket, runs the behaviors:
   1. scroll-as-excavation (exhibits dealt onto the thread)
   2. evidence cross-highlight (same ID lights up + jumps)
   3. mechanism readout (hover a moving part, read its function)
   ============================================================ */
(function(){
const M = window.MODULE;
const reduceMotion = matchMedia('(prefers-reduced-motion: reduce)').matches;
const rnd = n => Math.floor(Math.random()*n);
document.title = `MODULE ${M.id} — ${M.title} · Evidence Locker`;

/* ---------- header ---------- */
document.getElementById('filetag').innerHTML =
  `EVIDENCE LOCKER · MODULE <b>${M.id}</b> · <b>${M.code}</b>`;
document.getElementById('mtitle').textContent = M.title;
document.getElementById('msub').textContent = M.sub || '';
document.getElementById('charges').innerHTML =
  M.labels.map(l => `<li style="--tilt:${(rnd(25)-12)/10}deg">${l}</li>`).join('');
document.getElementById('objective').textContent = M.objective;

/* ---------- mechanism ---------- */
document.getElementById('mechTitle').innerHTML = M.mechanismTitle;
const mech = document.getElementById('mechanism');
M.mechanism.forEach((n, i) => {
  const d = document.createElement('div');
  d.className = 'mnode'; d.tabIndex = 0; d.dataset.text = n.text;
  d.innerHTML = `<div class="n">${i+1}</div><h3>${n.title}</h3>`;
  mech.appendChild(d);
  if (i < M.mechanism.length - 1){
    const a = document.createElement('div');
    a.className = 'marrow'; a.textContent = '→'; a.setAttribute('aria-hidden','true');
    mech.appendChild(a);
  }
});
if (M.loop){
  const l = document.createElement('div');
  l.className = 'mloop'; l.innerHTML = M.loop;
  mech.appendChild(l);
}
const mread = document.createElement('p');
mread.className = 'mread'; mread.setAttribute('aria-live','polite');
mech.appendChild(mread);
mech.querySelectorAll('.mnode').forEach(n => {
  const show = () => mread.textContent = '▸ ' + n.dataset.text;
  const hide = () => mread.textContent = '';
  n.addEventListener('pointerenter', show);
  n.addEventListener('focus', show);
  n.addEventListener('pointerleave', hide);
  n.addEventListener('blur', hide);
});

/* ---------- optional ledger table ---------- */
if (M.table){
  document.getElementById('tableTitle').innerHTML = M.table.title;
  const t = document.getElementById('ledger');
  t.innerHTML =
    '<tr>' + M.table.head.map(h => `<th>${h}</th>`).join('') + '</tr>' +
    M.table.rows.map(r => '<tr>' + r.map(c => `<td>${c}</td>`).join('') + '</tr>').join('');
  document.getElementById('ledgernote').innerHTML = M.table.note || '';
} else {
  document.getElementById('tableSection').remove();
}

/* ---------- exhibits ---------- */
document.getElementById('exTitle').innerHTML = M.exhibitsTitle;
const holder = document.getElementById('exhibits');
M.exhibits.forEach((ex, i) => {
  const el = document.createElement('article');
  el.className = 'exhibit';
  el.id = 'ex' + ex.num;
  el.style.setProperty('--deal', (i % 2 ? -1.4 : 1.4) + 'deg');
  const ids = (ex.ids || []).map(pair => {
    const [id, d] = Array.isArray(pair) ? pair : [pair, ''];
    const cls = id.startsWith('WA') || id.startsWith('SC') ? 'eid' : 'eid testimony';
    return `<button class="${cls}" data-eid="${id.split('–')[0]}" type="button">${id}${d ? ` <span class="d">· ${d}</span>` : ''}</button>`;
  }).join('');
  el.innerHTML = `
    <div class="exhibit__top">
      <span class="exhibit__num">EXHIBIT ${ex.num}</span>
      <span class="stamp" style="--tilt:${(rnd(5)-2)}deg">${ex.status}</span>
    </div>
    <h3>${ex.name}</h3>
    ${ids ? `<div class="ids">${ids}</div>` : ''}
    ${ex.quote ? `<blockquote class="receipt">${ex.quote}</blockquote>` : ''}
    ${ex.note ? `<p class="note">${ex.note}</p>` : ''}
    <p class="analysis"><b>ANALYSIS —</b> ${ex.analysis}</p>
    ${ex.crossref ? `<a class="crossref" href="${ex.crossref[0]}">↗ cross-reference: ${ex.crossref[1]}</a>` : ''}
  `;
  holder.appendChild(el);
});

/* ---------- impact + yaml + nav ---------- */
document.getElementById('impactTitle').innerHTML = M.impactTitle || 'DAMAGE ASSESSMENT';
document.getElementById('rawTitle').innerHTML = M.rawTitle || 'RAW DATA OUTPUT';
document.getElementById('impact').innerHTML = M.impact.map(x => `<li>${x}</li>`).join('');
document.getElementById('yaml').textContent = M.yaml;
document.getElementById('navPrev').innerHTML = M.prev ? `<a href="${M.prev[0]}"><b>&lt;</b> ${M.prev[1]}</a>` : '<span></span>';
document.getElementById('navNext').innerHTML = M.next ? `<a href="${M.next[0]}">${M.next[1]} <b>&gt;</b></a>` : '<span></span>';

/* ---------- 1. scroll-as-excavation ---------- */
const cards = [...document.querySelectorAll('.exhibit')];
if (reduceMotion){
  cards.forEach(c => c.classList.add('dealt'));
} else {
  const io = new IntersectionObserver(entries => {
    entries.forEach(en => {
      if (en.isIntersecting){
        const idx = cards.indexOf(en.target);
        setTimeout(() => en.target.classList.add('dealt'), (idx % 2) * 120);
        io.unobserve(en.target);
      }
    });
  }, {threshold: .15});
  cards.forEach(c => io.observe(c));
}

/* ---------- 2. evidence cross-highlight ---------- */
const eidBtns = [...document.querySelectorAll('.eid')];
eidBtns.forEach(btn => {
  const key = btn.dataset.eid;
  const kin = eidBtns.filter(b => b.dataset.eid === key);
  if (kin.length < 2) return;
  btn.addEventListener('pointerenter', () => kin.forEach(b => b.classList.add('linked')));
  btn.addEventListener('focus',       () => kin.forEach(b => b.classList.add('linked')));
  btn.addEventListener('pointerleave',() => kin.forEach(b => b.classList.remove('linked')));
  btn.addEventListener('blur',        () => kin.forEach(b => b.classList.remove('linked')));
  btn.addEventListener('click', () => {
    const other = kin.find(b => b !== btn);
    if (other) other.closest('.exhibit').scrollIntoView({behavior: reduceMotion ? 'auto' : 'smooth', block:'center'});
  });
});

/* ---------- background: LED static ---------- */
(function(){
  const canvas = document.getElementById('field');
  const gl = canvas.getContext('webgl');
  if (!gl) return;
  const vs = 'attribute vec2 p;void main(){gl_Position=vec4(p,0.,1.);}';
  const fs = `
precision highp float;
uniform vec2 u_res; uniform float u_time;
float hash(vec2 p){p=fract(p*vec2(123.34,456.21));p+=dot(p,p+45.32);return fract(p.x*p.y);}
vec3 hash3(vec2 p){return vec3(hash(p),hash(p+17.17),hash(p+31.31));}
void main(){
  vec2 frag=gl_FragCoord.xy; vec2 uv=frag/u_res;
  vec3 base=vec3(0.075,0.095,0.155);
  vec2 g=uv-vec2(0.5,0.45); g.x*=u_res.x/u_res.y;
  float glow=exp(-dot(g,g)*3.0);
  base*=0.85+0.35*glow;
  float tQ=floor(u_time*7.0);
  vec3 n=hash3(frag+vec2(tQ*0.0,tQ*13.7));
  vec3 n2=hash3(frag+vec2(tQ*7.3,0.0));
  vec3 static_rgb=(mix(n,n2,0.5)-0.5)*0.11;
  base+=static_rgb*vec3(1.0,1.0,1.3);
  vec2 cellmod=mod(frag,3.0);
  float seam=1.0;
  if(cellmod.x<0.8) seam*=0.92;
  if(cellmod.y<0.8) seam*=0.92;
  base*=seam;
  float vig=1.0-0.45*dot(g,g);
  gl_FragColor=vec4(base*vig,1.0);
}`;
  function sh(t,s){const o=gl.createShader(t);gl.shaderSource(o,s);gl.compileShader(o);return o;}
  const prog=gl.createProgram();
  gl.attachShader(prog,sh(gl.VERTEX_SHADER,vs));
  gl.attachShader(prog,sh(gl.FRAGMENT_SHADER,fs));
  gl.linkProgram(prog);gl.useProgram(prog);
  const buf=gl.createBuffer();
  gl.bindBuffer(gl.ARRAY_BUFFER,buf);
  gl.bufferData(gl.ARRAY_BUFFER,new Float32Array([-1,-1,3,-1,-1,3]),gl.STATIC_DRAW);
  const loc=gl.getAttribLocation(prog,'p');
  gl.enableVertexAttribArray(loc);
  gl.vertexAttribPointer(loc,2,gl.FLOAT,false,0,0);
  const uRes=gl.getUniformLocation(prog,'u_res'),uTime=gl.getUniformLocation(prog,'u_time');
  function resize(){
    const dpr=Math.min(devicePixelRatio||1,1.5);
    canvas.width=innerWidth*dpr;canvas.height=innerHeight*dpr;
    gl.viewport(0,0,canvas.width,canvas.height);
  }
  addEventListener('resize',resize);resize();
  const t0=performance.now();
  function frame(){
    gl.uniform2f(uRes,canvas.width,canvas.height);
    gl.uniform1f(uTime,(performance.now()-t0)/1000);
    gl.drawArrays(gl.TRIANGLES,0,3);
    if(!reduceMotion && !document.hidden) requestAnimationFrame(frame);
    else setTimeout(frame, 500);
  }
  frame();
})();
})();
