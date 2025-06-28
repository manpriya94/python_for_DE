import pandas as pd


df = pd.read_csv("/Users/priyankasmac/Desktop/Python for DE/iPhone_Project/iphone.csv")
df_columns = [ col.replace(' ','_') for col in df.columns ] #created a new list with spaces replaced by underscores
df.columns = df_columns # Assign the new list to df.columns to update the DataFrame's column names

average = df["Star_Rating"].mean() # Calculate the average of the Star_Rating columnrame
average = round(average, 2) # Round the average to 2 decimal places
df['Star_Rating'].fillna(average) # Fill NaN values in the Star_Rating column with the calculated average

df_avg_rating = df.groupby("Ram")["Star_Rating"].mean().reset_index()  # Group by Ram and calculate the average Star_Rating
df_avg_rating = df_avg_rating.rename(columns={"Star_Rating": "Average_Star_Rating"})  # Rename the column for clarity

df = df.merge(df_avg_rating, on="Ram", how="left")  # Merge the average ratings back into the original DataFrame

df_1 = df["Star_Rating"].fillna(df["Average_Star_Rating"] , inplace=True)  # Fill NaN values in Star_Rating with the average ratings
print(df)