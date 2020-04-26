import json
import io
import time
import  os
from apiPost import ApiCreatePost

filename = 'json/channel_messages_akbari.json'
mp3FileName = ''
ArtistDir = 'akbari'


def TextSpliter(TextMessage):
    TextObj = []
    
    TextSplit = TextMessage.split('\n')
    
    for line in TextSplit : 
        
        if "#" in line:
            TextObj.append({'kind':'mention','text':line})
        elif  line =="": print('')
        # elif "@" or 'instagram': print ('link line')
        else:
            TextObj.append({'kind':'content','text':line})
    
    if not TextObj :
        print('this file has not caption')
        
    return TextObj

with io.open(filename, 'r', encoding='utf8') as f:
    data = json.load(f)

    for message in data :
        TemplatePost = {
            "title":'',
            "content":'',
            # "categories":[75],
            "publish":"draft"
        }
        TextArray = [] 
        MentionArray = []
        title= ""
        content = """<h2 style="text-align: center;"><span style="color: #ff6600;"><strong>{} </strong></span></h2>
                
                <h3 style="text-align: center;"><span style="color: #993366;">کربلایی مهدی اکبری</span></h3>
                <h3 style="text-align: center;">فاطمیه ۹۸</h3>
                <p style="text-align: center;">برای دانلود <strong>{}</strong> به ادامه مطلب مراجعه نمایید...</p>
                <p style="text-align: center;"><!--more--></p>

                
                <p style="text-align: center;">درحال پردازش متن</p>
                &nbsp;
                <h1 style="text-align: center;"><a href="http://rovzenews.ir/singer/%d9%85%d9%87%d8%af%db%8c-%d8%a7%da%a9%d8%a8%d8%b1%db%8c/">آرشیو کامل نوحه و روضه مهدی اکبری</a></h1>
                <p style="text-align: center;"><a href="https://t.me/rovzenews_ir">جدیدترین نوحه و روضه ها در کانال تلگرامی روضه نیوز</a></p>
                """
        artist = "مهدی اکبری"

        TextMessage = message['message']
        # print(TextMessage)
        resTextSplit = TextSpliter(TextMessage)
        # print (resTextSplit)
        for text in resTextSplit:
            
            if text['kind'] == 'content':
                # print('if',text['text'])
                TextArray.append(text['text'])
                
            elif text['kind'] == 'mention':
                MentionArray.append(text['text'])
        # print(TextArray)
        if TextArray:
            if len(TextArray)>=2:
                title =  TextArray[0] + ' ' + TextArray[1] +'-' + artist
            else:
                title =  TextArray[0] + '-' + artist
        else :
            if MentionArray:
                ClearText = MentionArray[0].replace('#','')
                ClearText = ClearText.replace('_',' ')
                title = ClearText + '-' + artist
            else:
                title = 'روضه نیوز' + ' ' +artist
        
        if len(message['media']['document']['attributes']) == 1:
            mp3FileName = message['media']['document']['attributes'][0]['file_name']
        else :
            mp3FileName = message['media']['document']['attributes'][1]['file_name']

        if os.path.exists("downloads/{0}/{1}".format(ArtistDir,mp3FileName)) is True :
            TemplatePost['title'] = title
            TemplatePost['content'] = content.format(title,title) +"http://dl2.rovzenews.ir/{0}/{1}".format(ArtistDir,mp3FileName)
            # print(content.format(title,title))
            postID,status = ApiCreatePost(TemplatePost)    
            if status !=201:
                print('cant create post: ',message['id'])
            time.sleep(2)   
        else:
            print('cant find file :',message['id'])


# ApiCreatePost()    


