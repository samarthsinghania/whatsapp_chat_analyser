# %%
import plotly.express as px
from functions import df_maker
from functions import graph_maker as gm

obj = gm()


df = df_maker().txt_to_df('C:\\Users\\singh\\OneDrive\\Desktop\\personal_project\\whatsapp_analyser\\other\\test-chat.txt')
# print(df)
# print(obj.total_mssg_sent(df))


# #graph
print(obj.total_mssg_sent(df))

# import plotly.express as px





# print(new_df)
# %%
