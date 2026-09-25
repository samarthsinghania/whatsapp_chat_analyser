import numpy as np
import re
import pandas as pd

class df_maker:
    def __init__(self):
        pass

    def txt_to_df(self, txt_file_location):
        '''this method takes argument:
        1. txt_file_location : the text file location of the messages
        returns the Pandas DataFrame in format
        ['sno', 'date', 'time', 'sender', 'message', 'type']'''

        with open(txt_file_location, 'r') as f:
            chat = f.read() #will be string

        date_time_regex = r'[0-9]{2}/[0-9]{2}/[0-9]{4},\s[0-9]{2}:[0-9]{2}' #08/07/2026, 21:22 this for this
        sender_message_regex = r'(?<=[0-9]{2}/[0-9]{2}/[0-9]{4},\s[0-9]{2}:[0-9]{2}\s\-\s).*?(?=\n[0-9]{2}/[0-9]{2}/[0-9]{4}|\Z)' # Name: messsage {this type of format}

        date = re.findall(date_time_regex, chat) # for date time, Returns List [datetime1, datetime2 ..]
        mssg = re.findall(sender_message_regex, chat,flags=re.DOTALL) #[mssg1,mssg2..] 
        #DotALL basically as messages contain multiple lines and line break, this ignores them 

        df = pd.DataFrame({'sno':[i for i in range(1,len(date)+1)],
                           'datetime':date,
                           'sender_message':mssg})

        return df
        

