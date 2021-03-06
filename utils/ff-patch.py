#!/usr/bin/env python
# -*- coding: utf-8 -*-
import fontforge
import getopt
import re
import sys


# Set UTF-8 encoding
reload(sys)
sys.setdefaultencoding("utf8")


take        = ""
into        = ""
save_to     = ""
glyphs_file = ""
font_name   = ""

# Fetch command-line arguments
try:
	options, args = getopt.getopt(sys.argv[1:], "f:i:s:g:n:", ["from=", "into=", "save-to=", "glyphs-file=", "font-name="])
except getopt.GetoptError:
	usage()
	sys.exit(1)


# Parse their contents
for key, value in options:
	if   key in ("-f", "--from"):         take        = value
	elif key in ("-i", "--into"):         into        = value
	elif key in ("-s", "--save-to"):      save_to     = value
	elif key in ("-g", "--glyphs-file"):  glyphs_file = value
	elif key in ("-n", "--font-name"):    font_name   = value



# List of glyphs to extract from target file
glyphs = open(glyphs_file, "r").read()
glyphs = unicode(re.sub(ur"\s+", "", glyphs), "utf-8")


# Load both fonts in FontForge
take   = fontforge.open(take)
into   = fontforge.open(into)

# Copy each grapheme individually
for g in glyphs:
	take.selection.select(("unicode",), ord(g))
	take.copy()
	into.selection.select(("unicode",), ord(g))
	into.paste()

into.fontname = into.fondname = into.familyname  = into.fullname = font_name
into.generate(save_to)
