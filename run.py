import requests
import time 
from random import randint

user_name = 'pikachu_killar'
password = 'pikachu101'



url = 'https://www.instagram.com/accounts/login/'
url_main = url + 'ajax/'
auth = {'username': user_name, 'password': password}
headers = {'referer': "https://www.instagram.com/accounts/login/",
           'cookie':'csrftoken=1',
           'x-csrftoken':'1',
           'Content-Type':'application/x-www-form-urlencoded'}

sess = requests.Session()
res=sess.post(url_main, data=auth, headers=headers)
cook=res.cookies.get_dict()
sess_id = cook['sessionid']


########### GET USER ID
uusr='deepanshuxpal'
res1= sess.get('https://www.instagram.com/'+uusr+'/?__a=1')
user_data=res1.json()

user_id = user_data['graphql']['user']['id']
###########


########### GET USER DETAIL
uu_id=user_id
url_det = 'https://i.instagram.com/api/v1/users/'+uu_id+'/info/'
header1={'host':'i.instagram.com',
        'Connection':'keep-alive',
        'Accept':'*/*',
        'X-IG-Capabilities':'3wo=',
        'Accept-Language':'en-US;q=1',
        'Accept-Encoding':'gzip, deflate',
        'User-Agent':'Instagram 9.5.1 (iPhone9,2; iOS 10_0_2; en_US; en-US; scale=2.61; 1080x1920) AppleWebKit/420+',
        'X-IG-Connection-Type':'WiFi',
        'Cookie':'sessionid='+sess_id }
res2=sess.get(url_det, headers=header1)
data_user_pp=res2.json()
bio_user = data_user_pp['user']['biography']
try:
    bio_user = data_user_pp['user']['public_email']
except:
    print("no email exist bro")
    
count = data_user_pp['user']['follower_count']

print(bio_user)

##############


    
########### FINAL SWIPE  
end_cursor=''
final_followers=[]
final_followers_det=[]
per_quer=[]

star_itch=''
flag=1
while flag==1:
    time.sleep(randint(0,3))
    followers_url = 'https://www.instagram.com/graphql/query/?query_hash=c76146de99bb02f6415203be841dd25a&variables={"id":"'+uu_id+'","include_reel":true,"fetch_mutual":false,"first":24,"after":"'+end_cursor+'"}'
    header2={'Cookie':'sessionid='+sess_id}
    res3=sess.get(followers_url, headers=header2)
    data_user_pp1=res3.json()
    followers = data_user_pp1['data']['user']['edge_followed_by']['edges']
    end_cursor = data_user_pp1['data']['user']['edge_followed_by']['page_info']['end_cursor']
    
    per_quer.append(len(followers))
    for follower in followers:
        final_followers_det.append(follower)
        final_followers.append(follower['node']['username'])
        if follower['node']['username'] == 'benyarts':
            star_itch=follower
    
    if end_cursor is None :
        flag=0


len(final_followers)
#################




























