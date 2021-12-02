import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import time
import smtplib


api_key = 'XXXX'

ts = TimeSeries(key=api_key, output_format ='pandas')
data, meta_data = ts.get_intraday(symbol = 'GUSH', interval = '1min', outputsize = 'full')
print(data)
i= 1
#while i ==1:
#  data, meta_data = ts.get_intraday(symbol = 'GUSH', interval = '1min', outputsize = 'full')
#  data.to_excel("stockoutput.xlsx")
#  time.sleep(60)
close_data = data['4. close']
percent_diff = close_data.pct_change()
print(percent_diff)
#when day trading you only care about the last value because thats when you want to sell or keep stock
last_change = percent_diff[-1]

server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login("jusbot75@gmail.com", "Pandass*^8520")
if abs(last_change) > .0004:
  server.sendmail("jusbot75@gmail.com", "joeyisthebest69@gmail.com","GUSH is worth selling right now")
server.quit()
