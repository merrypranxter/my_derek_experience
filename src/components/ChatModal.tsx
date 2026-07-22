import { useState, useEffect } from "react";
import { motion, AnimatePresence } from "motion/react";
import { X } from "lucide-react";

interface ChatModalProps {
  chatId: string | null;
  onClose: () => void;
}

interface ChatMessage {
  lineNum: number;
  timestamp?: string;
  author?: string;
  text: string;
  isTarget: boolean;
}

export default function ChatModal({ chatId, onClose }: ChatModalProps) {
  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  useEffect(() => {
    if (!chatId) return;

    // Parse WA-1234 or WA-1234-1235 or WA-1234–1235
    const parts = chatId.replace('WA-', '').split(/[-–]/);
    const startLine = parseInt(parts[0], 10);
    const endLine = parts.length > 1 ? parseInt(parts[1], 10) : startLine;

    if (isNaN(startLine)) {
      setError("Invalid chat ID");
      return;
    }

    setLoading(true);
    fetch('/derek_whatsapp_combined.md')
      .then(res => {
        if (!res.ok) throw new Error("Could not load chat log");
        return res.text();
      })
      .then(text => {
        const lines = text.split('\n');
        
        // We want context: 5 lines before, 5 lines after
        const ctxStart = Math.max(1, startLine - 5);
        const ctxEnd = Math.min(lines.length, endLine + 5);
        
        const extracted: ChatMessage[] = [];
        
        let currentAuthor = "";
        let currentTimestamp = "";

        // The file is 1-indexed for the line numbers in WA tags
        for (let i = ctxStart; i <= ctxEnd; i++) {
          const rawLine = lines[i - 1];
          if (rawLine === undefined) continue;
          
          const isTarget = i >= startLine && i <= endLine;
          
          // Match timestamp and author
          // Example: [11/5/25, 9:06:09 PM] Derek Vasilakis: ...
          // Note there might be hidden characters like LRM at the start
          const match = rawLine.match(/^.?\[(.*?)\] (.*?): (.*)$/);
          
          if (match) {
            currentTimestamp = match[1];
            currentAuthor = match[2].trim();
            extracted.push({
              lineNum: i,
              timestamp: currentTimestamp,
              author: currentAuthor,
              text: match[3],
              isTarget
            });
          } else {
            // Continuation of previous line, or empty
            extracted.push({
              lineNum: i,
              author: currentAuthor, // inherit
              timestamp: currentTimestamp, // inherit
              text: rawLine,
              isTarget
            });
          }
        }
        
        setMessages(extracted);
        setLoading(false);
      })
      .catch(err => {
        setError(err.message);
        setLoading(false);
      });
      
  }, [chatId]);

  return (
    <AnimatePresence>
      {chatId && (
      <motion.div 
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        exit={{ opacity: 0 }}
        key="chat-modal"
        className="fixed inset-0 z-[200] bg-black/80 backdrop-blur-sm flex items-center justify-center p-4 md:p-8"
        onClick={onClose}
      >
        <motion.div 
          initial={{ y: 20, opacity: 0 }}
          animate={{ y: 0, opacity: 1 }}
          exit={{ y: 20, opacity: 0 }}
          className="bg-[#05030f] border border-cyan-500/30 max-w-2xl w-full max-h-[85vh] flex flex-col shadow-[0_0_30px_rgba(53,224,255,0.15)] relative overflow-hidden"
          onClick={e => e.stopPropagation()}
        >
          {/* Header */}
          <div className="flex items-center justify-between p-4 border-b border-cyan-500/30 bg-[#0d0a20]">
            <div>
              <div className="text-[10px] font-mono text-cyan-500 uppercase tracking-widest mb-1">Evidence Locker</div>
              <div className="text-white font-mono text-sm">SOURCE LOG: {chatId}</div>
            </div>
            <button 
              onClick={onClose}
              className="text-neutral-500 hover:text-cyan-400 transition-colors p-2"
            >
              <X size={20} />
            </button>
          </div>

          {/* Content */}
          <div className="flex-1 overflow-y-auto p-4 md:p-6 space-y-4 font-mono text-sm relative archival-scanlines">
            {loading && <div className="text-cyan-500 animate-pulse">Decrypting log...</div>}
            {error && <div className="text-red-500">Error: {error}</div>}
            
            {!loading && !error && messages.map((msg, idx) => {
              // Group consecutive messages by the same author
              const prevMsg = idx > 0 ? messages[idx - 1] : null;
              const isNewAuthor = !prevMsg || prevMsg.author !== msg.author;
              
              const isDerek = msg.author === "Derek Vasilakis";
              const isMerry = msg.author === "Merry";
              
              // Decorative styles
              const alignClass = isMerry ? "items-end" : isDerek ? "items-start" : "items-center";
              const bubbleClass = isMerry 
                ? "bg-cyan-900/40 border-cyan-500/50 text-cyan-100 rounded-tl-xl rounded-tr-xl rounded-bl-xl rounded-br-sm" 
                : isDerek
                ? "bg-purple-900/40 border-purple-500/50 text-purple-100 rounded-tr-xl rounded-tl-xl rounded-br-xl rounded-bl-sm"
                : "bg-neutral-900/80 border-neutral-700/50 text-neutral-400 rounded-lg text-center text-xs";
              
              const targetGlow = msg.isTarget ? (isMerry ? "shadow-[0_0_15px_rgba(53,224,255,0.3)] border-cyan-400 ring-1 ring-cyan-400/50" : "shadow-[0_0_15px_rgba(168,85,247,0.3)] border-purple-400 ring-1 ring-purple-400/50") : "";

              if (!msg.text.trim()) return null;

              return (
                <div key={msg.lineNum} className={`flex flex-col ${alignClass} w-full`}>
                  {isNewAuthor && (isMerry || isDerek) && (
                    <div className={`text-[10px] text-neutral-500 mb-1 tracking-wider uppercase ${isMerry ? "mr-1" : "ml-1"}`}>
                      {msg.author} • {msg.timestamp}
                    </div>
                  )}
                  <div className={`max-w-[85%] p-3 border ${bubbleClass} ${targetGlow} relative group`}>
                    {msg.isTarget && (
                      <div className="absolute -left-2 top-1/2 -translate-y-1/2 w-1 h-full max-h-[80%] bg-white/20 rounded-full" />
                    )}
                    <span className="opacity-90 leading-relaxed whitespace-pre-wrap">{msg.text}</span>
                    <div className="absolute top-1 right-1 opacity-0 group-hover:opacity-100 transition-opacity text-[8px] text-white/30">
                      L{msg.lineNum}
                    </div>
                  </div>
                </div>
              );
            })}
          </div>
        </motion.div>
      </motion.div>
      )}
    </AnimatePresence>
  );
}
