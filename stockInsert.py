import yfinance as yf
import pymssql
import random
import time
from datetime import datetime

"""
使用 pymssql 對資料進行連接
"""
server= "stanleyoreo.database.windows.net"
database = "free-sql-db-9475644" 
user = "dbeng"
password = "Zxcv1234"
'''密碼洩漏問題'''

INS_SQL = """
    INSERT into dbo.yfinanceLastPrice(sid,sname,last_price)
    VALUES(
        %s,
        %s,
        %d
    )
"""
try:
    connect = pymssql.connect(server,user,password,database)
    cursor = connect.cursor()
    dt2  = datetime(2026, 3, 18, 13, 30, 0)
    while datetime.now()<dt2:
    # for i in range(1,3):
        # 產生亂數 介於( 1850~ 1905)
        tick = yf.Ticker("2330.TW")
        info = tick.fast_info
        cursor.execute(INS_SQL, ("2330","TSMC",info.last_price))
        # pymssql 預設設定 autocommit = false
        connect.commit()
        time.sleep(300)
        print(f"寫入資料:2330,TSMC,{info.last_price}")

    print("資料寫入完畢")
    cursor.close()
    connect.close()

except Exception as e:
    print(f'連線失敗:原因({e})')
