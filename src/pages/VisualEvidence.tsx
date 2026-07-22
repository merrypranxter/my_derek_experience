import { useState } from "react";
import { motion, AnimatePresence } from "motion/react";
import { useNavigate } from "react-router-dom";
import evidenceFiles from "../data/evidenceFiles.json";
import TTSButton from "../components/TTSButton";

interface EvidenceFile {
  name: string;
  url: string;
  type: string;
  category: string;
}

export default function VisualEvidence() {
  const navigate = useNavigate();
  const [filter, setFilter] = useState<string>("all");
  const [selectedMedia, setSelectedMedia] = useState<EvidenceFile | null>(null);

  const files = evidenceFiles as EvidenceFile[]; const categories = Array.from(new Set<string>(files.map(f => f.category))) as string[];
  
  const filteredFiles = files.filter(f => filter === "all" || f.category === filter);

  return (
    <div className="min-h-screen text-white overflow-x-hidden font-sans selection:bg-cyan-500 selection:text-black">
      <button 
        onClick={() => navigate("/")}
        className="fixed top-6 left-6 z-50 text-[10px] font-mono uppercase tracking-widest text-neutral-500 hover:text-white transition-colors flex items-center gap-2 bg-[#05030f]/80 px-3 py-2 border border-white/10 backdrop-blur-md"
      >
        <span className="text-cyan-500">{"<"}</span> Return to System
      </button>

      <div className="max-w-[1400px] mx-auto px-4 md:px-6 pt-32 pb-24 relative z-10">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8, ease: [0.16, 1, 0.3, 1] }}
        >
          <div className="font-data text-xs text-cyan-500 uppercase tracking-widest mb-12 border-b border-cyan-500/30 pb-4">
            [ VISUAL EVIDENCE ARCHIVE ]
          </div>
          
          <h1 className="text-4xl md:text-5xl lg:text-6xl font-subject tracking-tighter mb-8 uppercase text-white drop-shadow-[0_0_15px_rgba(53,224,255,0.5)]">
            The Record
          </h1>
          
          <div className="relative">
            <TTSButton text="Direct feed from cloud storage established. The images below contain receipts, chat logs, and art files provided for cross-referencing. Notice: Original bucket filenames are preserved below each asset." className="absolute -top-4 -left-4" />
            <p className="text-neutral-400 font-data text-sm max-w-2xl mb-12 border-l border-cyan-500/50 pl-4 relative">
              Direct feed from cloud storage established. The images below contain receipts, chat logs, and art files provided for cross-referencing.
              <br/><br/>
              <span className="text-cyan-400">Notice:</span> Original bucket filenames are preserved below each asset.
            </p>
          </div>

          <div className="flex flex-wrap gap-4 mb-12 font-data text-xs uppercase tracking-widest">
            <button 
              onClick={() => setFilter("all")}
              className={`px-4 py-2 border transition-colors ${filter === "all" ? "border-cyan-500 text-cyan-400 bg-cyan-500/10" : "border-white/10 text-neutral-500 hover:border-white/30"}`}
            >
              All Data
            </button>
            {categories.map((c: string, i: number) => (
              <button 
                key={c}
                onClick={() => setFilter(c)}
                className={`px-4 py-2 border transition-colors ${filter === c ? "border-cyan-500 text-cyan-400 bg-cyan-500/10" : "border-white/10 text-neutral-500 hover:border-white/30"}`}
              >
                {c}
              </button>
            ))}
          </div>

          <motion.div 
            layout
            className="grid grid-cols-2 sm:grid-cols-4 md:grid-cols-6 lg:grid-cols-8 gap-2 md:gap-4"
          >
            <AnimatePresence mode="popLayout">
              {filteredFiles.map((file: EvidenceFile) => (
                <motion.div
                  layout
                  initial={{ opacity: 0, scale: 0.9 }}
                  animate={{ opacity: 1, scale: 1 }}
                  exit={{ opacity: 0, scale: 0.9 }}
                  transition={{ duration: 0.3 }}
                  key={file.name}
                  className="group relative flex flex-col gap-1"
                >
                  <div 
                    className="aspect-square bg-[#0d0a20] border border-[#241d45] group-hover:border-cyan-500/50 transition-colors flex items-center justify-center cursor-pointer overflow-hidden relative"
                    onClick={() => setSelectedMedia(file)}
                  >
                    {file.type.startsWith('video') ? (
                      <video 
                        src={file.url + "#t=0.1"} 
                        preload="metadata"
                        className="object-cover w-full h-full opacity-60 group-hover:opacity-100 transition-opacity mix-blend-screen grayscale group-hover:grayscale-0"
                        muted 
                        loop 
                        playsInline
                        onMouseOver={e => (e.target as HTMLVideoElement).play()}
                        onMouseOut={e => (e.target as HTMLVideoElement).pause()}
                      />
                    ) : (
                      <img 
                        src={file.url} 
                        alt={file.name} 
                        className="object-cover w-full h-full opacity-60 group-hover:opacity-100 transition-opacity mix-blend-screen grayscale group-hover:grayscale-0" 
                        loading="lazy" referrerPolicy="no-referrer" 
                      />
                    )}
                    <div className="absolute top-1 right-1 bg-black/80 px-1 py-0.5 text-[8px] font-data text-cyan-500 uppercase tracking-widest border border-cyan-500/20">
                      {file.type.startsWith('video') ? 'VID' : 'IMG'}
                    </div>
                  </div>
                  
                  <div className="font-data text-[8px] text-neutral-500 break-all bg-black/50 p-1 border border-white/5 line-clamp-2" title={file.name}>
                    <span className="text-cyan-400">ID:</span> {file.name.substring(0, 10)}...
                  </div>
                </motion.div>
              ))}
            </AnimatePresence>
          </motion.div>
        </motion.div>
      </div>

      <AnimatePresence>
        {selectedMedia && (
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            onClick={() => setSelectedMedia(null)}
            className="fixed inset-0 z-[100] bg-black/90 backdrop-blur-sm flex items-center justify-center p-6 cursor-zoom-out"
          >
            <div 
              className="relative max-w-5xl w-full h-full max-h-[90vh] flex flex-col"
              onClick={e => e.stopPropagation()}
            >
              <div className="flex justify-between items-center mb-4 flex-shrink-0">
                <div className="font-data text-xs text-cyan-400 break-all bg-black/50 px-3 py-2 border border-cyan-500/30">
                  {selectedMedia.name}
                </div>
                <button 
                  onClick={() => setSelectedMedia(null)}
                  className="text-white hover:text-cyan-500 font-data text-xl ml-4"
                >
                  [X]
                </button>
              </div>
              <div className="flex-1 min-h-0 flex items-center justify-center bg-black border border-white/10 p-2">
                {selectedMedia.type.startsWith('video') ? (
                  <video src={selectedMedia.url} className="w-full h-full object-contain" controls autoPlay />
                ) : (
                  <img src={selectedMedia.url} alt={selectedMedia.name} className="w-full h-full object-contain" referrerPolicy="no-referrer" />
                )}
              </div>
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
}
