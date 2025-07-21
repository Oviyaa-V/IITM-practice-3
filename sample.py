file = open("data.csv")
file.readline()
#data = file.readlines()
#print(data)
row = list(map(int,(file.readline().strip()).split(",")))
print(row)
print(type(row))
print(type(row[0]))
file.close()
'''
print(data[1])
print(type(data[1]))
'''