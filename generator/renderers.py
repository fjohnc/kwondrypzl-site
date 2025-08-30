from __future__ import annotations
from PIL import Image, ImageDraw, ImageFont
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
import os
from typing import List

FONT_PATHS = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    "/System/Library/Fonts/Supplemental/Arial Unicode.ttf",
]

def _load_font(size: int):
    for p in FONT_PATHS:
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()

def draw_grid_png(grid: List[List[int]], out_path: str, title: str = "Sudoku") -> None:
    cell = 64
    border = 24
    size = border*2 + cell*9
    img = Image.new("RGB", (size, size + 80), "white")
    d = ImageDraw.Draw(img)

    font_title = _load_font(32)
    d.text((border, 10), title, font=font_title, fill="black")

    ox, oy = border, 60
    font_num = _load_font(28)
    for r in range(9):
        for c in range(9):
            x0 = ox + c*cell
            y0 = oy + r*cell
            x1 = x0 + cell
            y1 = y0 + cell
            d.rectangle([x0, y0, x1, y1], outline="black", width=1)
            v = grid[r][c]
            if v:
                bbox = d.textbbox((0, 0), str(v), font=font_num)
                w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
                d.text((x0 + (cell - w) / 2, y0 + (cell - h) / 2 - 4), str(v), font=font_num, fill="black")


    for k in range(10):
        w = 3 if k % 3 == 0 else 1
        x = ox + k*cell
        d.line([x, oy, x, oy + 9*cell], fill="black", width=w)
        y = oy + k*cell
        d.line([ox, y, ox + 9*cell, y], fill="black", width=w)

    img.save(out_path, format="PNG")

def make_daily_pdf(grids: List[List[List[int]]], out_path: str, title: str = "Daily Sudoku") -> None:
    c = canvas.Canvas(out_path, pagesize=A4)
    W, H = A4
    margin = 18*mm
    cell = 16*mm
    ox, oy = margin, H - margin - 9*cell

    for i, grid in enumerate(grids):
        c.setTitle(title)
        c.setFont("Helvetica-Bold", 18)
        c.drawString(margin, H - margin + 2*mm, f"{title} – {i+1}")

        c.setLineWidth(0.5)
        for r in range(10):
            y = oy + r*cell
            c.line(ox, y, ox + 9*cell, y)
        for col in range(10):
            x = ox + col*cell
            c.line(x, oy, x, oy + 9*cell)

        c.setLineWidth(2)
        for k in range(0, 10, 3):
            c.line(ox, oy + k*cell, ox + 9*cell, oy + k*cell)
            c.line(ox + k*cell, oy, ox + k*cell, oy + 9*cell)

        c.setFont("Helvetica", 14)
        for r in range(9):
            for col in range(9):
                v = grid[r][col]
                if v:
                    x = ox + col*cell + cell/2
                    y = oy + (8 - r)*cell + cell/2
                    c.drawCentredString(x, y - 3, str(v))

        c.showPage()
    c.save()
