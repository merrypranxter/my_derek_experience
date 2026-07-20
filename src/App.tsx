import { BrowserRouter, Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import ModulePage from "./pages/ModulePage";
import ShaderBackground from "./components/ShaderBackground";

export default function App() {
  return (
    <BrowserRouter>
      <div className="relative min-h-screen bg-[var(--atm-bg)] text-white overflow-hidden selection:bg-cyan-500 selection:text-black font-data">
        <ShaderBackground />
        <div className="relative z-10 h-full overflow-y-auto h-screen archival-scanlines">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/module/:id" element={<ModulePage />} />
          </Routes>
        </div>
      </div>
    </BrowserRouter>
  );
}
