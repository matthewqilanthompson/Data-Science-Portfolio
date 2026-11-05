"""Professional icon set v2: restrained slate ramp + one accent per icon (green = bio/research,
blue = data/tech). 16x16 native, exported at 2x (32 px). Section icons + project thumbnails.
Usage: python3 icons2.py <out_dir>   -> icons/*.png, projects/*.png, review.png
"""
from __future__ import annotations

import math
import sys
from pathlib import Path

from PIL import Image

PAL = {
    "o": "#1b222c",                                                     # soft outline
    "1": "#3a424d", "2": "#5b6572", "3": "#8b949e", "4": "#c3cad3", "5": "#eef1f4",   # slate ramp
    "g": "#2f8f4e", "G": "#56c271", "h": "#a6e3b5",                     # green accent
    "b": "#2f6fc0", "B": "#5a9bea", "c": "#a9cdf6",                     # blue accent
}


class Spr:
    def __init__(self, w=16, h=16):
        self.w, self.h, self.px = w, h, {}

    def put(self, x, y, c):
        if 0 <= x < self.w and 0 <= y < self.h:
            self.px[(x, y)] = c

    def rect(self, x0, y0, x1, y1, c):
        for y in range(y0, y1 + 1):
            for x in range(x0, x1 + 1):
                self.put(x, y, c)

    def line(self, x0, y0, x1, y1, c, th=1):
        n = max(abs(x1 - x0), abs(y1 - y0), 1)
        for i in range(n + 1):
            x, y = round(x0 + (x1 - x0) * i / n), round(y0 + (y1 - y0) * i / n)
            for dx in range(th):
                for dy in range(th):
                    self.put(x + dx, y + dy, c)

    def circle(self, cx, cy, r, c, ring=None):
        for y in range(self.h):
            for x in range(self.w):
                d = math.hypot(x + 0.5 - cx, y + 0.5 - cy)
                if d <= r:
                    self.put(x, y, ring if (ring and d > r - 1.1) else c)

    def image(self, scale=2):
        full = dict(self.px)
        for (x, y) in self.px:
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                q = (x + dx, y + dy)
                if q not in self.px and 0 <= q[0] < self.w and 0 <= q[1] < self.h:
                    full[q] = "o"
        im = Image.new("RGBA", (self.w, self.h), (0, 0, 0, 0))
        for (x, y), c in full.items():
            h = PAL[c]
            im.putpixel((x, y), tuple(int(h[i:i + 2], 16) for i in (1, 3, 5)) + (255,))
        return im.resize((self.w * scale, self.h * scale), Image.Resampling.NEAREST)


# ---------------- section icons ----------------
def education():
    s = Spr()
    for i, hw in enumerate((2, 5, 8, 5, 2)):
        y = 3 + i
        for x in range(8 - hw, 8 + hw):
            s.put(x, y, "4" if (y < 5 and x < 8) else ("3" if y <= 5 else "2"))
    s.rect(4, 7, 11, 11, "2"); s.rect(4, 7, 5, 11, "3"); s.rect(4, 11, 11, 11, "1")
    s.put(8, 5, "5")
    s.line(9, 5, 14, 5, "G"); s.line(15, 6, 15, 9, "G"); s.rect(14, 10, 15, 12, "g"); s.put(14, 10, "h")
    return s


def research():                       # microscope
    s = Spr()
    s.line(4, 1, 8, 6, "3", 2); s.line(4, 1, 7, 5, "4"); s.rect(3, 0, 5, 1, "2")
    s.rect(8, 7, 9, 8, "1")
    s.line(9, 5, 11, 4, "2", 2); s.line(11, 4, 12, 7, "2", 2); s.rect(12, 7, 13, 12, "2"); s.rect(12, 7, 12, 12, "3")
    s.rect(4, 10, 12, 10, "3"); s.rect(5, 9, 8, 9, "G")
    s.put(8, 11, "h")
    s.rect(3, 13, 14, 14, "2"); s.rect(3, 13, 14, 13, "3"); s.rect(3, 13, 4, 14, "4")
    return s


