import re

with open("src/pages/ModulePage.tsx", "r") as f:
    content = f.read()

target = """              {ex.media && ex.media.length > 0 && (
                <div className="media-grid">
                  {ex.media.map((m, mIdx) => (
                    <div key={mIdx} className="media-item">"""

# Wait let me check the actual code for rendering media from exhibits
# Ah, I don't know the exact structure for media rendering. Let's see if media rendering is even implemented.

