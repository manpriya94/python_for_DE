
f1 = open("/Users/priyankasmac/Desktop/Python for DE/Namaste Kart Project/orders_2.csv")
f2 = open("/Users/priyankasmac/Desktop/Python for DE/Namaste Kart Project/product_master.csv")
f3 = open("/Users/priyankasmac/Desktop/Python for DE/Namaste Kart Project/error_orders_1.csv" ,'w') #creating error file to write errored records

#print(f1.read())
#print(f2.read())
header = next(f1)

f3.write(header[:-1] +  ",rejection_reason\n")  #last record in file is new line char , hence removing it before appending new column then adding again

header = next(f2)
product_id = []
for line in f2.readlines() :
    column = line.strip().split(',')
    product_id.append(column[0])
print(product_id)

for line in f1.readlines() :
    column = line.strip().split(',')
    if column[2] not in product_id :
        f3.write(line[:-1] + ",product_id not found in product master file\n")





 

