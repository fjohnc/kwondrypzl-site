# KwondryPZL – Daily Sudoku MVP

## Quick start (local)
1) **Install tools**: Python 3.11+, Node.js LTS, Git, and VS Code.
2) **Generate today’s puzzles**:
```bash
python -m venv .venv && source .venv/bin/activate   # Windows PowerShell: py -3.11 -m venv .venv; .\\.venv\\Scripts\\Activate.ps1
pip install -r generator/requirements.txt
python generator/generate_daily.py   # creates content/sudoku/YYYY-MM-DD/*
```
3) **Run the site**:
```bash
cd site
npm install
npm run dev
# Open http://localhost:3000
```

## Deploy (Vercel or Netlify)
- Push this repo to GitHub.
- On Vercel, set the project to use the `site/` folder.
- Build command: `npm run build` (this also exports + copies content into `out/content`).

## Daily automation
GitHub Action `.github/workflows/daily.yml` generates and commits new puzzles at 05:00 London time (UTC cron shown).
