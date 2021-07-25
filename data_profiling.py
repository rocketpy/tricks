import pandas as pd
import pandas_profiling
   

df = pd.read_csv('file_name.csv')
profile = df.profile_report(title='Profiling Report')
   
# save to file 
profile.to_file(output_file="file_name.html")
   
# save result as json file
profile.to_file(output_file="file_name.json")

