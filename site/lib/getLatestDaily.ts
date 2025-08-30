import fs from 'fs';
import path from 'path';

// Use the public folder in production so Vercel can serve the files.
export function getContentRoot() {
  // process.cwd() at runtime is the project root (the "site" folder).
  return path.join(process.cwd(), 'public', 'content', 'sudoku');
}

export function getLatestDate() {
  const r = getContentRoot();
  if (!fs.existsSync(r)) return null;
  const d = fs.readdirSync(r).filter(x => /\d{4}-\d{2}-\d{2}/.test(x));
  if (!d.length) return null;
  return d.sort().pop() || null;
}

export function readDaily(date: string) {
  const dir = path.join(getContentRoot(), date);
  const RJ = (n: string) => JSON.parse(fs.readFileSync(path.join(dir, n), 'utf-8'));
  const has = (n: string) => fs.existsSync(path.join(dir, n));
  return {
    date,
    easy: has('easy.json') ? RJ('easy.json') : null,
    medium: has('medium.json') ? RJ('medium.json') : null,
    hard: has('hard.json') ? RJ('hard.json') : null,
    pdf: has('daily.pdf') ? path.posix.join('/content/sudoku', date, 'daily.pdf') : null,
    pngs: {
      easy: has('easy.png') ? path.posix.join('/content/sudoku', date, 'easy.png') : null,
      medium: has('medium.png') ? path.posix.join('/content/sudoku', date, 'medium.png') : null,
      hard: has('hard.png') ? path.posix.join('/content/sudoku', date, 'hard.png') : null,
    },
  };
}
