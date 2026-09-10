import pandas as pd  
  
data = {  
    'Name': ['Alice', 'Bob', 'Charlie'],  
    'Age': [25, 30, 35],  
    'Score': [88, 92, 95]  
}  
  
df = pd.DataFrame(data)  
  
total_score = df['Score'].sum()  
  
columns_list = df.columns
  
print("Total Score:", total_score)  
print("Columns:", columns_list)