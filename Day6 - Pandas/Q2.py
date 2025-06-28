#2- find all orders in furniture category with sales amount between 1000 and 1200

import pandas as pd
df = pd.read_csv('orders.csv')
# Finding all orders in the furniture category with sales amount between 1000 and 1200

furniture_orders = df[(df["category"] == "Furniture") & ((df["sales"] >=1000) & (df["sales"] <= 1200))] 
print(furniture_orders)

