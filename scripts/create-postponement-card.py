"""Render a new text-only notice card; no existing raster images are edited."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
root = Path(__file__).resolve().parents[1]
image = Image.new('RGB', (1080, 1080), '#211d19')
draw = ImageDraw.Draw(image)
font_dir = Path('/System/Library/Fonts/Supplemental')
def label(text, y, size, color, bold=True):
    font = ImageFont.truetype(str(font_dir / ('Arial Bold.ttf' if bold else 'Arial.ttf')), size)
    draw.text((80, y), text, font=font, fill=color)
draw.rectangle((80, 82, 180, 94), fill='#fa713b')
label('CHEBANOV', 145, 110, '#fff7e9')
label('НОВОКУЗНЕЦК', 290, 48, '#fa713b')
draw.line((80, 395, 1000, 395), fill='#63574c', width=2)
label('Концерт', 470, 108, '#fff7e9')
label('переносится', 600, 108, '#fff7e9')
label('Новая дата будет', 770, 40, '#c7b7a6', False)
label('объявлена дополнительно', 825, 40, '#c7b7a6', False)
label('chebanovnoz.ru', 960, 35, '#c7b7a6', False)
image.save(root / 'assets/novokuznetsk-postponed-20261008.png', optimize=True)
