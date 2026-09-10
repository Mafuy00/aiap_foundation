import pandas as pd

# Sample data
data = {'City': ['New York', 'Paris'], 'Population': [8419000, 2148000]}
df = pd.DataFrame(data)  

# Can you figure out what's wrong with this line of code?
df = df.set_index('City')  
  
print(df)