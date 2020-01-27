import pandas as pd
import numpy as np
import numpy as np
from fredapi import Fred

api_key = '...'
fred = Fred(api_key=api_key)



ticker_tcoes_Rdata=pd.read_excel(...)
ticker=ticker_tcoes_Rdata.iloc[:,0]     #data tickers
tcodes=ticker_tcoes_Rdata.iloc[:,1]     #transform codes
raw_data.to_excel('/home/emre/Masaüstü/Replication of Fred-MD Python/raw_data.xlsx')




#HWI                Help-Wanted Index for United States
#HWIURATIO          Ratio of Help Wanted/No. Unemployed
#S&P: indust        S&P’s Common Stock Price Index: Industrial
#S&P div yield      S&P’s Composite Common Stock: Dividend Yield 
#S&P PE ratio       S&P’s Composite Common Stock: Price-Earnings Ratio 
#CONSPI             Nonrevolving consumer credit to Personal Income 

'''
mising_ticker=[]  
data={}    
for i in range(len(ticker)):
    
    try:
        
       dum1=fred.get_series(ticker.loc[i],observation_start='1959-01-01',observation_END='2020-01-01',frequency='m')
       data[ticker[i]]=dum1.copy()
    except:
    
       print(ticker[i])     
       mising_ticker.append(ticker[i])
       

raw_data=pd.DataFrame(data)


raw_data.to_excel('/home/emre/Masaüstü/Replication of Fred-MD Python/raw_data.xlsx')

###############################################################################################################################
'''







#% -------------------------------------------------------------------------
#% INPUT:
#%           rawdata     = raw data 
#%           tcode       = transformation codes for each series
#%
#% OUTPUT: 
#%           yt          = transformed data
#%
#% -------------------------------------------------------------------------
#% SUBFUNCTION:
#%           transxf:    transforms a single series as specified by a 
#%                       given transfromation code
#%
#% =========================================================================
#% 




###############################################################################################################################33
#APPLY TRANSFORMATION:
# Initialize output variable

yt=[]                #Initialize output variable                   
N=raw_data.shape[1]  #Number of series kept

for i in range(N):
    
    dum=transxf(raw_data.iloc[:,i].values,tcodes[i])
    yt.append(dum)
    
 
trans_data=pd.DataFrame(yt).T
trans_data.columns=raw_data.columns
trans_data.index = raw_data.index

trans_data.to_excel('/home/emre/Masaüstü/Replication of Fred-MD Python/trans_data.xlsx')
    
###############################################################################################################################33
    


def transxf(x,tcode) :
    
#=========================================================================
#DESCRIPTION:
#This function transforms a single series (in a column vector)as specified
#by a given transfromation code.
#
#-------------------------------------------------------------------------
#INPUT:
#           x       = series (in a column vector) to be transformed
#           tcode   = transformation code (1-7)
#
# OUTPUT:   
#           y       = transformed series (as a column vector)
#
# =========================================================================
# SETUP:
# Number of observations (including missing values)
    
#Number of observations (including missing values)
  n=x.size
  
#Value close to zero 
  small=1e-6
#Allocate output variable
  y=np.nan*np.ones(n);
  y1=np.nan*np.ones(n);
#  global result 
  if tcode==1: #  no transformation): x(t)
          y=x
          result=y
        
  elif tcode==2: # First difference: x(t)-x(t-1)
      
          y[2:n]=x[2:n]-x[1:n-1];
          result= y
        
  elif tcode==3:  #Second difference: (x(t)-x(t-1))-(x(t-1)-x(t-2))
      
          y[3:n]=x[3:n]-2*x[2:n-1]+x[1:n-2]       
          result=y

  elif tcode==4:    #Natural log: ln(x)
      
          if min(x) < small:
              y=np.nan
          else :
              y=np.log(x)
              
          result=y
           
  elif tcode==5:   #First difference of natural log: ln(x)-ln(x-1)
            
          if  min(x[pd.notnull(x)]) > small:
              x=np.log(x)
              y[2:n]=x[2:n]-x[1:n-1]
              result=y
#          else:
#              result=x
            
  elif tcode==6:  #Second difference of natural log: (ln(x)-ln(x-1))-(ln(x-1)-ln(x-2))
         
          if  min(x[pd.notnull(x)]) > small:
              x=np.log(x)
              y[3:n]=x[3:n]-2*x[2:n-1]+x[1:n-2]
              result=y
#          else:     
#              result=x
    
  elif tcode==7 :  #First difference of percent change: (x(t)/x(t-1)-1)-(x(t-1)/x(t-2)-1)
        
          y1[2:n]=(x[2:n]-x[1:n-1])/x[1:n-1]
          y[3:n]=y1[3:n]-y1[2:n-1]
          result=y
      
        
        
  return result           

###############################################################################################################################
###############################################################################################################################
###############################################################################################################################
  





    






















