#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

import pyperclip

# Read clipboard contents
text = pyperclip.paste()

# Separate by line and add asterisks
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]

# Rejoin lines
text = '\n'.join(lines)

# Copy back to clipboard
pyperclip.copy(text)