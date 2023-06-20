# find out the average price of the models of a company

file=open("cars.csv","r")
no=tot=avg=0

comp=input('Enter company name : ')

for rec in file:
    if rec.split(',')[2].lower()==comp.lower():
        #print(rec.split(','))
        no+=1
        tot+=float(rec.split(',')[3])


avg=tot/no
print('Total number of models : %d' %no)
print('average price of %s models is %.2f' %(comp,avg))
file.close()


'''
F:\Feb23-Python\DataScience\DataAnalytics>python 01AvgPrice.py
Enter company name : skoda
['sk181', 'Kushaq', 'Skoda', '1158000.0\n']
['sk182', 'Superb', 'Skoda', '3416000.0\n']
['sk183', 'Kodiaq', 'Skoda', '3749000.0\n']
Total number of models : 3
'''