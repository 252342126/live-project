import requests
import json

url2 = 'http://api.map.baidu.com/place/v2/search?query= 商圈&scope=2&location=26.0887007395,119.3032476646&sort_name=overall_rating&radius=20000&page_size=100&output=json&ak=SoNxyq6RlxwK6rrnVOPtcesi4W2pfMQ1&page_num='


def init():
    global url2
    lists = []
    for j in range(10):
        url = url2 + str(j)
        r = requests.get(url)
        t = r.text
        dict = json.loads(t)
        for i in dict:
            if i == 'results':
                s = dict[i]
                lists.append(s)
    return lists
location=[]
name=[]
t = init()
for i in t:
    for j in i:
        location.append(j["location"])
        name.append(j['name'])
print(name)
jujidi=""

# url3 = "http://api.map.baidu.com/place/v2/search?query= 美食$餐饮&scope=2&location={0},{1}&sort_name=overall_rating&radius=20000&page_size=100&output=json&ak=dntnIGs3ueWbi8TGkGYz0l8j1p6c9Yc1&page_num=".format(p1,p2)
max=-1
listss=[]
post1=0
post2=0
id=-1
ssss=0
for loc in location:
    p1=loc["lat"]
    p2=loc["lng"]
    url3 = "http://api.map.baidu.com/place/v2/search?query= 美食$餐饮&scope=2&location={0},{1}&sort_name=overall_rating&radius=100&page_size=100&output=json&ak=SoNxyq6RlxwK6rrnVOPtcesi4W2pfMQ1&page_num=".format(p1, p2)
    pos1=""
    pos2=""
    lists = []
    cnt=0
    for j in range(10):
        url = url3 + str(j)
        r = requests.get(url)
        t = r.text
        dict = json.loads(t)
        for i in dict:
            if i == 'results':
                s = dict[i]
                lists.append(s)
        cnt+=len(lists)
    if cnt>max:
        max=cnt
        post1=p1
        post2=p2
        id=ssss
    ssss+=1
print(name[id])



