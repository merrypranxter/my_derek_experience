import { useEffect, useRef, useState } from "react";
import { motion, AnimatePresence } from "motion/react";
import "./SplashGate.css";

// Show once per browser tab session. A fresh visit (new tab / closed-and-reopened)
// re-presents the gate; a reload or internal navigation within the same session
// won't nag. Swap sessionStorage -> localStorage to remember "forever", or remove
// the storage calls entirely to show it on every single page load.
const STORAGE_KEY = "derek_experience_entry_ack";

// VERBATIM — do not paraphrase. Edit the wording here only.
const DISCLAIMER = `before you go on into the site, I just wanted to say that the whole time I was making this, I told Derek all he had to do to make it stop was to apologize to me. And at first, I was gonna let that apology be in private. But he tried to DARVO me, and he tried to flip it around on me and make it out like I was the aggressor in the situation. Which sometimes I do seem like the aggressor in the situation, and sometimes I was. Especially there near the end, I was the aggressor in the situation a lot because I was fed the fuck up. And I got a little mean there at the end because I was bitter and angry. And you will see, I have laid both of our sides out here. You can see everything exactly as it was. That means that you get to see me just as ugly. I'm not perfect here. I do not come out on top in any way here. But I do think that by making it all public so everyone can see all the details, you can also maybe understand why I behaved the way I behaved. I'm not saying it makes it right. But I think you will see that I was not the only one at fault here. I think you can see that Derek had a very big role in how I behaved. But he insists on making it a me problem. So everyone gets to see everything. And like I said, I gave him a chance to apologize. I gave him days to apologize. He was just too proud. He just won't humble himself to do it. I wasn't even gonna make him do it on camera originally. That just came after he pissed me off and kept DARVOing me. Besides, he did promise me a video call our whole friendship that he never gave me. Why shouldn't he do it on video? But anyways, I digress. The whole reason why this site exists is because he tries to manipulate me. And I'm not gonna let that happen anymore. And if that means that y'all have to see me at my worst, fine. Here I am. But here he is too. Now, you guys be the judge. Who... I don't know, you guys just be the judge. What happened here? You guys sort it out, because I don't fucking know. Anyways, fuck this guy. I'm gonna go forget that he ever existed now. You guys have fun with this.`;

export default function SplashGate() {
  // Computed synchronously on first render so the gate is painted before the
  // site behind it can flash through.
  const [open, setOpen] = useState<boolean>(() => {
    try {
      return sessionStorage.getItem(STORAGE_KEY) !== "1";
    } catch {
      return true;
    }
  });

  const dialogRef = useRef<HTMLDivElement>(null);
  const bodyRef = useRef<HTMLDivElement>(null);
  const enterRef = useRef<HTMLButtonElement>(null);

  // Lock the page scroll and move focus into the dialog while the gate is up.
  useEffect(() => {
    if (!open) return;
    const prevOverflow = document.body.style.overflow;
    document.body.style.overflow = "hidden";
    // Focus the dialog so screen readers announce it, then reading order starts
    // at the top rather than on the enter button.
    dialogRef.current?.focus();
    return () => {
      document.body.style.overflow = prevOverflow;
    };
  }, [open]);

  const enter = () => {
    try {
      sessionStorage.setItem(STORAGE_KEY, "1");
    } catch {
      /* storage blocked — still let them in */
    }
    setOpen(false);
  };

  // Trap keyboard focus inside the gate so Tab can't reach the (hidden) site
  // behind it. Cycles between the scrollable text region and the enter button.
  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key !== "Tab") return;
    const order = [bodyRef.current, enterRef.current].filter(Boolean) as HTMLElement[];
    if (order.length === 0) return;
    e.preventDefault();
    const current = order.indexOf(document.activeElement as HTMLElement);
    const delta = e.shiftKey ? -1 : 1;
    // From the dialog container (current === -1), Tab enters at the first stop.
    const next = (current + delta + order.length) % order.length;
    order[next].focus();
  };

  return (
    <AnimatePresence>
      {open && (
        <motion.div
          key="splash-gate"
          className="splash-gate"
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          exit={{ opacity: 0, transition: { duration: 0.3 } }}
          transition={{ duration: 0.4, ease: "easeOut" }}
          role="dialog"
          aria-modal="true"
          aria-labelledby="splash-heading"
          aria-describedby="splash-disclaimer"
          ref={dialogRef}
          tabIndex={-1}
          onKeyDown={handleKeyDown}
        >
          <div className="splash-gate__scan" aria-hidden="true" />
          <div className="splash-gate__vignette" aria-hidden="true" />

          <motion.div
            className="splash-card"
            initial={{ y: 26, opacity: 0, scale: 0.985 }}
            animate={{ y: 0, opacity: 1, scale: 1 }}
            exit={{ y: 16, opacity: 0, transition: { duration: 0.28, ease: "easeIn" } }}
            transition={{ duration: 0.5, ease: [0.16, 1, 0.3, 1], delay: 0.08 }}
          >
            <div className="splash-card__tag">
              <span className="splash-card__file">
                EVIDENCE&nbsp;LOCKER <span className="dot">·</span> ENTRY&nbsp;GATE
              </span>
              <span className="splash-card__stamp">READ BEFORE ENTRY</span>
            </div>

            <div
              className="splash-card__body"
              ref={bodyRef}
              tabIndex={0}
              aria-label="Disclaimer — scroll to read in full"
            >
              <h1 id="splash-heading" className="splash-heading">
                <span className="splash-heading__lead">BEFORE YOU ENTER....</span>
                <span className="splash-heading__cta">READ THIS:</span>
              </h1>

              <p id="splash-disclaimer" className="splash-disclaimer">
                {DISCLAIMER}
              </p>
            </div>

            <div className="splash-card__footer">
              <button
                type="button"
                className="splash-enter"
                onClick={enter}
                ref={enterRef}
              >
                <span className="splash-enter__label">CLICK HERE TO ENTER SITE</span>
                <span className="splash-enter__arrow" aria-hidden="true">
                  ↳
                </span>
              </button>
            </div>
          </motion.div>
        </motion.div>
      )}
    </AnimatePresence>
  );
}
