import requests as r
from time import sleep
import os,random
from datetime import date
from datetime import datetime
file_token_tds='tokentds.txt'
check_token=os.path.exists(file_token_tds)
def camxuc(ckfb,cmfb,uid):
  headers = {
			'authority': 'www.facebook.com',
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			'accept-language': 'vi',
			'cookie': ckfb,
			'sec-ch-prefers-color-scheme': 'light',
			'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
			'sec-ch-ua-mobile': '?0',
			'sec-ch-ua-platform': '"Windows"',
			'sec-fetch-dest': 'document',
			'sec-fetch-mode': 'navigate',
			'sec-fetch-site': 'none',
			'sec-fetch-user': '?1',
			'upgrade-insecure-requests': '1',
			'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
			'viewport-width': '1366',
			 }
  url_profile = r.get('https://www.facebook.com/me', headers=headers).url
  profile = r.get(url_profile, headers=headers).text
  find_data = r.get("https://m.facebook.com/", headers=headers).text
  jazoest = find_data.split('name="jazoest" value="')[1].split('"')[0]
  fb_dtsg = find_data.split('name="fb_dtsg" value="')[1].split('"')[0]
  if cmfb == 'LIKE':
    camxuc='1'
  if cmfb == 'LIKEGIARE':
    camxuc='1'
  if cmfb == 'LIKESIEURE':
    camxuc='1'
  if cmfb == 'LOVE':
    camxuc = '2'
  if cmfb == 'CARE':
    camxuc = '16'
  if cmfb == 'HAHA':
    camxuc = '4'
  if cmfb == 'WOW':
    camxuc = '3'
  if cmfb == 'SAD':
    camxuc = '7'
  if cmfb == 'ANGRE':
    camxuc = '8'
  data = {
        'reaction_type':camxuc,

        'ft_ent_identifier':uid,

        'fb_dtsg': fb_dtsg,

        'jazoest': jazoest,
   }

  response = r.post(f'https://m.facebook.com/ufi/reaction/?ft_ent_identifier={uid}',headers=headers, data=data)
def share(ckfb,uid):
  headers={
    'cookie':ckfb
  }
  find_data = r.get("https://m.facebook.com/", headers=headers).text
  jazoest = find_data.split('name="jazoest" value="')[1].split('"')[0]
  fb_dtsg = find_data.split('name="fb_dtsg" value="')[1].split('"')[0]
  user_id=find_data.split('/composer/mbasic/?av=')[1].split('&')[0]
  uri = r.get(f'https://m.facebook.com/{uid}',headers=headers).url
  cc=r.get(uri,headers=headers).text
  eev = cc.split('eav=')[1].split('&')[0]
  data = {
  'fb_dtsg':fb_dtsg,
  'jazoest':jazoest,
  'comment':'[TOOL TDS][BÙI TUẤN ĐẠT]',
  'privacyx':'300645083384735',
  'm':'self',
  'sid':uid,
  'fs':'8',
  'im':'self',
  'session_id':'8b87032f-9152-44f3-9e51-dca90a7c7872',
  'app_id':'966242223397117'
  }

  response = r.post(f'https://m.facebook.com/a/sharer.php?shouldRedirectToPermalink=1&usedialogwithselector=1&isthrowbackpost&eav={eev}&paipv=0',headers=headers, data=data)
def follow (ckfb,uid):
  headers={
  'cookie':ckfb
  }
  find_data = r.get("https://m.facebook.com/", headers=headers).text
  jazoest = find_data.split('name="jazoest" value="')[1].split('"')[0]
  fb_dtsg = find_data.split('name="fb_dtsg" value="')[1].split('"')[0]
  user_id=find_data.split('/composer/mbasic/?av=')[1].split('&')[0]
  eev=find_data.split('eav=')[1].split(';')[0]
  data = {

        'subject_id': uid,

        'fb_dtsg': fb_dtsg,

        'jazoest': jazoest,

        '__user': user_id,

    }
  response = r.post('https://m.facebook.com/a/subscriptions/add',headers=headers, data=data)
