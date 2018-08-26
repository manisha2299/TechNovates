import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt

#read data
dataframe = pd.read_csv('dataset.csv')

y_values = dataframe[['NS1']]
x_values = dataframe[['platelet count']]

#train model on data
body_reg = linear_model.LinearRegression()
body_reg.fit(x_values, y_values)

#visualize results
plt.scatter(x_values, y_values)
plt.ylabel('NS1 LEVEL')
plt.xlabel('PLATELET COUNT')
plt.axis([20000,450000,0.04,2.0])
plt.plot(x_values, body_reg.predict(x_values),'ro-')
x=input()
print("Platelet count " + x)
x=int(x)
y=body_reg.predict(x)
#if(y<0.04):
   # y=0.04    
print("NSI LEVEL : ",y)
def fun():
    if(y>1.0):
        print("High chances of dengue")
        print("Consultants list:")
        f = open("doctors.txt", "r")
        print(f.read())
    elif(y<0.5):
        print("No chances of dengue")
    else:
        print("maybe chances of dengue ")
        print("Suggested Medicines : ")
        print("Acetaminophen(paracetomol)")  
        print("Avoid medicines:Aspirin, Ibuprofen")
print()
plt.show()
fun()
