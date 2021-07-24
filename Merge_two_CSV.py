import pandas as pd
  

data_1 = pd.read_csv('file_1.csv')  # or path to file
data_2 = pd.read_csv('file_2.csv')  # or path 
  
# using merge function by setting how='inner'
result = pd.merge(data_1, data_2, 
                   on='LOAN_NO', 
                   how='inner')
  
print(result)


# to merge LEFT Join
data_1 = pd.read_csv('file_1.csv')
data_2 = pd.read_csv('file_2.csv')
  
# using merge function by setting how='left'
result = pd.merge(data_1, data_2, 
                   on='LOAN_NO', 
                   how='left')
  
print(result)


# # to merge RIGHT Join
# using merge function by setting how='right'
result = pd.merge(data1, data2,
                   on='LOAN_NO',
                   how='right')
  
print(result)