def presentations():                  # poster on a stand
    s = Spr()
    s.rect(2, 1, 13, 10, "5"); s.rect(2, 1, 13, 1, "4")
    s.rect(4, 3, 11, 3, "2")
    s.rect(4, 5, 7, 8, "c"); s.put(4, 5, "5")
    for i, (x, hgt) in enumerate(((9, 2), (10, 3), (11, 4))):
        s.rect(x, 8 - hgt, x, 8, "G" if i == 2 else "3")
    s.rect(7, 11, 8, 13, "2"); s.rect(4, 14, 11, 14, "2"); s.rect(4, 14, 11, 14, "3")
    return s


def projects():                       # bar chart with trend
    s = Spr()
    s.line(1, 1, 1, 14, "3"); s.line(1, 14, 15, 14, "3")
    for x, hgt in ((3, 4), (6, 7), (9, 6), (12, 11)):
        s.rect(x, 13 - hgt, x + 1, 13, "b"); s.rect(x, 13 - hgt, x, 13, "B")
    s.line(3, 7, 13, 1, "G")
    return s


def software():                       # terminal
    s = Spr()
    s.rect(0, 2, 15, 13, "1"); s.rect(0, 2, 15, 3, "3"); s.rect(0, 2, 15, 2, "4")
    for x in (2, 4, 6):
        s.put(x, 3, "2")
    s.put(2, 6, "G"); s.put(3, 7, "G"); s.put(2, 8, "G")
    s.rect(5, 8, 7, 8, "B")
    s.rect(2, 10, 9, 10, "3"); s.rect(2, 12, 6, 12, "2")
    return s


def skills():                         # briefcase-style toolbox, slate with a blue clasp
    s = Spr()
    s.rect(5, 2, 10, 2, "3"); s.rect(5, 2, 5, 5, "3"); s.rect(10, 2, 10, 5, "2")
    s.rect(1, 6, 14, 14, "2"); s.rect(1, 6, 14, 6, "4"); s.rect(1, 6, 2, 14, "3"); s.rect(1, 14, 14, 14, "1")
    s.rect(1, 9, 14, 9, "1")
    s.rect(7, 8, 8, 10, "B"); s.put(7, 8, "c")
    return s


def looking():                        # magnifier
    s = Spr()
    s.circle(6, 6, 4.6, "c", ring="3")
    s.put(4, 4, "5"); s.put(5, 4, "5"); s.put(4, 5, "5")
    s.line(9, 9, 14, 14, "2", 2); s.line(9, 9, 13, 13, "3")
    return s


def connect():                        # envelope
    s = Spr()
    s.rect(1, 4, 14, 12, "5"); s.rect(1, 12, 14, 12, "4"); s.rect(14, 4, 14, 12, "4")
    for i in range(7):
        s.put(1 + i, 4 + i, "3"); s.put(14 - i, 4 + i, "3")
    s.rect(7, 9, 8, 10, "B")
    return s


# ---------------- project thumbnails ----------------
def p_sql():                          # database cylinder with table rows
    s = Spr()
    for y in range(2, 15):
        for x in range(2, 14):
            s.put(x, y, "B" if x < 4 else "b")
    for x in range(3, 13):
        s.put(x, 1, "c"); s.put(x, 15, "b")
    for y in (5, 9, 13):
        s.rect(2, y, 13, y, "c")
    s.rect(3, 2, 12, 3, "c"); s.rect(4, 2, 6, 2, "5")
    return s


def p_readmit():                      # ROC curve
    s = Spr()
    s.rect(1, 1, 14, 14, "5"); s.rect(1, 1, 14, 1, "4")
    s.line(2, 13, 13, 2, "4")                                   # chance diagonal
    pts = [(2, 13), (2, 9), (3, 6), (5, 4), (8, 3), (13, 2)]
    for a, b in zip(pts, pts[1:]):
        s.line(*a, *b, "b")
    s.rect(9, 10, 12, 12, "G"); s.put(9, 10, "h")              # 'AUC' block, filled
    return s


