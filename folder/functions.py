import numpy as np
import re
import pandas as pd
import plotly.express as px

class df_maker:
    def __init__(self):
        pass

    def txt_to_df(self, txt_file_location):
        '''this method takes argument:
        1. txt_file_location : the text file location of the messages
        returns the Pandas DataFrame in format
        ['sno', 'datetime', 'sender', 'message', 'type']
        sno: str
        datetime: []

        N O T E :
        this only works for text and media Messages.
        does not work for Voice and others.
        '''

        with open(txt_file_location, 'r') as f:
            chat = f.read() #will be string

        date_time_regex = r'[0-9]{2}/[0-9]{2}/[0-9]{4},\s[0-9]{2}:[0-9]{2}' #08/07/2026, 21:22 this for this
        sender_message_regex = r'(?<=[0-9]{2}/[0-9]{2}/[0-9]{4},\s[0-9]{2}:[0-9]{2}\s\-\s).*?(?=\n[0-9]{2}/[0-9]{2}/[0-9]{4}|\Z)' # Name: messsage {this type of format}

        date = re.findall(date_time_regex, chat) # for date time, Returns List [datetime1, datetime2 ..]
        mssg = re.findall(sender_message_regex, chat,flags=re.DOTALL) #[mssg1,mssg2..] 
        #DotALL basically as messages contain multiple lines and line break, this ignores them 

        df = pd.DataFrame({'sno':[i for i in range(1,len(date))], #no mistake here, just ignores 1st row
                           'datetime':date[1:],
                           'sender_message':mssg[1:]}) #ignroe that default line('messagea and calls are end-to-end encryp...')

        #To convert date time column to datetime
        df['datetime'] = pd.to_datetime(
            df['datetime'],
            format="%d/%m/%Y, %H:%M"
        )

        #split sender:message to sender and message columns
        df['sender_message'] = df['sender_message'].str.split(': ') # into :['sender', 'message']
        list_col = df['sender_message']
        
        df.insert(2, "sender", list_col.apply(lambda lis:lis[0])) #takes second item of above list
        df.insert(3, "message", list_col.apply(lambda lis:lis[1].strip() if len(lis)==2 else None))#2nd item now

        del df['sender_message']

        #for adding type column
        df['type'] = df['message'].apply(lambda val:'media' if val[-15:]=='(file attached)' else 'text')  
        #bascially if last ke some part == '(file attached)' then media type

        return df



class GraphMaker: #oh ok, this is PEP 8 way of writing class names
    def __init__(self):
        self.plotly_js_file = 'other\\plotly_js.js'

    def total_mssg_sent(self, chat_df, graph='pie', output='str'):
        '''total_mssg method take 1 parameter:
        1. chat_df: dataframe in format:
        2. graph: which graph 
            Options: 
                1. pie: for Pie Chart: of 2 talkers
                2. sunburst: for sunburst chart [Not currently here(Coming soon)]

        3. output: which type of output (str, photo_graph)
                1. str: returns string of html
                2. photo_graph: returns photo of graph in jpg format [Not currently here(Coming soon)]

        ['sno', 'datetime', 'sender', 'message', 'type'] 

        and returns the html in string format'''

        new_df = chat_df.groupby('sender').count().reset_index() #counts the total values of each group and reset index(without reset index, it throws error when name=sender done)

        #pie chart:
        print(new_df)
        figure = px.pie(new_df, values='datetime',names='sender') #making figure

        fig_html_str = figure.to_html(full_html=False, include_plotlyjs='other\\plotly_js.js') #plotly_js is the plotly's js thing it uses to make these graph(very imp)

        return fig_html_str # returns the html str
        