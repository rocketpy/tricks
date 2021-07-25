import pandas as pd
import pandas_profiling
   
# read the file
df = pd.read_csv('Geeks.csv')
   
# run the profile report
profile = df.profile_report(title='Pandas Profiling Report')
   
# save the report as html file
profile.to_file(output_file="pandas_profiling1.html")
   
# save the report as json file
profile.to_file(output_file="pandas_profiling2.json")
