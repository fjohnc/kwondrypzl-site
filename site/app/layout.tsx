import '../styles/globals.css'
import Link from 'next/link'

export const metadata = { title: 'KwondryPZL – Daily Sudoku', description: 'Play and print fresh Sudoku every day.' }

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (<html lang='en'><body><header className='border-b'><nav className='container flex items-center gap-6 h-16'><Link href='/' className='font-bold text-xl'>KwondryPZL</Link><Link href='/daily'>Daily Sudoku</Link><Link href='/downloads'>Downloads</Link><Link href='/about'>About</Link></nav></header><main className='container py-10'>{children}</main><footer className='container py-10 text-sm opacity-70'>© {new Date().getFullYear()} KwondryPZL • <a href='https://kwondry.etsy.com'>Etsy</a></footer></body></html>) }
