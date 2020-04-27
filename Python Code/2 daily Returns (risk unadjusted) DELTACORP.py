import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as web


df = web.get_data_yahoo("DELTACORP.NS",
                            start = "2019-04-01",
                            end = "2020-03-31")        
                             #adds reproducability of code and flexibility of time period    



"""We can also use the following code in comments if the scraped csv from attached zip is used

df = pd.read_csv('DELTACORP.csv',header=[0])            """



df['Daily_Return']=df['Close'].pct_change()
                                #Daily Returns have been stored in a separate column
df['Daily_Return']=df['Daily_Return']*100                                
                                #will be relevant as we need to return values in% and not /100 

print("Daily Returns %")
print("Maximum:"+ str(round(df['Daily_Return'].max(axis=0),3)))    
print("Minimum:"+str(round(df['Daily_Return'].min(axis=0),3)))  
print("Mean:"+str(round(df['Daily_Return'].mean(),4)))  
print("Sample Standard Deviation:"+str(round(df['Daily_Return'].std(axis=0),4)))  

df['Daily_Return'].plot(kind='line',title='Line Graph for Daily Returns')
plt.show()


df.drop(df.columns.difference(['Date','Close','Daily_Return']), 1, inplace=True)
df.to_csv (r'D:\000Finance\FOFA ASSIGNMENT 2\85_Shubh_2018A2PS0832H_DELTACORP\2 daily Returns (risk unadjusted) DELTACORP.csv', header=True)
