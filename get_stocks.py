
import time
import pandas as pd
import pandas_datareader as pdr

def get_stocks(name_stocks):
    
    """
    Parmeters:
    -----------
    name_stocks: is array data type that contain the symbols of the 500 companies belong the S&P 500 index
    """
    
    API_key = 'TDQIB4FECTM52GAV'  
    stocks = {}
    end = pd.to_datetime('2020-08-01')
    start = end - pd.DateOffset(years = 5)
        
    for i, name in enumerate(name_stocks):
        
        stocks[name] = (pdr.data.DataReader(name,
                                         "av-daily-adjusted", 
                                         start = start, 
                                         end = end, 
                                         api_key = API_key))
        
        if i in [x * 5 for x in range( 1, round(len(name_stocks)/5) + 1)]:
            
            print('Waiting 62 seconds for next 5 calls')
            
            time.sleep(62)
            
    return stocks
