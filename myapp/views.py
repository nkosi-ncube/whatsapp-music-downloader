from selenium import webdriver
from django.shortcuts import render
from django.http import HttpResponse
from twilio.rest import Client 
from django.views.decorators.csrf import csrf_exempt
import time
from django.conf import settings
from . import downloader
from .downloader import *
from selenium.webdriver.firefox.options import Options
    
#path_to_user_folder = media_url + "/user_name/"


client = Client(account_sid, auth_token) 
TWILIO_PHONE_NUMBER='+14155238886'
'''
message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='Hello! This is an editable text message. You are free to change it and write whatever you like.',      
                              to='whatsapp:' 
                          ) 
 
print(message.sid)
'''

    #tubidy.com
'''from pyngrok import ngrok
ngrok.set_auth_token('2ALp6o15Ka6JMSsgkYfJMaWp1mS_5orTAzGgGpGMsGqbc8Cop')
def start_ngrok():
    port=80
    #url1=ngrok.connect(8000).public_url
    downloads_expose=ngrok.connect(port,bind_tls=True).public_url
    #print('*Tunnel url1',url1)
    print(f'*Tunnel url2 connects to {port}',downloads_expose)
    #client.incoming_phone_numbers.list(
     #   phone_number=TWILIO_PHONE_NUMBER[0].update(sms_url=url1)    )
    return downloads_expose 
'''
        

@csrf_exempt
def feedback(request):
    return render(request,'feedback.html')

