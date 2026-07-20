import { useEffect, useState } from "react";
import { useParams, useNavigate } from "react-router-dom";
import { motion } from "motion/react";
import Markdown from "react-markdown";

const MODULE_MAP: Record<string, string> = {
  "01": "MODULE_01_PROMISES",
  "02": "MODULE_02_WITHHOLDING",
  "03": "MODULE_03_RUG_PULLS",
  "04": "MODULE_04_GASLIGHTING_DARVO",
  "05": "MODULE_05_TRIANGULATION",
  "06": "MODULE_06_EXPLOITATION",
  "07": "MODULE_07_ERASURE",
};

export default function ModulePage() {
  const { id } = useParams<{ id: string }>();
  const navigate = useNavigate();
  const [content, setContent] = useState<string>("");
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (!id || !MODULE_MAP[id]) {
      navigate("/");
      return;
    }

    const fetchModule = async () => {
      try {
        setLoading(true);
        const fileName = MODULE_MAP[id];
        const res = await fetch(`https://raw.githubusercontent.com/merrypranxter/fuckyou_derek/main/modules/${fileName}.md`);
        if (!res.ok) throw new Error("Failed to fetch module");
        const text = await res.text();
        setContent(text);
      } catch (err) {
        setContent("# Error Loading Module\nThe evidence could not be retrieved. Connection severed.");
      } finally {
        setLoading(false);
      }
    };

    fetchModule();
  }, [id, navigate]);

  return (
    <div className="min-h-screen text-white overflow-x-hidden font-sans selection:bg-cyan-500 selection:text-black">
      
      <button 
        onClick={() => navigate("/")}
        className="fixed top-6 left-6 z-50 text-[10px] font-mono uppercase tracking-widest text-neutral-500 hover:text-white transition-colors flex items-center gap-2"
      >
        <span className="text-cyan-500">{"<"}</span> Return to System
      </button>

      <div className="max-w-4xl mx-auto px-6 pt-32 pb-24 relative z-10">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8, ease: [0.16, 1, 0.3, 1] }}
        >
          <div className="font-mono text-xs text-neutral-500 uppercase tracking-widest mb-12 border-b border-white/10 pb-4">
            [ Module {id} Active ]
          </div>
          
          {loading ? (
            <div className="font-mono text-cyan-500 text-sm animate-pulse tracking-widest">
              Extracting receipts...
            </div>
          ) : (
            <div className="prose prose-invert max-w-none prose-headings:font-black prose-headings:tracking-tighter prose-h1:text-5xl prose-h2:text-3xl prose-h2:text-cyan-400 prose-h3:text-pink-500 prose-p:text-neutral-300 prose-a:text-cyan-400 hover:prose-a:text-pink-500 prose-strong:text-white prose-code:text-lime-400 prose-code:bg-white/5 prose-code:px-1 prose-code:rounded">
              <Markdown>{content}</Markdown>
            </div>
          )}
        </motion.div>
      </div>

    </div>
  );
}
