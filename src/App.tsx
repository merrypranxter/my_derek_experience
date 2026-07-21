import { BrowserRouter, Routes, Route, Link, useLocation } from "react-router-dom";
import Home from "./pages/Home";
import ModulePage from "./pages/ModulePage";
import VisualEvidence from "./pages/VisualEvidence";
import ShaderBackground from "./components/ShaderBackground";

function GlobalStamp() {
  const location = useLocation();
  if (location.pathname !== "/") return null;

  return (
    <Link 
      to="/evidence" 
      className="fixed top-8 left-8 z-[100] group transform hover:scale-105 transition-transform"
    >
      <div className="border-4 border-red-600 px-4 py-2 -rotate-[12deg] text-red-600 font-black text-2xl md:text-3xl tracking-tighter uppercase opacity-80 mix-blend-screen shadow-[0_0_20px_rgba(220,38,38,0.3)] group-hover:opacity-100 group-hover:border-red-500 group-hover:text-red-500 group-hover:shadow-[0_0_30px_rgba(220,38,38,0.6)] backdrop-blur-sm pointer-events-auto">
        <div className="absolute inset-0 border border-red-600/50 m-1 pointer-events-none"></div>
        Visual Evidence
      </div>
    </Link>
  );
}

export default function App() {
  return (
    <BrowserRouter>
      <div className="relative min-h-screen bg-[var(--atm-bg)] text-white overflow-hidden selection:bg-cyan-500 selection:text-black font-data">
        <ShaderBackground />
        
        <GlobalStamp />

        <div className="relative z-10 h-full overflow-y-auto h-screen archival-scanlines">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/module/:id" element={<ModulePage />} />
            <Route path="/evidence" element={<VisualEvidence />} />
          </Routes>
        </div>
      </div>
    </BrowserRouter>
  );
}
