import requests
import json
import time

url = 'https://oapi.dingtalk.com/robot/send?access_token=dfb282779fa574887abaade18616db9be415fcc4b11289a6bd487a59f2b5a641'

bili_ids = ['37663924','437316738']
yesterday = time.time()-60*60*24*1  # 1天前
for bid in bili_ids:
    bili_url = 'https://api.bilibili.com/x/space/arc/search?mid='+bid+'&pn=1&ps=25&jsonp=jsonp'

    r = requests.get(bili_url)
    videos = r.json()['data']['list']['vlist']
    for video in videos:
        if(video['created']>yesterday):
            print(video['title'],video['description'],video['author'])
            print(video['created'])
            obj = {
                "msgtype": "link", 
                "link": {
                    "text": video['description']+'B站', 
                    "title": video['title'], 
                    "picUrl": 'http:'+video['pic'], 
                    "messageUrl": "https://www.bilibili.com/video/av%s" %(video['aid'])
                }
            }
            requests.post(url,
                headers={'Content-Type': 'application/json'},
                data=json.dumps(obj)
            )