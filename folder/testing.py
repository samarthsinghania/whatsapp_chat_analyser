from functions import df_maker as dfm
import pandas
c = dfm()

df = c.txt_to_df('other\\test-chat.txt')

print(df)