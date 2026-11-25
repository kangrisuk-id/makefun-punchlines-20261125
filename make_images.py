"""Build-time image generator for the README gallery (not the entry).

Renders cover.png + three card images with Pillow. Run once:
    python3 make_images.py
Outputs land in assets/.
"""

import os

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "assets")

BG = (18, 18, 22)          # deep charcoal
PANEL = (32, 32, 40)
GOLD = (212, 175, 55)
CREAM = (245, 240, 225)
MUTED = (160, 155, 140)
BLUE = (96, 165, 250)


def font(name, size):
    for path in (
        f"/usr/share/fonts/truetype/dejavu/{name}.ttf",
        f"/usr/share/fonts/{name}.ttf",
    ):
        if os.path.exists(path):
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = f"{cur} {w}".strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def base(w, h):
    img = Image.new("RGB", (w, h), BG)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, w - 1, 10], fill=GOLD)
    d.rectangle([0, h - 11, w - 1, h - 1], fill=GOLD)
    return img, d


def centred(d, y, text, fnt, fill, w):
    d.text(((w - d.textlength(text, font=fnt)) / 2, y), text, font=fnt, fill=fill)


def cover():
    w, h = 1280, 720
    img, d = base(w, h)
    centred(d, 70, "MONDAY MORNING", font("DejaVuSans-Bold", 84), CREAM, w)
    centred(d, 165, "PUNCHLINES", font("DejaVuSans-Bold", 84), GOLD, w)
    centred(d, 290, "The bed sued for custody — and won.", font("DejaVuSans", 34), MUTED, w)
    d.rounded_rectangle([140, 380, 1140, 560], radius=18, fill=PANEL, outline=GOLD, width=3)
    f = font("DejaVuSans-Bold", 40)
    lines = wrap(d, "\u201cMy bed filed for custody of me on Monday mornings. The judge ruled in its favour.\u201d", f, 900)
    y = 410
    for ln in lines:
        centred(d, y, ln, f, CREAM, w)
        y += 52
    centred(d, 640, "81 characters  ·  24/25 tournament winner  ·  $5 bounty, 3 paid places",
            font("DejaVuSans", 26), MUTED, w)
    img.save(os.path.join(OUT, "cover.png"))


def card_winner():
    w, h = 1280, 800
    img, d = base(w, h)
    centred(d, 60, "THE WINNING JOKE", font("DejaVuSans-Bold", 44), GOLD, w)
    centred(d, 130, "81 characters — absurd legal, two-beat punchline", font("DejaVuSans", 28), MUTED, w)
    d.rounded_rectangle([110, 220, 1170, 520], radius=18, fill=PANEL, outline=GOLD, width=3)
    f = font("DejaVuSans-Bold", 46)
    lines = wrap(d, "\u201cMy bed filed for custody of me on Monday mornings. The judge ruled in its favour.\u201d", f, 940)
    y = 270
    for ln in lines:
        centred(d, y, ln, f, CREAM, w)
        y += 62
    centred(d, 600, "Criterion 1–5: 5 · 5 · 5 · 4 · 5  =  24/25",
            font("DejaVuSans-Bold", 30), BLUE, w)
    centred(d, 670, "Beat 1: the bed files for custody.  Beat 2: the judge sides with the bed.",
            font("DejaVuSans", 26), MUTED, w)
    img.save(os.path.join(OUT, "card-winner.png"))


def card_runner_up():
    w, h = 1280, 800
    img, d = base(w, h)
    centred(d, 60, "RUNNER-UP — LOST THE FINAL 24/25 vs 24/25", font("DejaVuSans-Bold", 36), GOLD, w)
    centred(d, 130, "Negotiation device — decided on economy (81 vs 93 chars)", font("DejaVuSans", 28), MUTED, w)
    d.rounded_rectangle([110, 220, 1170, 520], radius=18, fill=PANEL, outline=MUTED, width=3)
    f = font("DejaVuSans-Bold", 44)
    lines = wrap(d, "\u201cI tried to negotiate with Monday. It offered me Tuesday as a compromise and kept the weekend.\u201d", f, 940)
    y = 270
    for ln in lines:
        centred(d, y, ln, f, CREAM, w)
        y += 60
    centred(d, 600, "Criterion 1–5: 5 · 5 · 5 · 4 · 5  =  24/25",
            font("DejaVuSans-Bold", 30), BLUE, w)
    centred(d, 670, "Same score, longer text — the tie-break favours the shorter line.",
            font("DejaVuSans", 26), MUTED, w)
    img.save(os.path.join(OUT, "card-runner-up.png"))


def card_bracket():
    w, h = 1280, 800
    img, d = base(w, h)
    centred(d, 60, "THE TOURNAMENT — 24 CANDIDATES, 8 SEEDS", font("DejaVuSans-Bold", 40), GOLD, w)
    rows = [
        ("QF1", "#3 Negotiation  beats  #8 Shower dialogue"),
        ("QF2", "#4 Bed custody  beats  #7 Performance review"),
        ("QF3", "#1 Five alarms  beats  #19 Cc'd my boss"),
        ("QF4", "#9 Slept through it  beats  #2 Fridge raid"),
        ("SF1", "#3 Negotiation  beats  #9 Unemployed Tuesday"),
        ("SF2", "#4 Bed custody  beats  #1 Five alarms"),
        ("FINAL", "#4 Bed custody  beats  #3 Negotiation — economy"),
    ]
    f_lab = font("DejaVuSans-Bold", 32)
    f_txt = font("DejaVuSans", 32)
    y = 170
    for lab, txt in rows:
        d.text((140, y), lab, font=f_lab, fill=GOLD if lab == "FINAL" else CREAM)
        d.text((330, y), txt, font=f_txt, fill=CREAM)
        y += 62
    centred(d, 640, "Self-pairwise: winner #4 held against runners-up #3 and #1",
            font("DejaVuSans", 28), MUTED, w)
    centred(d, 700, "Full scores in candidates.md", font("DejaVuSans", 28), MUTED, w)
    img.save(os.path.join(OUT, "card-bracket.png"))


def main():
    os.makedirs(OUT, exist_ok=True)
    cover()
    card_winner()
    card_runner_up()
    card_bracket()
    for name in ("cover.png", "card-winner.png", "card-runner-up.png", "card-bracket.png"):
        p = os.path.join(OUT, name)
        print(name, os.path.getsize(p), "bytes")


if __name__ == "__main__":
    main()
