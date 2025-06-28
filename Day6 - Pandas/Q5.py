""" 5- in the orders data frame rename column names to upper case ..
eg order_id should be ORDER_ID, ship mode should be SHIP_MODE and so on

#6- again change the column names back to lower case """

import pandas as pd
df = pd.read_csv("orders.csv")
rename_upper = df.columns.str.upper()
df.columns = rename_upper
rename_lower = df.columns.str.lower()
df.columns = rename_lower
print(df)