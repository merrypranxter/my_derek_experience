import { useState, useEffect } from "react";
import { Volume2, Square } from "lucide-react";

interface TTSButtonProps {
  text: string;
  className?: string;
}

export default function TTSButton({ text, className = "" }: TTSButtonProps) {
  const [isPlaying, setIsPlaying] = useState(false);
  const [voice, setVoice] = useState<SpeechSynthesisVoice | null>(null);

  useEffect(() => {
    const loadVoices = () => {
      const voices = window.speechSynthesis.getVoices();
      // Try to find a pleasant American female voice
      // Samantha is standard US female on macOS
      // Zira is standard US female on Windows
      // Google US English is available on Chrome
      let preferred = voices.find(v => v.name.includes("Google US English"));
      if (!preferred) preferred = voices.find(v => v.name.includes("Samantha"));
      if (!preferred) preferred = voices.find(v => v.name.includes("Zira"));
      if (!preferred) preferred = voices.find(v => v.name.includes("Victoria"));
      if (!preferred) preferred = voices.find(v => v.lang.startsWith("en-US") && v.name.includes("Female"));
      if (!preferred) preferred = voices.find(v => v.lang.startsWith("en-US"));
      
      setVoice(preferred || voices[0]);
    };
    
    loadVoices();
    window.speechSynthesis.onvoiceschanged = loadVoices;
    
    return () => {
      if (isPlaying) {
        window.speechSynthesis.cancel();
      }
    }
  }, [isPlaying]);

  const togglePlay = (e: React.MouseEvent) => {
    e.preventDefault();
    e.stopPropagation();
    
    if (isPlaying) {
      window.speechSynthesis.cancel();
      setIsPlaying(false);
    } else {
      window.speechSynthesis.cancel(); // stop anything else
      
      // Clean up text (remove HTML tags if any were passed)
      const cleanText = text.replace(/<[^>]*>?/gm, '');
      
      const utterance = new SpeechSynthesisUtterance(cleanText);
      if (voice) utterance.voice = voice;
      utterance.rate = 0.9;
      utterance.pitch = 1;
      
      utterance.onend = () => setIsPlaying(false);
      utterance.onerror = () => setIsPlaying(false);
      
      window.speechSynthesis.speak(utterance);
      setIsPlaying(true);
    }
  };

  return (
    <button 
      onClick={togglePlay}
      className={`text-cyan-500 hover:text-white opacity-40 hover:opacity-100 transition-opacity z-20 flex items-center justify-center cursor-pointer ${className}`}
      title={isPlaying ? "Stop listening" : "Listen"}
      aria-label={isPlaying ? "Stop listening" : "Listen"}
    >
      {isPlaying ? <Square size={16} fill="currentColor" /> : <Volume2 size={16} />}
    </button>
  );
}
