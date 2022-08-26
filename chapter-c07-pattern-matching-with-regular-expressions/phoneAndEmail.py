#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses in the clipboard text

import pyperclip, re

# Phone regex
phoneRegex = re.compile(r'''
    (\d{3}|\(\d{3}\))?              # Area code
    (\s|-|\.)?                      # Separator
    (\d{3})                         # First three digits
    (\s|-|\.)?                      # Separator
    (\d{4})                         # Last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # Extension
    )''', re.VERBOSE)

# Email regex
emailRegex = re.compile(r'''
    [a-zA-Z0-9._%+-]+   # Local-part
    @                   # At
    [a-zA-Z0-9.-]+      # Domain
    \.                  # Dot
    [a-zA-Z\.]{2,5}     # Extension
    ''', re.VERBOSE)

# Import clipboard data
text = str(pyperclip.paste())

# Find all matches in the text
matches = []    # Store in tuple
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join(groups[1], groups[3], groups[5])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

# Neatly format the matched strings into a single string
# Paste back to the clipboard

# Message if no matches found