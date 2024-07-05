from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import datetime
import os
import time

def request_copilot(input_text):
    # デスクトップのパスを取得
    desktop_path=os.path.expanduser('~/Desktop')
    # ドライバーの場所を指定
    driver_path=desktop_path+R"\copilot\tool\ChromeDriver\chromedriver.exe"
    # ブラウザの場所指定
    browser_path=desktop_path+R"\copilot\tool\Chrome\chrome.exe"
    
    # ウェブドライバ設定
    options=Options()
    options.binary_location=browser_path
    cService=webdriver.ChromeService(executable_path=driver_path)
    driver=webdriver.Chrome(service=cService,options=options)
        
    # 起動したいサイトのURLを入力
    driver.get('https://copilot.microsoft.com/')
    
    # 質問を入力するテキストボックスを取得
    time.sleep(10)
    shadowroot1=driver.find_element(By.CLASS_NAME, 'cib-serp-main').shadow_root
    shadowroot2=shadowroot1.find_element(By.ID, 'cib-action-bar-main').shadow_root
    shadowroot3=shadowroot2.find_element(By.CSS_SELECTOR, 'div > div.main-container > div > div.input-row > cib-text-input').shadow_root
    input=shadowroot3.find_element(By.ID, 'searchbox')
    # テキストボックスに質問入力
    input.send_keys(input_text)
    
    # 質問の送信ボタンを取得
    time.sleep(10)
    sendbutton=shadowroot2.find_element(By.CSS_SELECTOR, 'div > div.main-container > div > div.bottom-controls > div > div.bottom-right-controls > div.control.submit > button')
    # 質問の送信ボタンをクリック
    sendbutton.click()
    
    # copilotからの返答を取得
    time.sleep(30)
    shadowroot4=driver.find_element(By.CLASS_NAME, 'cib-serp-main').shadow_root
    shadowroot5=shadowroot4.find_element(By.ID, 'cib-conversation-main').shadow_root
    shadowroot6=shadowroot5.find_element(By.CSS_SELECTOR, '#cib-chat-main > cib-chat-turn').shadow_root
    shadowroot7=shadowroot6.find_element(By.CSS_SELECTOR, 'cib-message-group.response-message-group').shadow_root
    shadowroot8=shadowroot7.find_element(By.CSS_SELECTOR, 'cib-message[type=text]').shadow_root
    output=shadowroot8.find_element(By.CSS_SELECTOR, 'cib-shared > div').get_attribute('aria-label')
    return(output)


# デスクトップのパスを取得
desktop_path=os.path.expanduser('~/Desktop')
# 質問一覧ファイルの場所を指定
input_text_path=desktop_path+R"\copilot\data\input\input.txt"
# 出力用ファイルの末尾に付ける現在時刻を取得 
dt=datetime.datetime.now()
# copilotからの返答を出力するファイルの場所を指定
output_text_path=desktop_path+R"\copilot\data\output\output_"+dt.strftime('%Y%m%d%H%M%S')+".txt"

with open(input_text_path,encoding="utf-8") as f1:
    for input_text in f1:
        output_text=request_copilot(input_text)
        with open(output_text_path,'a',encoding="utf-8") as f2:
            f2.write('##########\n')
            f2.write('■質問\n')
            f2.write(input_text)
            f2.write('##########\n')
            f2.write('■返答\n')
            f2.write(output_text+'\n')
            f2.write('##########\n')
            f2.write('\n')