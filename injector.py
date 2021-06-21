from modules.GMethod import Get
from modules.PMethod import Post

print(r"""
  _____________________________________________
 |            _____________________            |
 |           |            _ _ _    |           |
 |           |  ___  __ _| (_) |_  |           |
 |           | / __|/ _` | | | __| |           |
 |           | \__ \ (_| | | | |_  |           |
 |           | |___/\__, |_|_|\__| |           |
 |           |         |_|  v1.0   |           |
 |           |                     |           |
 |           | [ Coded By Andi.D ] |           |
 |           |_____________________|           |
 |_____________________________________________|
""")

print('[ Options ]'.center(50, '='), end='\n\n')

target = input('Target : ')
vulnParam = input('\nVuln Parameter : ')
method = input('\nMethod : ')

if method.lower() == 'post':
    keys = []
    while '\s' not in keys:
        keys.append(
            input('\nKeys [# without vuln parameter, stop by typing \s] : '))
    keys.remove('\s')
    trucon = input('\nTrue Condition [# uniq text] : ')

print()

print('[ Injecting ]'.center(50, '='), end='\n\n')

if method.lower() == 'post':
    # Post Method
    Post(
        target,
        vulnParam,
        keys,
        trucon,
        headers={
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
            'Referer': 'www.google.com',
        }
    ).execute()
    # Post Method
elif method.lower() == 'get':
    # Get Method
    Get(
        target,
        vulnParam,
        headers={
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
            'Referer': 'www.google.com',
        }
    ).execute()
    # Get Method
else:
    print('only get/post method\n')
