from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from glob import glob
#from .views import bot
from .views import *
from selenium.webdriver.firefox.options import Options
from webdriver_manager.chrome import ChromeDriverManager
#user_input = input('Enter name of song here:')
try:
    def download(song):
            user_input = song
            list_of_files_before_download = glob('/home/nkosindu/Downloads/*.mp3')
            #print(list_of_files_before_download)


            #Get the loop start time ( current time)
            start = time.time()

            #this is the time in seconds , we set to zero initially
            elapsed = 0

            # instance of Options class allows
            # us to configure Headless Chrome
            options = Options()
        
            # this parameter tells Chrome that
            # it should be run without UI (Headless)
            #options.headless = True 
            #options.add_argument("--window-size=1920,1080")
            options.add_argument("--headless")
            #options.add_argument("--disable-gpu")
            #options.add_argument(
            #    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")      # write your code to click download
            driver = webdriver.Firefox()
                #tubidy.com


            driver.get("https://tubidy.com/")
            driver.find_element(By.CLASS_NAME,'form-group')
            time.sleep(4)
            driver.find_element(By.CLASS_NAME,'nav-search-input').send_keys(user_input)
            driver.find_element(By.CLASS_NAME,'nav-search-btn').click()
            list_of_media_bodies =[]
            driver.find_element(By.XPATH,'//div[@class="col-xs-12"]//div[@class="media-left"]/a').click()
            time.sleep(4)
            driver.find_element(By.XPATH,'//div[@class="row donwload-box"]//ul[@class="list-group"]/li[3]/a').click()
            time.sleep(2)
            driver.find_element(By.XPATH,'//div[@id ="donwload_box"]//ul[@class="list-group"]/li[3]/a').click()
            print(f'Please wait {user_input} song is downloading ....')
            time.sleep(35)
            driver.close()
            while elapsed < 120:

                list_of_files_after_download = glob(r'/home/nkosindu/Downloads/*.mp3')
                #get time and check if 120 second is elapsed
                done = time.time()
                elapsed = done - start
                global newfile
                # get new file list
                list_of_files_after_download = glob('/home/nkosindu/Downloads/*.mp3')
                newfile = \
                    list(set(list_of_files_after_download).difference(list_of_files_before_download))

                #if new file is created then break the loop
                #global my_song
                if len(newfile):
                    my_song  = newfile[0][25:]
                    print(f"Your song {my_song} has been donloaded")
                    return my_song           
                    break

                #download(user_input)        
except:
    print('Sorry song not found')
