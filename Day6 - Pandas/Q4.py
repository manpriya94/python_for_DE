""" 4- create a new column in the orders dataframe with name profit_flag. Set its value as as per below rule 
"High Profit" if profit > 100
"Medium Profit" if profit>50
"Low Profit" if profit>=0
"loss" if profit<0
 """

import pandas as pd
df = pd.read_csv("orders.csv")

def profit_loss(profit) :
    if profit > 100 :
        return "Highest Profit"
    elif profit > 50 :
        return "Medium Profit"
    elif profit > 0 :
        return "Low Profit"
    else :
        return  "Loss"

# Applying the function to create the profit_flag column
df["profit_flag"] = df["profit"].apply(profit_loss)     

print(df)
