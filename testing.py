import numpy as np
import re
import pandas as pd


with open('didi.txt', 'r') as f:
    a = f.read()

# print(a[:100000].split('\n'))
regex = r'[0-9]{2}/[0-9]{2}/[0-9]{4},\s[0-9]{2}:[0-9]{2}'
regex2 = pattern = r'(?<=[0-9]{2}/[0-9]{2}/[0-9]{4},\s[0-9]{2}:[0-9]{2}\s\-\s).*?(?=\n[0-9]{2}/[0-9]{2}/[0-9]{4}|\Z)'
# a = np.array

# regex = r'[87][0-9]{9}'
# regex = r'meow[0-9]+cat'

date = re.findall(regex,a)
chat = re.findall(regex2, a,flags=re.DOTALL)


x = pd.DataFrame({'hi':date,'bye':chat})
x.to_excel('didi.xlsx')
print(x)