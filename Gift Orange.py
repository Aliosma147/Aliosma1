# Orange Wheel

# Aliosma

import requests,json,random,string,termcolor,time,pyfiglet,sys
#----------------------------
from hashlib import sha256
print("\033[1;35m Welcome to script orange gift by Aliosma")

print("\x1b[1;31m="*50)

logo = pyfiglet.figlet_format("Aliosma")
lago = pyfiglet.figlet_format("Gifts")
descr = """
 \x1b[0;33mBy: Aliosma
 
 """
print(termcolor.colored(logo, color="green"), termcolor.colored(lago, color="green"),termcolor.colored(descr, color="red"))

print("\x1b[1;31m="*50)
num=input('\x1b[1;35m Enter a Number :  ')
pas=input('\x1b[1;35m Enter a Password :  ')
print()

import hashlib
url2 = "https://services.orange.eg/GetToken.svc/GenerateToken"
hd2 = {"Content-type":"application/json", 
  "Content-Length":"78", 
  "Host":"services.orange.eg"
   , "Connection":"Keep-Alive" ,
    "User-Agent":"okhttp/3.12.1"}
data2 = '{"appVersion":"2.9.8","channel":{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"},"dialNumber":"%s","isAndroid":true,"password":"%s"}' %(num,pas)
ctv = requests.post(url2,headers=hd2,data = data2).json()["GenerateTokenResult"]["Token"]
a=ctv+',{.c][o^uecnlkijh*.iomv:QzCFRcd;drof/zx}w;ls.e85T^#ASwa?=(lk'
htv=(sha256(a.encode('utf-8')).hexdigest().upper())

ur1 = 'https://services.orange.eg/SignIn.svc/SignInUser' 

headers ={ 
'IsAndroid': 'true',
'_ctv': ctv,
'_htv': htv,
'OsVersion': '9',
'AppVersion': '6.4.0',
'Content-type': 'application/json',
'Accept': 'application/json',
'User-Agent': 'okhttp/3.14.9',
'Host': 'services.orange.eg'
}

data1 = '{"appVersion":"6.4.0","channel":{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"},"dialNumber":"%s","isAndroid":true,"password":"%s"}'  % (num,pas)

req=requests.post(ur1,headers=headers,data=data1).json()

longe = str(req["SignInUserResult"]["ErrorDescription"])
print("\x1b[1;32m")
print('    ' + longe)
print("\x1b[1;31m")
if longe == 'invalid number or password ...' :
	sys.exit()
urlo = "https://services.orange.eg/GetToken.svc/GenerateToken"
hdo = {"Content-type":"application/json", 
  "Content-Length":"78", 
  "Host":"services.orange.eg"
   , "Connection":"Keep-Alive" ,
    "User-Agent":"okhttp/3.12.1"}
datao = '{"appVersion":"2.9.8","channel":{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"},"dialNumber":"%s","isAndroid":true,"password":"%s"}' %(num,pas)
ctv = requests.post(urlo,headers=hdo,data = datao).json()["GenerateTokenResult"]["Token"]
key = ',{.c][o^uecnlkijh*.iomv:QzCFRcd;drof/zx}w;ls.e85T^#ASwa?=(lk'
htv=(str(hashlib.sha256((ctv+key).encode('utf-8')).hexdigest()).upper())
url3 ="https://services.orange.eg/APIs/Gaming/api/WheelOfFortune/Spin"

data3 ='{"ChannelName":"MobinilAndMe","ChannelPassword":"ig3yh*mk5l42@oj7QAR8yF","Dial":"%s","Language":"ar","Password":"%s","ServiceClassId":"831"}' %(num,pas)

header3 ={
"_ctv": ctv,
"_htv": htv,
"isEasyLogin": "false",
"net-msg-id": "a53a6ccd021379dq17106206219231068",
"x-microservice-name": "APMS",
"Content-Type": "application/json; charset=UTF-8",
"Content-Length": "157",
"Host": "services.orange.eg",
"Connection": "Keep-Alive",
"Accept-Encoding": "gzip",
"User-Agent": "okhttp/3.14.9",
}

reqe=requests.post(url3,headers=header3,data=data3).json()
jj=reqe["OfferDetails"]["OfferId"]
jjj=reqe["SecondryButtonDetails"]["CategoryId"]
des=reqe["OfferDetails"]["OfferDescription"]


print(des)

urlo2 = "https://services.orange.eg/GetToken.svc/GenerateToken"
hdo2 = {"Content-type":"application/json", 
  "Content-Length":"78", 
  "Host":"services.orange.eg"
   , "Connection":"Keep-Alive" ,
    "User-Agent":"okhttp/3.12.1"}
datao2 = '{"appVersion":"2.9.8","channel":{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"},"dialNumber":"%s","isAndroid":true,"password":"%s"}' %(num,pas)
ctv2 = requests.post(urlo2,headers=hdo2,data = datao2).json()["GenerateTokenResult"]["Token"]
key2 = ',{.c][o^uecnlkijh*.iomv:QzCFRcd;drof/zx}w;ls.e85T^#ASwa?=(lk'
htv2=(str(hashlib.sha256((ctv2+key2).encode('utf-8')).hexdigest()).upper())

url4="https://services.orange.eg/APIs/Gaming/api/WheelOfFortune/Fulfill"

data4='{"CategoryId":"%s","ChannelName":"MobinilAndMe","ChannelPassword":"ig3yh*mk5l42@oj7QAR8yF","Dial":"%s","Language":"ar","OfferId":"%s","Password":"%s","ServiceClassId":"831"}' %(jjj,num,jj,pas)

header4={
"_ctv": ctv2,
"_htv": htv2,
"isEasyLogin": "false",
"net-msg-id": "a53a6ccd021379d17106206400481072",
"x-microservice-name": "APMS",
"Content-Type": "application/json; charset=UTF-8",
"Content-Length": "190",
"Host": "services.orange.eg",
"Connection": "Keep-Alive",
"Accept-Encoding": "gzip",
"User-Agent": "okhttp/3.14.9",
}

r4=requests.post(url4,headers=header4,data=data4).json()

print('\x1b[1;32m')
#print(r2)
drah=r4["ErrorDescription"]
print(drah)

# By Ali