#! python3
# pw.py - An (insecure) password locker programme.

PASSWORDS = {'email': 'myemailpword',
             'blog': 'myblogpword',
             'luggage': '1234'}

import sys, pyperclip
# sys.argv list must contain both programme filename and first command line arg (account name)
if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]   # first command line arg is the account name

# Check if account name exists in PASSWORDS
if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('No account named ' + account)
