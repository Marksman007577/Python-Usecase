#! python3

import pyperclip as pclip
import sys

passwords = {
    'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
    'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
    'luggage': '12345'
}

if len(sys.argv) < 2:
    print('Usage: python password locker - copy account password')
    sys.exit()

account = sys.argv[1]

if account in passwords:
    pclip.copy(passwords[account])
    print(f'Password for {account} copied to clipboard')
else:
    print(f'There is no account named {account}')
    