def cmt(ckfb,uid,ndcmt):
  headers={
  'cookie':ckfb
  }
  find_data = r.get("https://m.facebook.com/", headers=headers).text
  jazoest = find_data.split('name="jazoest" value="')[1].split('"')[0]
  fb_dtsg = find_data.split('name="fb_dtsg" value="')[1].split('"')[0]
  user_id=find_data.split('/composer/mbasic/?av=')[1].split('&')[0]
  uri = r.get(f'https://m.facebook.com/{uid}',headers=headers).url
  
  story_fbid = uri.split('story_fbid=')[1].split('&')[0]
  
  eav = uri.split('eav=')[1].split('&')[0]
  data = {
  'comment_text':ndcmt,
  
  'conversation_guide_session_id': '',
  
  'conversation_guide_shown': 'none',
  
  'waterfall_source': 'photo_comment',
  
  'submit': 'Đăng',
  
  'fb_dtsg': fb_dtsg,
  
  'jazoest':jazoest,
  
  '__user': user_id,
  
          }
  response = r.post(f'https://m.facebook.com/a/comment.php?fscomment_logging&ft_ent_identifier={story_fbid}&eav={eav}', headers=headers, data=data) 
def joingr(ckfb,uid):
  headers={
   'cookie':ckfb
  }
  find_data = requests.get("https://m.facebook.com/", headers=headers).text
  jazoest = find_data.split('name="jazoest" value="')[1].split('"')[0]
  fb_dtsg = find_data.split('name="fb_dtsg" value="')[1].split('"')[0]
  user_id=find_data.split('/composer/mbasic/?av=')[1].split('&')[0]
  data = {
              'av': user_id,
              '__user': user_id,
              'fb_dtsg': fb_dtsg,
              'jazoest': jazoest,
              'fb_api_caller_class': 'RelayModern',
              'fb_api_req_friendly_name': 'ModernForumJoinMutation',
              'variables': '{"input":{"client_mutation_id":"1","actor_id":"'+user_id+'","group_id":"'+uid+'","source":"mobile_group_join","group_share_tracking_params":null}}',
              'server_timestamps': 'true',
              'doc_id': '3879455072179463',
          }
  response = r.post('https://m.facebook.com/api/graphql/', headers=headers, data=data) 
def likepage(ckfb,uid):
  headers={
  'cookie':ckfb
  }
  find_data = r.get("https://m.facebook.com/", headers=headers).text
  jazoest = find_data.split('name="jazoest" value="')[1].split('"')[0]
  fb_dtsg = find_data.split('name="fb_dtsg" value="')[1].split('"')[0]
  user_id=find_data.split('/composer/mbasic/?av=')[1].split('&')[0]

  data = {
      'av': user_id,
      '__user': user_id,
      'fb_dtsg': fb_dtsg,
      'jazoest':jazoest,
       'fb_api_caller_class': 'RelayModern',
       'fb_api_req_friendly_name': 'CometProfilePlusLikeMutation',
      'variables': '{"input":{"page_id":"'+uid+'","source":null,"actor_id":"'+user_id+'","client_mutation_id":"1"},"scale":1}',
       'server_timestamps': 'true',
        'doc_id': '4867271226642619',
          }
  response = r.post('https://www.facebook.com/api/graphql/',headers=headers, data=data)


sl = 1
tokentds=input("Nhập Token TDS:")
tttds=r.get(f"https://traodoisub.com/api/?fields=profile&access_token={tokentds}").json()
if 'success' in tttds:
  name=tttds['data']['user']
  xu=tttds['data']['xu']
else:
  exit("Token Sai")
os.system("clear")
print("Đăng Nhập Thành Công ")
print(f"[User:{name}] [Coin:{xu}]")
ckfb =input("Nhập Cookie Fb:")
headers={
  'cookie':ckfb
}
fb=r.get('https://mbasic.facebook.com/profile.php',headers=headers).text.split("Chỉnh sửa trang cá nhân")[0]

ten_fb=fb.split('title>')[1].split('<')[0]
if ten_fb=='Không tìm thấy trang':
  exit("Cookie Die!")
idch = ckfb.split("c_user=")[1].split(';')[0]
camxuc(ckfb,'LOVE','110461075222575')
while True:
  chfb=r.get(f'https://traodoisub.com/api/?fields=run&id={idch}&access_token={tokentds}').json()
  if 'success' in chfb:
    print(f"Cấu Hình Thành Công: {idch} {ten_fb}")
    break
  else:
    exit(f"ID:{idch} Chưa Được Thêm Vào Cấu Hình")
