#!/usr/bin/python3
import requests, json, time

token = input(f" [+] Submit your token: ")
while not token:
    print(" [+] Enter a fucking token you prick: ")
headers = {
        'Authorization': token,
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0',
        'Content-Type': 'application/json'
}
r = "https://discordapp.com/api/"
data = requests.get(r + "v6/users/@me", headers=headers).json()

def check():
    print("\n Verifying the token is valid..")
    time.sleep(1)
    if not data:
        print(" [!] Token failed. Restart the script and try again.")
    else:
        print(" [+] Valid token, gathering information..")
check()

def acc_info():
    print(f"\n [-] User: {data['username']}#{data['discriminator']} - {data['id']}")
    if data['verified'] == True:
        print(f" [-] Email: {data['email']} (Verified)")
    else:
        print(f" [-] Email: {data['email']} (Not Verified)")
    print(f" [-] 2FA: {data['mfa_enabled']}")
    if data['phone'] == None:
        print(f" [-] Phone Number: N/A")
    else:
        print(f" [-] Phone Number: {data['phone']}")
acc_info()
