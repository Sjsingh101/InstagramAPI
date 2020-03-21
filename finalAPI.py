import requests
import time 
from random import randint
import re


user_name = ''
password = ''


################### PROXY DICT



IP = '159.65.69.157'
PORT = '8118'
HTTP_PROXY = 'http://'+IP+':'+PORT  
HTTPS_PROXY = 'https://'+IP+':'+PORT  
proxies = dict(http=HTTP_PROXY, https=HTTPS_PROXY)


###################


################### SAVE DATA

myData = [["UserName", "FullName", "Verified","Business","Email","BusinessEmail","PhoneNumber"]]

################## LOGIN

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

##################

########### GET USER ID
uusr='deepanshuxpal'
res1= sess.get('https://www.instagram.com/'+uusr+'/?__a=1')
user_data=res1.json()

user_id = user_data['graphql']['user']['id']
###########

#################### FIND EMAIL FROM BIO


def getEmails(str):
    regex = r'([\w0-9._-]+@[\w0-9._-]+\.[\w0-9_-]+)'
    elist = re.findall(regex, str, re.M|re.I)
    if elist:
        return elist[0]
    return ''



##################


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


user_ibemail = getEmails(bio_user) 
user_iuname = data_user_pp['user']['username']
user_ifname = data_user_pp['user']['full_name']

user_iverify = data_user_pp['user']['username']
user_ibusiness = data_user_pp['user']['full_name']

try:
    user_iemail = data_user_pp['user']['public_email']
except:
    user_iemail=''

try:
    user_ipno = data_user_pp['user']['public_phone_number']
except:
    user_ipno='' 
    
try:
    user_icat = data_user_pp['user']['category']
except:
    user_icat='' 
#count = data_user_pp['user']['follower_count']

myData.append(user_iuname,user_ifname,user_iverify,user_ibusiness,user_ibemail,user_iemail,user_ipno)

##############


    
########### FINAL SWIPE  
end_cursor=''
star_itch=''
flag=1
count=0
while flag==1:
    count+=1
    followers_url = 'https://www.instagram.com/graphql/query/?query_hash=c76146de99bb02f6415203be841dd25a&variables={"id":"'+uu_id+'","include_reel":true,"fetch_mutual":false,"first":200,"after":"'+end_cursor+'"}'
    header2={'Cookie':'sessionid='+sess_id}
    res3=sess.get(followers_url, headers=header2)
    data_user_pp1=res3.json()
    followers = data_user_pp1['data']['user']['edge_followed_by']['edges']
    end_cursor = data_user_pp1['data']['user']['edge_followed_by']['page_info']['end_cursor']
    
    for follower in followers:
        time.sleep(3)
        url_det = 'https://i.instagram.com/api/v1/users/'+follower['node']['id']+'/info/'
        res2=sess.get(url_det, headers=header1)
        data_user_pp2=res2.json()
        try:
            bio_user = data_user_pp2['user']['biography']
        except:
            bio_user=''

        user_ibemail = getEmails(bio_user) 
        user_iuname = data_user_pp2['user']['username']
        user_ifname = data_user_pp2['user']['full_name']

        user_iverify = data_user_pp2['user']['is_verified']
        user_ibusiness = data_user_pp2['user']['is_business']

        try:
            user_iemail = data_user_pp2['user']['public_email']
        except:
            user_iemail=''

        try:
            user_ipno = data_user_pp2['user']['public_phone_number']
        except:
            user_ipno='' 
    
        try:
            user_icat = data_user_pp2['user']['category']
        except:
            user_icat='' 
#count = data_user_pp['user']['follower_count']

        myData.append([user_iuname,user_ifname,user_iverify,user_ibusiness,user_ibemail,user_iemail,user_ipno])

  
        
    if end_cursor is None or count>=30000 :
        flag=0



#################


################# CSV SAVED

out = open('out.csv', 'w')
for row in myData:
    for column in row:
        out.write('%s;' % column)
    out.write('\n')
out.close()

#################





















