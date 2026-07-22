import { useState, useEffect } from "react";
import { useSearchParams, useNavigate } from "react-router-dom";
import { motion } from "motion/react";

export default function ChatLog() {
  const [searchParams] = useSearchParams();
  const navigate = useNavigate();
  const id = searchParams.get("id");

  return (
    <div className="min-h-screen text-white overflow-x-hidden font-sans selection:bg-cyan-500 selection:text-black">
      <button 
        onClick={() => navigate(-1)}
        className="fixed top-6 left-6 z-50 text-[10px] font-mono uppercase tracking-widest text-neutral-500 hover:text-white transition-colors flex items-center gap-2 bg-[#05030f]/80 px-3 py-2 border border-white/10 backdrop-blur-md"
      >
        <span className="text-cyan-500">{"<"}</span> Back
      </button>

      <div className="max-w-[800px] mx-auto px-4 md:px-6 pt-32 pb-24 relative z-10">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8, ease: [0.16, 1, 0.3, 1] }}
        >
          <div className="font-data text-xs text-cyan-500 uppercase tracking-widest mb-12 border-b border-cyan-500/30 pb-4">
            [ WHATSAPP LOG VIEWER ]
          </div>
          
          <h1 className="text-4xl font-subject tracking-tighter mb-8 uppercase text-white drop-shadow-[0_0_15px_rgba(53,224,255,0.5)]">
            Chat Transcript
          </h1>
          
          {id ? (
            <div className="bg-black/50 border border-cyan-500/30 p-6 font-data text-sm text-neutral-300">
              <p className="text-cyan-400 mb-4">Searching for record: <span className="font-bold text-white">{id}</span></p>
              <p className="mb-4">The chat log text file is currently pending upload to the internal dataset.</p>
              <p>Once provided, the forensic context viewer will display the surrounding conversation history for this timestamp here.</p>
            </div>
          ) : (
            <div className="bg-black/50 border border-white/10 p-6 font-data text-sm text-neutral-400">
              <p>No message ID specified. Full chat log pending upload.</p>
            </div>
          )}
        </motion.div>
      </div>
    </div>
  );
}
