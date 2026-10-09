# Responsive dashboard styling

A token-driven, responsive dashboard stylesheet built with CSS custom properties, CSS Grid and Flexbox.

## Files
- `style.css` — all styling (design tokens, layout, theme variables)
- `index.html` — demo dashboard that uses it
- `screenshots/` — rendered at 320, 768, 1024 and 1440 px, in light and dark
- `shoot.py` — regenerates the screenshots and checks for horizontal overflow (`pip install playwright && playwright install chromium`)

## What's inside
- **Tokens** in `:root`: brand colors, fluid type scale (`clamp()`), spacing, radii, shadows, motion. Light and dark themes redefine the same variables; dark follows the system setting unless `data-theme` is set.
- **Grid**: 1 column (320) → 2 (768) → sidebar + 4 (1024) → sidebar + 12 (1440). Tracks use `minmax(0,1fr)` so content can't force overflow.
- **Flexbox**: nav, badges, list rows, the time-range control.
- **Look**: backdrop-filter glass cards, layered soft shadows, hover transitions (disabled for `prefers-reduced-motion`).

## Overflow check (document.scrollWidth vs clientWidth)
All 8 combinations (4 widths × 2 themes) pass: no horizontal scrollbar.

## Push to GitHub
```
git init && git add . && git commit -m "Responsive dashboard styling"
git branch -M main
git remote add origin https://github.com/<you>/<repo>.git
git push -u origin main
```
