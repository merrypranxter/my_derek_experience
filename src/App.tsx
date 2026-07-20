import { useEffect, useState } from "react";
import { motion } from "motion/react";

const MODULES = [
  { id: "01", title: "THE PROMISES", color: "#ffffff" },
  { id: "02", title: "THE WITHHOLDING", color: "#a3a3a3" },
  { id: "03", title: "THE RUG-PULLS", color: "#60a5fa" },
  { id: "04", title: "THE GASLIGHTING & DARVO", color: "#ffffff" },
  { id: "05", title: "THE TRIANGULATION", color: "#a3a3a3" },
  { id: "06", title: "THE EXPLOITATION", color: "#dc2626" },
  { id: "07", title: "THE ERASURE", color: "#ffffff" },
];

export default function App() {
  const [radius, setRadius] = useState(300);

  useEffect(() => {
    const updateRadius = () => {
      const minDimension = Math.min(window.innerWidth, window.innerHeight);
      setRadius(minDimension * 0.35); // 35% of the smallest screen dimension
    };
    
    updateRadius();
    window.addEventListener("resize", updateRadius);
    return () => window.removeEventListener("resize", updateRadius);
  }, []);

  return (
    <div className="relative min-h-screen w-full bg-neutral-950 text-white overflow-hidden flex items-center justify-center font-sans selection:bg-white selection:text-black">
      
      {/* BACKGROUND NOISE / ASTRAL TRASH GRID */}
      <div 
        className="absolute inset-0 opacity-10 pointer-events-none" 
        style={{ backgroundImage: 'radial-gradient(#ffffff 1px, transparent 1px)', backgroundSize: '40px 40px' }} 
      />

      {/* PLACEHOLDER FOR JS EXPERIMENT */}
      <div 
        id="js-placeholder"
        className="absolute inset-0 m-auto rounded-full border border-dashed border-white/20 flex items-center justify-center opacity-30"
        style={{ width: radius * 1.5, height: radius * 1.5 }}
      >
        <div className="absolute w-[200vw] h-[0.5px] bg-white/20" />
        <div className="absolute h-[200vh] w-[0.5px] bg-white/20" />
        <motion.div 
          animate={{ rotate: 360 }} 
          transition={{ duration: 40, repeat: Infinity, ease: "linear" }}
          className="w-full h-full border border-white/10 rounded-full absolute"
        />
        <span className="font-mono text-[10px] text-neutral-500 uppercase tracking-widest absolute bottom-4 bg-neutral-950 px-2">
          [ JS Canvas Placeholder ]
        </span>
      </div>

      {/* CENTER TYPOGRAPHY */}
      <div className="relative z-20 flex flex-col items-center justify-center pointer-events-none">
        <div className="flex flex-col w-full max-w-[80vw] md:max-w-2xl items-center text-center">
          <span className="text-xs uppercase tracking-[0.5em] text-neutral-400 self-center mb-[-10px] z-20 font-sans">
            My
          </span>
          <h1 className="text-[15vw] md:text-[140px] font-black leading-none tracking-tighter text-white">
            DEREK
          </h1>
          <div className="flex justify-between w-full text-[11px] font-mono text-neutral-300 uppercase tracking-[1.4em] mt-1 px-1 pl-[1.4em]">
            {Array.from("Experience").map((char, i) => (
              <span key={i}>{char}</span>
            ))}
          </div>
        </div>
      </div>

      {/* CIRCULAR MODULES */}
      <div className="absolute inset-0 m-auto pointer-events-none" style={{ width: 0, height: 0 }}>
        {MODULES.map((module, index) => {
          const angle = (index / MODULES.length) * Math.PI * 2 - Math.PI / 2; // Start from top (-90deg)
          const x = Math.cos(angle) * radius;
          const y = Math.sin(angle) * radius;

          return (
            <motion.div
              key={module.id}
              className="absolute flex flex-col items-center justify-center text-center pointer-events-auto cursor-pointer hover:scale-110 transition-transform duration-300"
              style={{
                x,
                y,
                translateX: "-50%",
                translateY: "-50%",
              }}
              initial={{ opacity: 0, scale: 0 }}
              animate={{ opacity: 1, scale: 1 }}
              transition={{ delay: index * 0.1, duration: 0.8, type: "spring" }}
            >
              <div 
                className="font-mono text-[10px] text-neutral-500 mb-1 tracking-widest uppercase"
              >
                MOD_{module.id}
              </div>
              <div 
                className="text-sm font-bold uppercase tracking-widest transition-all duration-300"
                style={{ color: module.color }}
              >
                {module.title}
              </div>
            </motion.div>
          );
        })}
      </div>

    </div>
  );
}
