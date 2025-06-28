#3- find all the orders where there was a loss (profit<0) in only east and west region

import pandas as pd
df = pd.read_csv("orders.csv")
loss = df[(df["region"] == "East") & (df["profit"] < 0) | (df["region"] == "West") & (df["profit"] < 0)]
print(loss) 