#1- fetch all the orders with indexes  multiple of 5 eg : 5,10,15,20 and so on..... . 
# Display order_id , category and sales columns only 

import pandas as pd
df = pd.read_csv('orders.csv')
# Fetching orders with indexes that are multiples of 5
result = df.iloc[5::5, :][['order_id', 'category', 'sales']]
# Displaying the result
print(result)
