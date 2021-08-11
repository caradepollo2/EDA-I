import random
counting=0
semaforo=''
ages_of_persons_with_covid=[]
db=[]
for i in range(100):
  age=random.randint(1,100)
  age=str(age)
  indicator=random.uniform(0,1)
  indicator=str(indicator)
  data=age+','+indicator+'\n'
  db.append(data)

database=open("mydatabase.csv", "w")
database.writelines(db)
database.close()
database=open('mydatabase.csv', 'r')
lines=database.readlines()
for line in lines:
    line=line.split(',')
    line[1]=line[1].replace('\n','')
    line[1]=float(line[1])
    indicator=line[1]
    line[0]=int(line[0])
    age=line[0]
    if indicator>=0.8:
        counting=counting+1
        ages_of_persons_with_covid.append(age)
if (counting==0):
    semaforo='Verde'
elif(counting>=1 or counting<30):
    semaforo='Amarillo'
elif(counting>=31 or counting<=70):
    semaforo="Naranja"
else:
    semaforo='Rojo'

average=sum(ages_of_persons_with_covid)/len(ages_of_persons_with_covid)
print("El promedio de edades de infectados es: ", average)
print("Semáforo: ", semaforo)
database.close()
