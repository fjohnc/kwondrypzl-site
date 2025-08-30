from __future__ import annotations
import json, datetime
from pathlib import Path
from sudoku_engine import generate
from renderers import draw_grid_png, make_daily_pdf

ROOT = Path(__file__).resolve().parents[1]
OUT_ROOT = ROOT / "content" / "sudoku"
DIFS = ["easy", "medium", "hard"]

def main():
    today = datetime.date.today().isoformat()
    out_dir = OUT_ROOT / today
    out_dir.mkdir(parents=True, exist_ok=True)

    grids = []
    for d in DIFS:
        data = generate(d)
        (out_dir / f"{d}.json").write_text(json.dumps({
            "id": f"{today}-{d}",
            "difficulty": d,
            "grid": data["grid"],
            "solution": data["solution"],
        }, ensure_ascii=False), encoding="utf-8")
        draw_grid_png(data["grid"], str(out_dir / f"{d}.png"), title=f"{today} – {d.title()}")
        grids.append(data["grid"])

    make_daily_pdf(grids, str(out_dir / "daily.pdf"), title=f"Sudoku – {today}")
    (OUT_ROOT / "latest.txt").write_text(today, encoding="utf-8")
    print(f"Generated daily puzzles for {today} → {out_dir}")

if __name__ == "__main__":
    main()
