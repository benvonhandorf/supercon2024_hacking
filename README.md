## Description

This repo holds rough hacking for the Supercon 8 / 2024 badge, primarily focused on the petal SAO.

I wanted to use the Petal SAO as an alphanumeric display.

- `font_mapping.py` - Contains a set of positions for each LED on the badge and code to allow analysis of a font and will output the byte arrays of each character in a Python map.
  - Allows changing the font and font rotation for generated characters
  - Copy paste the output of this into `characters.py`
- `characters.py` - Contains the map of characters for a font and a helper `set_character( i2cbus, character )` method
  - This has 2 different character maps in it that are rotated 0 and 60 degrees for convenience.  Uncomment the one you want to use.