@csrf_exempt
def bot(request):
    
    #message =request.POST["body"]
    
    
    if request.POST:
        message = request.POST["Body"]
        sender_name = request.POST["ProfileName"]
        number = request.POST['From'][9:]
        print(number)
        print(sender_name)
        print(request.POST)
        if message =="hi" or message =='Hi' or message =='Hello' or message=='Hie':
            message = client.messages.create( 
                                from_='whatsapp:+14155238886',  
                                body='Hello  there {}  , I am MUSIC DOWNLOADER BOT by CODESCIMATH(Nkosi Ncube) . I  assist  you to download song from youtube .This is how you type the song -Song Big Zulu imali eningi'.format(sender_name),      
                                to='whatsapp:{}'.format(number) 
                            )

        elif  'Mathematics' in  message :
            message = request.POST["Body"].replace(" ","")
            sender_name = request.POST["ProfileName"]
            try:
                if message[13:16] == 'Sep':
                    if message[16:] =='2022':    
                        url1 =r'https://saexampapers.co.za/wp-content/uploads/{}/10/{}-Maths-NSC-{}-QP-{}-{}-Eng.pdf'.format(message[16:],message[:11],message[11:13],message[13:16],message[16:])
                        url2=r'https://saexampapers.co.za/wp-content/uploads/{}/10/{}-Maths-NSC-{}-Memo-{}-{}-Eng.pdf'.format(message[16:],message[:11],message[11:13],message[13:16],message[16:])
                    else:
                        url1 =r'https://saexampapers.co.za/wp-content/uploads/{}/10/{}-NSC-{}-QP-{}-{}-Eng.pdf'.format(message[16:],message[:11],message[11:13],message[13:16],message[16:])
                        url2=r'https://saexampapers.co.za/wp-content/uploads/{}/10/{}-NSC-{}-Memo-{}-{}-Eng.pdf'.format(message[16:],message[:11],message[11:13],message[13:16],message[16:])

                    
                    print(url1)
                    print(url2)
                    download = wget.download(url1)
                    download2 = wget.download(url2)
                elif message[13:16] =='May':
                    url1 =r'https://saexampapers.co.za/wp-content/uploads/{}/8/{}-NSC-{}-QP-{}-{}-Eng.pdf'.format(message[16:],message[:11],message[11:13],message[13:16],message[16:])
                    url2=r'https://saexampapers.co.za/wp-content/uploads/{}/8/{}-NSC-{}-Memo-{}-{}-Eng.pdf'.format(message[16:],message[:11],message[11:13],message[13:16],message[16:])
                    #print(url1)
                    #print(url2)
                    download = wget.download(url1)
                    download2 = wget.download(url2)

                elif message[13:16] =='Jun':
                    url1 =r'https://saexampapers.co.za/wp-content/uploads/{}/7/{}-NSC-{}-QP-{}-{}-Eng.pdf'.format(message[16:],message[:11],message[11:13],message[13:16],message[16:])
                    url2=r'https://saexampapers.co.za/wp-content/uploads/{}/7/{}-NSC-{}-Memo-{}-{}-Eng.pdf'.format(message[16:],message[:11],message[11:13],message[13:16],message[16:])
                    print(url1)
                    print(url2)
                    download = wget.download(url1)
                    download2 = wget.download(url2)
                elif message[13:16] =='Mar':
                    url1 =r'https://saexampapers.co.za/wp-content/uploads/{}/5/{}-NSC-{}-QP-{}-{}-Eng.pdf'.format(message[16:],message[:11],message[11:13],message[13:16],message[16:])
                    url2=r'https://saexampapers.co.za/wp-content/uploads/{}/5/{}-NSC-{}-Memo-{}-{}-Eng.pdf'.format(message[16:],message[:11],message[11:13],message[13:16],message[16:])
                    print(url1)
                    print(url2)
                    download = wget.download(url1)
                    download2 = wget.download(url2)
                else:
                    url1 =r'https://saexampapers.co.za/wp-content/uploads/{}/5/{}-NSC-{}-QP-{}-{}-Eng.pdf'.format(message[16:],message[:11],message[11:13],message[13:16],message[16:])
                    url2=r'https://saexampapers.co.za/wp-content/uploads/{}/5/{}-NSC-{}-Memo-{}-{}-Eng.pdf'.format(message[16:],message[:11],message[11:13],message[13:16],message[16:])
                    print(url1)
                    print(url2)
                    download = wget.download(url1)
                    download2 = wget.download(url2)    
            except:
                print('Page not found')
                message = client.messages.create( 
                                    from_='whatsapp:+14155238886',  
                                    body='Sorry {}  ,Paper not found.Will search it for you try again later'.format(sender_name),
                                    #media_url =f"https://drive.google.com/drive/folders/1IPNuefeIXXCKm8Xxm3u1ekltxTF3dCT0/songs/gaga.mp3",      
                                    to='whatsapp:{}'.format(number)) 



            #print(message)
            url_list =[url1,url2]
            for i in range(0,2):
                message = client.messages.create( 
                                    from_='whatsapp:+14155238886',
                                    media_url = url_list[i],                                                                                                            
                                    to='whatsapp:{}'.format(number)  
                                )
       
                    
        elif 'Song' in message:
            message =request.POST['Body'].replace(" ","")
            global title
            title=message[4:]
            #media_url = settings.MEDIA_URL
            #print(dir(mudopy))
            message = client.messages.create( 
                                    from_='whatsapp:+14155238886',  
                                    body='Hello   {}  , Your song {} is downloading...This will take less than aminute if you have good network.'.format(sender_name,title),
                                    #media_url =f"https://7163-41-145-193-42.ap.ngrok.io/tmp/gaga.mp3",      
                                    to='whatsapp:{}'.format(number)) 
            #mudopy.download_path(r"C:\xampp\htdocs\tmp")
            #global user_input
            #user_input = title
            the_song = downloader.download(title)
            #song=mudopy.download(title)
            #print(mudopy.Path(song))
            #time.sleep(6)
            #song1 = mudopy.download().replace(" ","%")
            #print(song1)
            #song_now =r"https://847f-41-145-195-37.ap.ngrok.io/tmp/{}".format(song1)
            #print(f'htrtps://4716-41-150-34-161.ap.ngrok.io/{song}.mp3')
            #print('now looking for song in port 80')
            #song_now = downloaded_song
            #final = song_now.replace(" ","%")
            #print(final)
            #print(song)
            
            time.sleep(6)
            print(the_song)
            #download_song = wget.download("https://d373-41-150-35-30.ap.ngrok.io/{}".format(the_song))
            options =Options()
            options.headless =True   
            driver = webdriver.Firefox(options=options)
            #tubidy.com


            #driver.get(downloads_expose) 
            driver.refresh()
            time.sleep(4)
            driver.close()        
            message = client.messages.create( 
                                    from_='whatsapp:+14155238886',  
                                    body='Hello  there {}  , Downloaded {} ........'.format(sender_name,the_song),                                    
                                    to='whatsapp:{}'.format(number)) 
            #print("https://2a9a-41-150-33-57.ap.ngrok.io/tmp/{}")
            time.sleep(2)
            message = client.messages.create( 
                                    from_='whatsapp:+14155238886',  
                                    media_url =r"https://d86f-41-150-34-140.ngrok.io/{}".format(the_song),                                                                                                          
                                    to='whatsapp:{}'.format(number)) 
           
                                
            print(title)
            #print(downloaded_song)
            print('Done')
            print('Perfect')



        else:
                 
              message = client.messages.create( 
                                from_='whatsapp:+14155238886',  
                                body='Sorry {} i dont understand try to rephrase'.format(sender_name),      
                                to='whatsapp:{}'.format(number) 
                            )
           
                               
    return HttpResponse("hello")

    
