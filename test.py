import click
import requests, os, sys
from datetime import time
from googlesearch import search
from sys import exit
import datetime
from datetime import datetime
import random
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

import time
from time import sleep
from colorama import Fore
os.system('clear')
sl=1
while(True):
    now = datetime.now()
    cc1 = now.strftime("%H")
    cc2 = now.strftime("%M")
    cc3 = now.strftime("%S")
    tym =[" (y) "," ;) "," :/ "," :( "," :) "," :-D "," >.< " ," T_T "]
    icon =[" <3 "," <3 <3 "," <3 <3 <3 "]
    oh = random.choice(tym)
    ok = random.choice(icon)
    oh1 = random.choice(tym)
    oh2 = random.choice(tym)
    oh3 = random.choice(tym)
    oh4 = random.choice(tym)
    oh5 = random.choice(tym)
    cookie= "sb=6UQcYrNM-I42Ite2aOXLWAyF;datr=6UQcYuLw_KE9ToF7iWDn00F_;vpd=v1%3B692x360x2;locale=vi_VN;dpr=2;c_user=100085055015984;xs=2%3ApdYizTVRCLfN_g%3A2%3A1666717818%3A-1%3A6280;m_page_voice=100085055015984;fbl_cs=AhCiw6JTQe6%2BpOBXW1GMRdbMGFg3STkwZlBvdkhMSz00ZUVBd3BPcFg0Yw;fbl_ci=1230331037819178;fbl_st=100426293%3BT%3A27778634;fr=0nWZXbt2UT2YDrMVm.AWXf-YdzuLReO35NU8w9cvYb_BI.BiveFX.0Z.AAA.0.0.BjWBp0.AWXCKfZbEJo;wd=980x1884"
    linkfb="https://www.facebook.com/taonho.qua.351"
    
    tinnhan=f"[{cc1}:{cc2}:{cc3}] Bao Gio Anh Het Doi Em Em Dung [{sl}] {ok} {oh} {oh1} {oh2} {oh3} {oh4} {oh5}"
    sl=sl+1
    
    
    
    headfb={
       'Host':'mbasic.facebook.com',
       'upgrade-insecure-requests':'1',
       'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5057.107 Safari/537.36',
       'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
       'sec-fetch-site':'cross-site',
       'sec-fetch-mode':'navigate',
       'sec-fetch-user':'?1',
       'sec-fetch-dest':'document',
       'cookie':cookie,
      }
    headers={
       'Host':'mbasic.facebook.com',
       'content-length':'289',
       'cache-control':'max-age=0',
       'sec-ch-ua':'"Chromium";v="105", "Not)A;Brand";v="8"',
       'sec-ch-ua-mobile':'?1',
       'sec-ch-ua-platform':'"Android"',
       'upgrade-insecure-requests':'1',
       'user-agent':'Mozilla/5.0 (X11; U; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4990.82 Safari/537.36',
       'origin':'https://mbasic.facebook.com',
       'content-type':'application/x-www-form-urlencoded',
       'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
       'sec-fetch-site':'same-origin',
       'sec-fetch-mode':'navigate',
       'sec-fetch-user':'?1',
       'sec-fetch-dest':'document',
       'referer':'https://www.facebook.com',
       'cookie':cookie,
    }
    
    home=requests.get('https://mbasic.facebook.com',headers=headfb).text
    checkck=home.find('Đăng nhập hoặc đăng ký')
    if checkck==-1:
    	fb=requests.get('https://mbasic.facebook.com/profile.php',headers=headfb).text.split("Chỉnh sửa trang cá nhân")[0]
    	id_fb=fb.split("/composer/mbasic/?av=")[1].split("&")[0]
    	ten_fb=fb.split('title>')[1].split('<')[0]
    	id = "100058943230770"
     
    	a=requests.get(f"https://mbasic.facebook.com/messages/read/?fbid={id}",headers=headfb).text.split('/messages/read/?')[1].split('"')[0].replace('amp;','')
    	b=requests.get(f"https://mbasic.facebook.com/messages/read/?fbid={id}",headers=headfb).text.split("fb_dtsg")[1].split('value="')[1].split('"')[0]
    	c=requests.get(f"https://mbasic.facebook.com/messages/read/?fbid={id}",headers=headfb).text.split('fb_dtsg')[1].split('jazoes')[1].split('value="')[1].split('"')[0]
    	d=requests.get(f"https://mbasic.facebook.com/messages/read/?fbid={id}",headers=headfb).text.split('fb_dtsg')[1].split('tids')[1].split('value="')[1].split('"')[0]
    	e=requests.get(f"https://mbasic.facebook.com/messages/read/?fbid={id}",headers=headfb).text.split('fb_dtsg')[1].split('wwwupp')[1].split('value="')[1].split('"')[0]
    	f=requests.get(f"https://mbasic.facebook.com/messages/read/?fbid={id}",headers=headfb).text.split('fb_dtsg')[1].split('name="ids[')[1].split('"')[0]
    	g=requests.get(f"https://mbasic.facebook.com/messages/read/?fbid={id}",headers=headfb).text.split('fb_dtsg')[1].split('csid')[1].split('value="')[1].split('"')[0]
    	data=(f"fb_dtsg={b}&jazoest={c}&body={tinnhan}&send=G%E1%BB%ADi&tids={d}&wwwupp={e}&ids[{f}={id}&referrer=&ctype=&cver=legacy&csid={g}")
    	pp=requests.post(f"https://mbasic.facebook.com/messages/send/?{a}",data=data,headers=headers)
     
    	 
    		
    		
    	 
     