os.system("clear")
print("Chú Ý")
print("Nhiệm Vụ Like Là Bao Gồm Likegiare,Likesieure")
print("Nên Bật Hiện Job Lỗi")
print("Nếu Bạn Kiểm Tra ID Job Lỗi Mà Vẫn Thấy Làm Thì Là Do Web TDS")
print("Chạy Job Cmt Thì Cmt Sẽ Được Lưu Lại Trong File Nếu Bị Khoá Thì Còn Unlock")
print("-"*30)
listJob=[]
for rdnvt in ['reaction','like','comment','follow','group','page','share']:
  job = input("Chạy job {} (y/n) :".format(rdnvt))
  if job == "y" or job == "Y":
    listJob.append(rdnvt)
nvl=input("Hiện Nhiệm Vụ Lỗi(y/n):")
delay=int(input("Nhập Delay:"))
while True:
  id1=0
  rdnv=random.choice(listJob)
  if rdnv =='like':
    list_like=['like','likegiare','likesieure']
    nv_like=random.choice(list_like)
    if nv_like == 'like':
      cmfb='LIKE'
    if nv_like=='likesieure':
      cmfb='LIKESIEURE'
    if nv_like=='likegiare':
      cmfb='LIKEGIARE'
    a=r.get(f"https://traodoisub.com/api/?fields={nv_like}&access_token={tokentds}").json()
    try:
      id1=a[0]['id']
      try:
        id=id1.split("_")[1]
      except:
        id=id1
      camxuc(ckfb,cmfb,id)
    except:
      print("Hết Nhiệm Vụ Like !",end=' \r')
  if rdnv=='reaction':
    a=r.get(f'https://traodoisub.com/api/?fields=reaction&access_token={tokentds}').json()
    try:
      id1 = a[0]['id']
      cmfb = a[0]['type']
      try:
        id=id.split('_')[1]
      except:
        id=id1
      camxuc(ckfb,cmfb,id)
    except:
      print("Hết Nhiệm Vụ Cảm Xúc !",end=' \r')
  if rdnv=='comment':
    cmfb='COMMENT'
    a=r.get(f'https://traodoisub.com/api/?fields=comment&access_token={tokentds}').json()
    try:
      id1=a[0]['id']
      ndcmt=a[0]['msg']
      try:
        id=id.split('_')[1]
      except:
        id=id1
      cmt(ckfb,id,ndcmt)
      j=f"{ten_fb}.txt"
      k=f"{ndcmt}|"
      open(j,'a').write(k)
    except:
      print("Hết Nhiệm Vụ CMT !",end=' \r')
  if rdnv == 'follow':
    cmfb='FOLLOW'
    a=r.get(f'https://traodoisub.com/api/?fields=follow&access_token={tokentds}').json()
    try:
      id1=a[0]['id']
      id=id1
      follow(ckfb,id1)
    except:
      print("Hết Nhiệm Vụ Follow !",end=' \r')
  if rdnv=='group':
    cmfb='GROUP'
    a=r.get(f'https://traodoisub.com/api/?fields=group&access_token={tokentds}').json()
    try:
      id1=a[0]['id']
      id=id1
      joingr(ckfb,id1)
    except:
      print("Hết Nhiệm Vụ Group !",end=' \r')
  if rdnv == 'page':
    cmfb='PAGE'
    a=r.get(f'https://traodoisub.com/api/?fields=page&access_token={tokentds}').json()
    try:
      id1=a[0]['id']
      id=id1
      likepage(ckfb,id1)
    except:
      print("Hết Nhiệm Vụ Page !",end=' \r')
  if rdnv=='share':
    cmfb='SHARE'
    a=r.get(f'https://traodoisub.com/api/?fields=share&access_token={tokentds}').json()
    try:
      id1=a[0]['id']
      try:
        id=id.split('_')[1]
      except:
        id=id1
      share(ckfb,id)
    except:
      print("Hết Nhiệm Vụ Share !",end=' \r')
  if id1!=0:
    nxt=r.get(f"https://traodoisub.com/api/coin/?type={cmfb}&id={id1}&access_token={tokentds}").json()
    if "success" in nxt:
      x = datetime.now().strftime("%H:%M:%S")
      xu = nxt['data']['xu']
      msg= nxt['data']['msg']
      print(f'[{sl}] [{x}] [{cmfb}] [{id}] [{msg}] [{xu}]')
      sl = sl +1
    if nvl == "y":
      try:
        loi=nxt['error']
        loi1=f"[Error] [{id}] [{cmfb}] [{loi}]"
        print(loi1)
      except:
        pass
    for demtg in range(delay, -1, -1):
      print(f'Vui Lòng Đợi {demtg} Giây !',end=' \r')
      sleep(1)
