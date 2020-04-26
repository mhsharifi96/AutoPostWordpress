# -*- coding: utf-8 -*-


import http.client
import json
def ApiCreatePost(data):
    conn = http.client.HTTPConnection("test.rovzenews.ir")

    payload = "{\n\t\"title\":\"دانلود باشه جدیدترین روضه و نوحه در ایران و جهان \",\n\t\"content\":\"دانلود جدیدترین و خفن ترینها از سایت روضه نیوز دات ای ار بیایید پیش ما سایتمون داره خفن میشه  همه رو میخواییم زخمی کنیم\",\n\t\"publish\":\"draft\"\n}"

    headers = {
        'authorization': "Bearer <TOKEN>", #test.rovzenews.ir "For TEST"
        #  'authorization':"Bearer <TOKEN>",  #rovzenews.ir
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "7af7a2d3-fdb2-6e66-41ad-be50287b8983"
        }

    # data = {
    #     "title":"تست برای اینکه ببینم ار میکننه یا نه",
    #     "content": "download newest nohe in site rovzenews we can it 2270",
    #     "publish":"draft"
    # }

    data = json.dumps(data)

    conn.request("POST", "/wp-json/wp/v2/posts", data.encode('utf-8'), headers)

    res = conn.getresponse()
    data = res.read()
    status = res.status
    if status ==201:
        print(status)
        # print(data)
        PostData = json.loads(data)
        print(PostData['id'])
        return PostData['id'] ,201
    else:
        print("Error")
        return '',status








