import { BrowserRouter, Routes, Route, Link, useLocation } from "react-router-dom";
import Home from "./pages/Home";
import ModulePage from "./pages/ModulePage";
import VisualEvidence from "./pages/VisualEvidence";
import ChatLog from "./pages/ChatLog";
import Legalities from "./pages/Legalities";
import ShaderBackground from "./components/ShaderBackground";
import SplashGate from "./components/SplashGate";
import "./module.css";

function GlobalStamp() {
  const location = useLocation();
  return (
    <>
    {location.pathname === "/" && (
      <Link 
      to="/evidence" 
      className="fixed bottom-6 left-6 z-[100] group transform hover:scale-105 transition-transform"
      style={{
        fontFamily: "var(--font-data)",
        fontSize: ".72rem",
        fontWeight: 700,
        letterSpacing: ".3em",
        textTransform: "uppercase",
        color: "var(--atm-stamp)",
        textDecoration: "none",
        border: "2px solid var(--atm-stamp)",
        padding: ".7em 1.1em",
        transform: "rotate(-5deg)",
        background: "rgb(5 3 15 / .6)",
        transition: "transform 120ms, background 120ms"
      }}
    >
      Visible Evidence ↗
      </Link>
    )}
    <Link
      to="/legalities"
      className="fixed bottom-6 right-6 z-[100] opacity-30 hover:opacity-100 transition-opacity"
      style={{
        fontFamily: "var(--font-data)",
        fontSize: ".6rem",
        letterSpacing: ".2em",
        textTransform: "uppercase",
        color: "#fff",
        textDecoration: "none"
      }}
    >
      LEGALITIES
    </Link>
    </>
  );
}

export default function App() {
  return (
    <BrowserRouter>
      <SplashGate />
      <div className="relative min-h-screen bg-[var(--atm-bg)] text-white overflow-hidden selection:bg-cyan-500 selection:text-black font-data">
        <ShaderBackground />
        
        <GlobalStamp />

        <div className="relative z-10 h-full overflow-y-auto h-screen archival-scanlines">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/module/:id" element={<ModulePage />} />
            <Route path="/evidence" element={<VisualEvidence />} />
            <Route path="/chat" element={<ChatLog />} />
            <Route path="/legalities" element={<Legalities />} />
          </Routes>
        </div>
      </div>
    </BrowserRouter>
  );
}
