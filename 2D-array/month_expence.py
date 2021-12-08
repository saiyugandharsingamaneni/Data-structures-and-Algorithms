data= {'January' : 2200,
        'February' : 2350,
        'March' : 2600,
        'April' : 2130,
        'May' : 2190}
data_num=[2200,2350,2600,2130,2190]
print(data)
print('extra amount spend in february compared to january',data_num[1]-data_num[0])
print('total expense of firt quarter',data_num[0]+data_num[1]+data_num[2])
print('did i spend 2000$ in any month:',2000 in data_num)
data_num.append(1980)
print(data_num)
data_num[3]= data_num[3]-200
print(data_num)