def p_taxa():                         # phylogenetic tree
    s = Spr()
    s.line(1, 8, 4, 8, "2"); s.line(4, 3, 4, 13, "2")
    s.line(4, 3, 8, 3, "2"); s.line(4, 13, 8, 13, "2")
    s.line(8, 1, 8, 5, "2"); s.line(8, 11, 8, 15, "2")
    for y, c in ((1, "G"), (5, "G"), (11, "B"), (15, "B")):
        s.line(8, y, 12, y, "3"); s.rect(13, y - 1 if y > 0 else 0, 14, y, c)
    return s


def p_viz():                          # area/line plot
    s = Spr()
    s.line(1, 1, 1, 14, "3"); s.line(1, 14, 15, 14, "3")
    top = [10, 9, 9, 7, 8, 6, 5, 6, 4, 3, 4, 2, 3]
    for i, t in enumerate(top):
        x = 2 + i
        s.rect(x, t, x, 13, "G")
        s.put(x, t, "g")
    low = [12, 12, 11, 11, 11, 10, 10, 10, 9, 9, 9, 8, 8]
    for i, t in enumerate(low):
        s.rect(2 + i, t, 2 + i, 13, "c")
    return s


def p_emotion():                      # speech bubble with tag dots
    s = Spr()
    s.rect(1, 2, 14, 10, "5"); s.rect(1, 2, 14, 2, "4")
    for xy in ((1, 2), (14, 2), (1, 10), (14, 10)):
        s.px.pop(xy, None)
    s.line(4, 11, 3, 14, "5"); s.put(5, 11, "5"); s.put(4, 12, "5")
    for x, c in ((4, "G"), (7, "B"), (10, "3")):
        s.rect(x, 5, x + 1, 7, c)
    return s


def p_kiosk():                        # health kiosk: screen on a stand with a plus sign
    s = Spr()
    s.rect(3, 1, 12, 9, "1"); s.rect(4, 2, 11, 8, "c"); s.rect(4, 2, 11, 2, "5")
    s.rect(7, 3, 8, 7, "G"); s.rect(5, 4, 10, 5, "G"); s.rect(7, 4, 8, 5, "h")
    s.rect(7, 10, 8, 13, "2"); s.rect(4, 14, 11, 14, "2"); s.rect(4, 14, 11, 14, "3")
    return s


def p_bot():                          # chat bubble with a check mark: grammar feedback bot
    s = Spr()
    s.rect(1, 2, 14, 10, "5"); s.rect(1, 2, 14, 2, "4")
    for xy in ((1, 2), (14, 2), (1, 10), (14, 10)):
        s.px.pop(xy, None)
    s.line(10, 11, 12, 14, "5"); s.put(11, 11, "5"); s.put(11, 12, "5")
    for xy in ((4, 6), (5, 7), (6, 8), (7, 7), (8, 6), (9, 5), (10, 4)):
        s.put(*xy, "G")
    s.put(6, 7, "h")
    return s


SECTIONS = {"education": education, "research": research, "presentations": presentations,
            "projects": projects, "software": software, "skills": skills, "looking": looking, "connect": connect}
PROJECTS = {"sql": p_sql, "readmission": p_readmit, "taxa": p_taxa, "viz": p_viz,
            "emotion": p_emotion, "kiosk": p_kiosk, "bot": p_bot}


def main():
    out = Path(sys.argv[1])
    tiles = []
    for folder, group in (("icons", SECTIONS), ("projects", PROJECTS)):
        (out / folder).mkdir(parents=True, exist_ok=True)
        for name, fn in group.items():
            sp = fn()
            sp.image(2).save(out / folder / f"{name}.png")
            tiles.append(sp.image(6))
    bands = []
    for bg in ("#0d1117", "#ffffff"):
        band = Image.new("RGB", (len(tiles) * 110 + 10, 116), bg)
        for i, t in enumerate(tiles):
            band.paste(t, (10 + i * 110, 10), t)
        bands.append(band)
    sheet = Image.new("RGB", (bands[0].width, 2 * 116 + 4), "#555")
    sheet.paste(bands[0], (0, 0)); sheet.paste(bands[1], (0, 120))
    sheet.save(out / "review.png")
    print("section", len(SECTIONS), "project", len(PROJECTS))


if __name__ == "__main__":
    main()
