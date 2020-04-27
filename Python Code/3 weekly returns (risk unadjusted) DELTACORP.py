import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as web

delcorp = web.get_data_yahoo("DELTACORP.NS",
                            start = "2019-04-01",
                            end = "2020-03-31")

delcorp_weekly_returns = delcorp['Close'].resample('W-FRI').ffill().pct_change()    
                #resampling by weekly data with Friday as the anchor
                #even if the Friday is a holiday, the previous day is taken and filled in that day
delcorp_weekly_returns=delcorp_weekly_returns*100

print("Weekly Returns")
print("Maximum:"+ str(round(delcorp_weekly_returns.max(axis=0),3)))    
print("Minimum:"+str(round(delcorp_weekly_returns.min(axis=0),3)))  
print("Mean:"+str(round(delcorp_weekly_returns.mean(),3)))  
print("Sample Standard Deviation:"+str(round(delcorp_weekly_returns.std(axis=0),3))) 


delcorp_weekly_returns.to_csv (r'D:\000Finance\FOFA ASSIGNMENT 2\85_Shubh_2018A2PS0832H_DELTACORP\3 weekly returns (risk unadjusted) DELTACORP.csv', header=True)

