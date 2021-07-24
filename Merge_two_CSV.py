import pandas as pd
  

data_1 = pd.read_csv('file_1.csv')
data_2 = pd.read_csv('file_2.csv')
  
# using merge function by setting how='inner'
result = pd.merge(data_1, data_2, 
                   on='LOAN_NO', 
                   how='inner')
  
print(result)
