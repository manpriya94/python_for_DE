import os
directory_path = "/Users/priyankasmac/Desktop/Python for DE/Namaste Kart Project/incoming"

def sales_validation(filename):

    f1 = open(directory_path + "/" + filename)  #opening file in incoming directory
    f2 = open("/Users/priyankasmac/Desktop/Python for DE/Namaste Kart Project/product_master.csv")
    f3 = open("/Users/priyankasmac/Desktop/Python for DE/Namaste Kart Project/error_orders_1.csv" ,'a') 

    header = next(f1)
    header2 = next(f2)

    for line in f1.readlines():
        column = line.strip().split(',')
        for line2 in f2.readlines():
            column2 = line2.strip().split(',')
            if column[2] == column2[0]:  # Check if product_id matches
                if column[4] != int(column2[2]) * int(column[3]):   # Check if sales_price matches product_price * quantity
                    print(f"Mismatch found in {filename}: {column[2]} - sales_price: {column[4]}, product_price: {column2[2]}, quantity: {column[3]}")
                    f3.write(line[:-1] + ",sales_price does not match product_price * quantity\n")
                break  # Exit inner loop once a match is found

    f3.close()


for file in os.listdir(directory_path):
    sales_validation(filename=file)
