import requests
import json
url2='http://api.map.baidu.com/place/v2/search?query=美食$餐饮&scope=2&location=26.0887007395,119.3032476646&filter=cater&sort_name=overall_rating&radius=20000&page_size=100&output=json&ak=SoNxyq6RlxwK6rrnVOPtcesi4W2pfMQ1&page_num='

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



def NO5():
    t = init()
    list_1 = [['', 0.0, 0.0], ['', 0.0, 0.0], ['', 0.0, 0.0], ['', 0.0, 0.0], ['', 0.0, 0.0]]
    list_2 = [['', 0.0, 0.0], ['', 0.0, 0.0], ['', 0.0, 0.0], ['', 0.0, 0.0], ['', 0.0, 0.0]]
    list_3 = [['', 0.0, 0.0], ['', 0.0, 0.0], ['', 0.0, 0.0], ['', 0.0, 0.0], ['', 0.0, 0.0]]
    list_4 = [['', 0.0, 0.0], ['', 0.0, 0.0], ['', 0.0, 0.0], ['', 0.0, 0.0], ['', 0.0, 0.0]]
    # 降序
    # [name,price,rate]
    for i in t:
        for j in i:
            l = j['detail_info']
            try:
                money = float(l['price'])
                rate = float(l['overall_rating'])
            except:
                continue
            if money < 50:
                for k in range(0, 5):
                    if rate > list_1[k][2]:
                        q=4
                        while(q>k):
                            list_1[q][0] = list_1[q - 1][0]
                            list_1[q][1] = list_1[q - 1][1]
                            list_1[q][2] = list_1[q - 1][2]
                            q-=1
                        list_1[k][0] = j['name']
                        list_1[k][1] = float(l['price'])
                        list_1[k][2] = float(l['overall_rating'])
                        break
            elif money >= 50 and money < 100:
                for k in range(0, 5):
                    if rate > list_2[k][2]:
                        q = 4
                        while (q > k):
                            list_2[q][0] = list_2[q - 1][0]
                            list_2[q][1] = list_2[q - 1][1]
                            list_2[q][2] = list_2[q - 1][2]
                            q -= 1
                        list_2[k][0] = j['name']
                        list_2[k][1] = float(l['price'])
                        list_2[k][2] = float(l['overall_rating'])
                        break
            elif money >= 100 and money < 200:
                for k in range(0, 5):
                    if rate > list_3[k][2]:
                        q = 4
                        while (q > k):
                            list_3[q][0] = list_3[q - 1][0]
                            list_3[q][1] = list_3[q - 1][1]
                            list_3[q][2] = list_3[q - 1][2]
                            q -= 1
                        list_3[k][0] = j['name']
                        list_3[k][1] = float(l['price'])
                        list_3[k][2] = float(l['overall_rating'])
                        break
            elif money >= 200:
                for k in range(0, 5):
                    if rate > list_4[k][2]:
                        q = 4
                        while (q > k):
                            list_4[q][0] = list_4[q - 1][0]
                            list_4[q][1] = list_4[q - 1][1]
                            list_4[q][2] = list_4[q - 1][2]
                            q -= 1
                        list_4[k][0] = j['name']
                        list_4[k][1] = float(l['price'])
                        list_4[k][2] = float(l['overall_rating'])
                        break
    print(list_1)
    print(list_2)
    print(list_3)
    print(list_4)
    return list_1,list_2,list_3,list_4

NO5()