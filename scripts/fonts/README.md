# Custom Zodiac Symbol Fonts

This directory is for custom fonts containing monochrome zodiac glyphs to use in PDF generation.

## Why Custom Fonts?

WeasyPrint (our PDF generator) renders Unicode zodiac symbols (♈ ♉ ♊ etc.) as **colored emojis** that cannot be styled to black and white using CSS. Custom fonts with zodiac glyphs allow us to display actual symbols in monochrome.

## Font Requirements

Your custom font must meet these requirements:

1. **Contains zodiac glyphs** at Unicode positions U+2648 through U+2653:
   - U+2648: ♈ Aries
   - U+2649: ♉ Taurus
   - U+264A: ♊ Gemini
   - U+264B: ♋ Cancer
   - U+264C: ♌ Leo
   - U+264D: ♍ Virgo
   - U+264E: ♎ Libra
   - U+264F: ♏ Scorpio
   - U+2650: ♐ Sagittarius
   - U+2651: ♑ Capricorn
   - U+2652: ♒ Aquarius
   - U+2653: ♓ Pisces

2. **File format**: .ttf, .otf, .woff, or .woff2

3. **Glyphs are stylable**: Must render as actual glyphs (not embedded color images)

## Where to Find Suitable Fonts

### Option 1: Check Fonts Already On Your Mac

Many specialty fonts on your Mac may already have zodiac glyphs. To check:

1. Open **Font Book** (Applications > Font Book)
2. Search for fonts with keywords like:
   - "Astrological"
   - "Symbol"
   - "Dingbats"
   - "Icons"
3. Select a font and look at the character map
4. Check if it contains zodiac symbols at the Unicode positions listed above

### Option 2: Download Free Astrology Fonts

Some free fonts that contain zodiac symbols:

- **Astrology Symbols** - Search for "astrology symbols font free"
- **Astrological Symbol** fonts on font websites
- **Dingbat/Symbol fonts** that include zodiac glyphs

**Important**: Verify the font license allows PDF embedding before using commercially.

### Option 3: Purchase Professional Fonts

Professional symbol fonts from:
- Adobe Fonts (included with Creative Cloud)
- MyFonts.com
- FontShop.com

Search for "zodiac symbols" or "astrological symbols"

## How to Use Your Custom Font

### Step 1: Place Font File Here

Copy your font file to this directory:
```
scripts/fonts/YourFontName.ttf
```

### Step 2: Configure in base.css

Edit `scripts/css/base.css` and update the `@font-face` declaration:

```css
/* Uncomment and update these lines (around line 14) */
@font-face {
    font-family: 'ZodiacFont';
    src: url('file:///Users/darrenschaeffer/Documents/Claude/Astrogy_Claude/scripts/fonts/YourFontName.ttf');
    font-weight: normal;
    font-style: normal;
}
```

Then uncomment the font-family line in the `.zodiac-symbol` class (around line 123):
```css
.zodiac-symbol {
    /* ... other properties ... */
    /* Uncomment this line: */
    font-family: 'ZodiacFont', 'Helvetica', 'Arial', sans-serif;
}
```

### Step 3: Enable Custom Font Mode

Edit `scripts/pdf_generator.py` and change line 35:

```python
# Change this:
USE_CUSTOM_ZODIAC_FONT = False

# To this:
USE_CUSTOM_ZODIAC_FONT = True
```

### Step 4: Test

Regenerate a report to test:

```bash
python scripts/pdf_generator.py \
    profiles/Darren_S/output/transit_long_synthesis_Darren_S_2026-01-01_to_2034-12-31.md \
    --seed-data profiles/Darren_S/seed_data/master_seed_data.yaml \
    --report-type transit_long
```

Check the PDF - zodiac symbols should now appear as monochrome glyphs from your custom font.

## Testing Your Font

To verify your font contains the correct glyphs:

### Method 1: Font Book (Mac)

1. Open Font Book
2. Select your font
3. Go to Preview > Custom
4. Type or paste these Unicode characters: ♈ ♉ ♊ ♋ ♌ ♍ ♎ ♏ ♐ ♑ ♒ ♓
5. Verify they display as zodiac symbols (not empty boxes)

### Method 2: Character Viewer (Mac)

1. Open Character Viewer (Edit menu > Emoji & Symbols, or Control+Command+Space)
2. Search for "zodiac"
3. Check if glyphs appear in your selected font
4. Look for Unicode positions 2648-2653

### Method 3: Quick Test Script

Create a simple HTML file and open in browser:

```html
<!DOCTYPE html>
<html>
<head>
    <style>
        @font-face {
            font-family: 'TestFont';
            src: url('file:///path/to/your/font.ttf');
        }
        .test {
            font-family: 'TestFont';
            font-size: 48pt;
        }
    </style>
</head>
<body>
    <div class="test">♈ ♉ ♊ ♋ ♌ ♍ ♎ ♏ ♐ ♑ ♒ ♓</div>
</body>
</html>
```

## Troubleshooting

### Symbols Still Show as Colored Emojis

- Your font may not contain glyphs at the correct Unicode positions
- Try a different font or verify Unicode coverage

### Symbols Show as Empty Boxes or Question Marks

- Font file path in base.css may be incorrect
- Font may not be properly embedded
- Check WeasyPrint console output for font loading errors

### PDF Shows Text Abbreviations (CAP, LEO) Instead of Symbols

- `USE_CUSTOM_ZODIAC_FONT` is still set to `False` in pdf_generator.py
- Change it to `True` and regenerate

## Current Status

**Default Mode**: Text abbreviations (CAP, LEO, ARI, etc.)
- Reliable, no setup required
- Works immediately

**Custom Font Mode**: Unicode symbols (♈ ♉ ♊ etc.)
- Requires custom font setup
- Better visual appearance (actual symbols instead of text)
- Follow steps above to enable

## Font Recommendations

If you're looking for recommendations, these are good starting points:

1. **Check your Mac first** - You may already have suitable fonts installed
2. **Adobe Fonts** - If you have Creative Cloud, search their library
3. **Free options** - Search "astrology symbols font free download"

Always verify the license allows PDF embedding for your intended use (personal/commercial).
