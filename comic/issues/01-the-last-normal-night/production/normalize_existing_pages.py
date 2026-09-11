from pathlib import Path
from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parents[4]
PAGES = ROOT / 'comic/issues/01-the-last-normal-night/pages'
TARGET = (2063, 3150)

for n in range(9, 19):
    path = PAGES / f'p{n:02d}.png'
    if not path.exists():
        raise SystemExit(f'missing required page: {path}')
    with Image.open(path) as src:
        src = src.convert('RGB')
        if src.size == TARGET:
            print(f'{path.name}: already {TARGET[0]}x{TARGET[1]}')
            continue
        old = src.size
        # Existing generated pages are very close to the canonical aspect ratio.
        # Fit to the print master canvas with a centered crop rather than stretch.
        out = ImageOps.fit(src, TARGET, method=Image.Resampling.LANCZOS, centering=(0.5, 0.5))
        out.save(path, optimize=True)
        print(f'{path.name}: normalized {old[0]}x{old[1]} -> {TARGET[0]}x{TARGET[1]}')
