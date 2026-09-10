import pandas as pd  
  
# Sample data  
data = {'Name': ['Alice', 'Bob'], 'Age': [25,30]}  
df = pd.DataFrame(data)  
  
df = df.rename(columns={'Name': 'FullName'})  
  
print(df)