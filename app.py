import pickle
model=pickle.load(open('model.pkl','rb'))

print("Titanic Survival Prediction: ")

# # #take input 
Pclass= int(input("Enter Passenger class(1/2/3): "))
Sex=int(input("Enter Sex(0=male,1=female): "))
Age=float(input("Enter Age: "))
SibSp=int(input("Enter no.of Sibling or spouse: "))
Parch=int(input("Enter no. of parents-children: "))

#prediction
input_data=[[Pclass,Sex,Age,SibSp,Parch]]
prediction=model.predict(input_data)

if prediction[0]==1:
    print("Passenger Survived")
else:
    print("Passenger Did Not Survived")

