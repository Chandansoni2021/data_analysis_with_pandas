# import pandas as pd 
# df = pd.Series([1,2,3,4])
# print(df)

# output :-
# 0    1
# 1    2
# 2    3
# 3    4
# dtype: int64

# query :-
# print(df.index)

# output :- 
# RangeIndex(start=0, stop=4, step=1)
# import pandas as pd 
# df = pd.Series([1,2,3,4])
# df.index=('a','b','c','d')
# df.index=[12,32,45,23]
# print(df)

# output:-
# 0    1
# 1    2
# 2    3
# 3    4
# dtype: int64


# k = df['a']
# print(k)

#output : _  1

# import pandas as pd 
# df = pd.Series([1,2,3,4])
# df['a']=["chandan"]
# print(df)

# output 
# 0            1
# 1            2
# 2            3
# 3            4
# a    [chandan]

# import pandas as pd 
# df = pd.Series([1,2,3,4])
# j=df[df>2]
# print(j)

# output:-
# 2    3
# 3    4



# import pandas as pd 
# df = pd.Series(['chandan','ram','ishita','yogya','neeraj'])
# print(df)

# 0    chandan
# 1        ram
# 2     ishita
# 3      yogya
# 4     neeraj
# dtype: object

import pandas as pd 
df = pd.Series(['chandan','ram','ishita','yogya','neeraj'])
l = df[df*2]
print(l)