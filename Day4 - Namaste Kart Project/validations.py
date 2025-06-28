import os
directory_path = "/Users/priyankasmac/Desktop/Python for DE/Namaste Kart Project/incoming"

# Function to check if product_id in incoming file is present in product master file
# If not present, write the record to error file with reason for rejection
# Also, write header in error file only once
# Function takes filename as input and a boolean to write header or not
# If write_header is True, it writes the header in error file, else it appends records without header
# The error file is created in the same directory as the incoming file with name 'error_orders_1.csv'

def check_product_id(filename, write_header = True):
    f1 = open(directory_path + "/" + filename)  #opening file in incoming directory
    f2 = open("/Users/priyankasmac/Desktop/Python for DE/Namaste Kart Project/product_master.csv")
    f3 = open("/Users/priyankasmac/Desktop/Python for DE/Namaste Kart Project/error_orders_1.csv" ,'a') #creating error file to write errored records
    
    header = next(f1)
    if write_header:
        f3.write(header[:-1] +  ",rejection_reason\n")  #last record in file is new line char , hence removing it before appending new column then adding again
    
    header2 = next(f2)
    product_id = []
    for line in f2.readlines() :
        column = line.strip().split(',')
        product_id.append(column[0])
    
    for line in f1.readlines() :
        column = line.strip().split(',')
        
        if column[2] not in product_id :
            
            f3.write(line[:-1] + ",product_id not found in product master file\n")
            #f3.flush()        
    f3.close()


write_header = True
for file in os.listdir(directory_path):
    check_product_id(filename = file, write_header= write_header)
    write_header = False


