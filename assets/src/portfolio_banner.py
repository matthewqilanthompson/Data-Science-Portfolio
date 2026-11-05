"""Portfolio banner concepts (still), 200x40 native, exported at 4x (800x160). Reuses the muted icon set.
A = pipeline (research -> database -> model -> findings -> poster), B = project shelf, C = analyst desk.
Usage: python3 portfolio_banner.py <out_dir>
"""
from __future__ import annotations

import sys
from pathlib import Path

from PIL import Image

sys.path.insert(0, str(Path(__file__).parent))
import icons2 as I  # noqa: E402

W, H, SCALE = 200, 40, 4
CARD, GRID, GRID2 = (22, 27, 34), (30, 36, 45), (38, 45, 56)


def hexrgb(h):
    return tuple(int(h[i:i + 2], 16) for i in (1, 3, 5))


def card(grid=True):
    im = Image.new("RGB", (W, H), CARD)
    if grid:
        px = im.load()
        for y in range(H):
            for x in range(W):
                if x % 8 == 0 or y % 8 == 0:
                    px[x, y] = GRID2 if (x % 40 == 0 or y % 40 == 0) else GRID
    return im


def paste(im, spr, x, y):
    s = spr.image(1)
    im.paste(s, (x, y), s)


def dotted(im, x0, x1, y, col, gap=2):
    px = im.load()
    for x in range(x0, x1):
        if (x - x0) % (gap + 1) == 0:
            px[x, y] = col
    for d in (1, 2):                                   # arrowhead
        px[x1 - d, y - d] = col
        px[x1 - d, y + d] = col


def concept_a():
    im = card()
    steps = [I.research(), I.p_sql(), I.p_readmit(), I.p_taxa(), I.presentations()]
    xs = [14, 54, 94, 134, 174]
    for i, (spr, x) in enumerate(zip(steps, xs)):
        paste(im, spr, x - 2, 12)
        if i < len(xs) - 1:
            dotted(im, x + 17, xs[i + 1] - 5, 20, hexrgb(I.PAL["G"] if i % 2 == 0 else I.PAL["B"]))
    return im


def concept_b():
    im = card(grid=False)
    px = im.load()
    for x in range(8, W - 8):                         # two slate shelves with a lit top edge
        for y, top in ((19, True), (37, True)):
            px[x, y] = hexrgb(I.PAL["4"]) if top else hexrgb(I.PAL["2"])
            px[x, y + 1] = hexrgb(I.PAL["2"])
    items = [I.p_sql(), I.p_readmit(), I.p_emotion(), I.p_taxa(), I.p_viz(), I.p_kiosk(), I.p_bot()]
    for i, spr in enumerate(items):                   # alternate shelves, evenly spaced
        x = 16 + i * 25
        y = 3 if i % 2 == 0 else 21
        paste(im, spr, x, y)
    return im


def concept_c():
    im = card(grid=False)
    px = im.load()
    for x in range(0, W):                             # desk surface + front edge
        for y in range(32, H):
            px[x, y] = hexrgb(I.PAL["2"]) if y == 32 else hexrgb(I.PAL["1"])
        px[x, 31] = hexrgb(I.PAL["3"])
    # monitor: 40x24 with an ROC-style chart on screen
    mx, my = 80, 4
    for y in range(my, my + 22):
        for x in range(mx, mx + 40):
            edge = x in (mx, mx + 39) or y in (my, my + 21)
            px[x, y] = hexrgb(I.PAL["1"]) if edge else hexrgb("#0f2346")
    for x in range(mx + 4, mx + 36):
        px[x, my + 18] = hexrgb(I.PAL["3"])
    for y in range(my + 3, my + 19):
        px[mx + 4, y] = hexrgb(I.PAL["3"])
    pts = [(4, 18), (5, 12), (8, 8), (14, 5), (24, 4), (35, 3)]
    for (a, b), (c, d) in zip(pts, pts[1:]):
        n = max(abs(c - a), abs(d - b))
        for t in range(n + 1):
            px[mx + round(a + (c - a) * t / n), my + round(b + (d - b) * t / n)] = hexrgb(I.PAL["B"])
    for x in range(mx + 18, mx + 22):
        for y in range(my + 22, my + 27):
            px[x, y] = hexrgb(I.PAL["2"])
    paste(im, I.research(), 30, 15)                   # microscope
    paste(im, I.p_sql(), 56, 15)                       # database "on the desk"
    paste(im, I.p_taxa(), 132, 15)                     # tree printout
    for x in range(158, 176):                         # notebook
        for y in range(24, 31):
            px[x, y] = hexrgb(I.PAL["5"]) if y > 24 else hexrgb(I.PAL["4"])
    for y in (26, 28):
        for x in range(160, 174):
            px[x, y] = hexrgb(I.PAL["3"])
    for x, y in ((186, 22), (185, 20), (187, 19), (184, 23), (188, 23), (186, 18)):   # plant
        px[x, y] = hexrgb(I.PAL["G"])
    for x in range(183, 190):
        for y in range(25, 31):
            px[x, y] = hexrgb(I.PAL["3"])
    return im


def main():
    out = Path(sys.argv[1]); out.mkdir(parents=True, exist_ok=True)
    tiles = []
    for name, fn in (("A-pipeline", concept_a), ("B-shelf", concept_b), ("C-desk", concept_c)):
        big = fn().resize((W * SCALE, H * SCALE), Image.Resampling.NEAREST)
        big.save(out / f"{name}.png")
        tiles.append(big)
    sheet = Image.new("RGB", (W * SCALE + 20, 3 * (H * SCALE + 10) + 10), "#555")
    for i, t in enumerate(tiles):
        sheet.paste(t, (10, 10 + i * (H * SCALE + 10)))
    sheet.save(out / "concepts.png")
    print("ok")


if __name__ == "__main__":
    main()
