"""
提供排程的方式固定在 9:00 ~ 13:30 分執行 , 每30秒執行一次
第二 單次執行( 13:31 分) 執行一次
套件: schedule
pip install schedule
"""
import schedule
import time
from datetime import datetime

def run_every_5seconds():
    print(f"每 5秒執行一次")

def run_every_30seconds():
    print(f"每 30秒執行一次")

def run_every_60seconds():
    print(f"每 60秒執行一次")

def run_at_spec_time():
    now= datetime.now()
    print(f"觸發時間: {now}")

def run_and_cancelJob():
    # 本任務視情況 決定是否繼續執行, 例如各分點的檔案在營業結束後要上傳 pos csv file
    # schedule 沒有提供設定開始的邏輯 , 必須在 func內自己判斷時間是否滿足開始執行
    cnt = True
    if( cnt ):
        return schedule.cancel_job   #通知 schedule 不用再安排後續的任務了




#只是安排一個任務 
# schedule.every(5).seconds.do(run_every_5seconds)
# schedule.every(1).minutes.do(run_every_60seconds)
# schedule.every().day.at("14:29").do(run_at_spec_time)
# schedule.every().hours.at(":31").do()
# schedule.every().friday.at("16:30").do()

# 隨機一個數值進行觸發
schedule.every(2).to(10).seconds.do(run_at_spec_time).until("14:49")

# 設定結束或取消的方式
# schedule.every(30).seconds.do(run_every_30seconds).until("14:38")  # 開始每30秒執行任務直到 13:30 結束
# schedule.every().hours.at(":39").do(run_and_cancelJob)   # 一旦檔案下載完成 自動結束


while True:
    #要求 schedule 每n單位 檢查一次是否有任務需要執行
    schedule.run_pending()
    time.sleep(1) 