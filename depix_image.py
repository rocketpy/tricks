#  Official:  https://github.com/beurtschipper/Depix

#  Depix is a tool for recovering passwords from pixelized screenshots.
#  This implementation works on pixelized images that were created with a linear box filter.

#  Example
#  python depix.py -p images/testimages/testimage3_pixels.png -s images/searchimages/debruinseq_notepad_Windows10_closeAndSpaced.png -o output.png
#  Usage
"""
Cut out the pixelated blocks from the screenshot as a single rectangle.
Paste a De Bruijn sequence with expected characters in an editor with the same font settings (text size, font, color, hsl).
Make a screenshot of the sequence. If possible, use the same screenshot tool that was used to create the pixelized image.

Run python depix.py -p [pixelated rectangle image] -s [search sequence image] -o output.png
"""

