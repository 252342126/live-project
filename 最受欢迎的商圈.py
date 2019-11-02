import requests
import json
url2='http://api.map.baidu.com/place/v2/search?query=商圈&scope=2&location=26.0887007395,119.3032476646&filter=cater&sort_name=overall_rating&radius=20000&page_size=100&output=json&ak=7HWkIo9B8P4S9vLUEVn9MSAY84YhFP1N&page_num='

def init():
    global url2
    lists=[]
    for j in range(10):
        url=url2+str(j)
        r=requests.get(url)
        t=r.text
        dict=json.loads(t)
        for i in dict:
            if i=='results':
                s=dict[i]
                lists.append(s)
    return lists
def sq():
    score=0
    name=''
    t=init()
    for i in t:
        for j in i:
            k=j

            for key in k:
                if(key=='detail_info'):
                    m=k[key]
                    try:
                        if score<(int)(m['comment_num']):
                            score=(int)(m['comment_num'])
                            name=j['name']
                    except:
                        a=1
    return name

print(sq())