with open("src/pages/ModulePage.tsx", "r") as f:
    content = f.read()

import re
content = re.sub(
    r"const EVIDENCE_BUCKET = '/derek_original_chat\.txt\.pdf';\s*const SOURCE_REGISTRY: Record<string, \{label: string, meaning: string, url\?: string\}> = \{.*?\};",
    """const EVIDENCE_BUCKET = 'https://console.cloud.google.com/storage/browser/astraltrash_other/derek?project=gen-lang-client-0646349261&pageState=(%22StorageObjectListTable%22:(%22f%22:%22%255B%255D%22))';
const SOURCE_REPO = 'https://github.com/merrypranxter/fuckyou_derek';

const SOURCE_REGISTRY: Record<string, {label: string, meaning: string, url?: string}> = {
  'WA':
    { label:'WA-####', meaning:'WhatsApp chat export — message ID in the captured log (Nov 5 2025 – Feb 16 2026).', url:SOURCE_REPO + '/tree/main/evidence/whatsapp' },
  'SC':
    { label:'SC-####', meaning:'StarMaker record — post, comment, or duet ID.', url:EVIDENCE_BUCKET },
  'STARMAKER': { label:'STARMAKER', meaning:'StarMaker app record — the public profile and its posts.', url:EVIDENCE_BUCKET },
  'DOSSIER':   { label:'DOSSIER §', meaning:'The Forensic Audit Dossier — the full compiled report.', url:SOURCE_REPO + '/blob/main/reports/FORENSIC_AUDIT_DOSSIER.md' },
  'FORENSIC_PATTERN_ANALYSIS': { label:'FORENSIC PATTERN ANALYSIS', meaning:'Cross-case forensic pattern analysis document.', url:SOURCE_REPO + '/blob/main/reports/FORENSIC_PATTERN_ANALYSIS.md' },
  'GA':
    { label:'GA — GHOST ANALYSIS', meaning:'Independent AI forensic audit of the original chat export — NODE_771, GHOST_FRAGMENT v2.6. Full session transcript on file.', url:SOURCE_REPO + '/tree/main/forensics' },
  'TESTIMONY': { label:'TESTIMONY', meaning:'First-person account of the Operative — events from the era the log does not recover.' }
};""",
    content,
    flags=re.DOTALL
)

with open("src/pages/ModulePage.tsx", "w") as f:
    f.write(content)
