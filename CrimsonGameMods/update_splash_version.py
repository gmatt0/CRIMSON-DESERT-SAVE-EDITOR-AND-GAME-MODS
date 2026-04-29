"""Update splash.png version text from updater.py. Run before building."""
import re
from PIL import Image, ImageDraw, ImageFont

with open('updater.py') as f:
    m = re.search(r'APP_VERSION\s*=\s*["\']([^"\']+)', f.read())
ver = m.group(1) if m else '?'

img = Image.open('splash.png')
draw = ImageDraw.Draw(img)
bg = img.getpixel((400, 180))
draw.rectangle([8, 155, 150, 195], fill=bg)
try:
    font = ImageFont.truetype('arial.ttf', 20)
except Exception:
    font = ImageFont.load_default()
draw.text((12, 162), f'v{ver}', fill=(255, 68, 102), font=font)
img.save('splash.png')
print(f'splash.png updated to v{ver}')
