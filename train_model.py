#importing the dependencies
import numpy as np                #create numpy arrays
import pandas as pd           #create dataframe
import matplotlib.pyplot as plt   #create graph and plot
import seaborn as sns

from sklearn.model_selection import train_test_split  #contains data prprocessing functions and ml algos
from sklearn.linear_model import LogisticRegression   #binary classification
from sklearn.metrics import accuracy_score   #used to evaluate our model

#load the data from csv.file to Pandas Dataframe
titanic_data=pd.read_csv('titanic.csv')

#print first 5 rows
# print(titanic_data.head())

# # #no. of row and column
# # print(titanic_data.shape)   #11 columns -> features  1column(survived)-> target

# # #getting somme info about dataset
# # #titanic_data.info()  #from here we can see that some values are missing in age and age column (total 891) 

# # #check the no. of missing values in each column
# #print(titanic_data.isnull().sum())

# # #handling the missing value  -> most of the values(687)in cabin column are missing so there is no sense to replace by mean so we will drop this column
titanic_data=titanic_data.drop(columns='Cabin',errors='ignore')   #0 represents row and 1 represents column

# #check if cabin is dropped
# #print(titanic_data.columns)

# #in age column 177 values are missing so we will replace all the null values with mean value
# # #replacing the missing values in age column with mean value
titanic_data['Age']=titanic_data['Age'].fillna(titanic_data['Age'].mean())  #if we dont use inplace the change will not be in whole original dataset but only in the cell  -> with - same df is modified and without original df stays same and the new df has the column removed

# # #Embark column -> has only two missing values -> we will replace by most repeating value(mode)
# # #finding the mode value of embark column
# print(titanic_data['Embarked'].mode())

# #replacing the missimg value in Embarked column with S(mode)
titanic_data['Embarked']=titanic_data['Embarked'].fillna(titanic_data['Embarked'].mode()[0])

# print(titanic_data.isnull().sum())

#Data analysis
#getting some statistical measures about the data
# print(titanic_data.describe())    #not very useful when we have categorical column(used in age not in survived)

#find number of people survived or not
# print(titanic_data['Survived'].value_counts())

#data visualization
# sns.set()

#making a count plan for survived column
#sns.countplot(x='Survived',data=titanic_data)

# making a count plot for 'Sex' column
#sns.countplot(x='Sex', data=titanic_data)

#number of survivors based on gender
# sns.countplot(x='Sex',hue='Survived', data=titanic_data) #the males are more but gender survived more is female

#making countplot for pclass (people survived based on pclass)
# sns.countplot(x='Pclass',hue='Survived', data=titanic_data)

#plot for embarked
#sns.countplot(x='Embarked', data=titanic_data)

#replace text value in "sex" with some numerical value to feed data to machine male- 0  female-1
#ENCODING THE CATEGORICAL VALUE
# print(titanic_data['Sex'].value_counts())

# print(titanic_data['Embarked'].value_counts())

#converting categorical columns(sex and embarked)
titanic_data.replace({'Sex':{'male':0, 'female':1}, 'Embarked':{'S':0,'C':1,'Q':2}},inplace=True)

# print(titanic_data.head())

#we need to separate our target i.e. Survived
#Separating features and target
x=titanic_data[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch']]
y=titanic_data['Survived']

#print(x)    #featues 
# print(y)    #targets

# #splitting the data into training data and test data
x_train, x_test, y_train, y_test =train_test_split(x,y, test_size=0.2, random_state=2)
# print(x.shape, x_train.shape,x_test.shape)  #total data, training, testing

model=LogisticRegression()
model.fit(x_train, y_train)

# import pickle
# pickle.dump(model, open('model.pkl', 'wb'))

# x_train_prediction=model.predict(x_train)
# # print(x_train_prediction)
# training_accuracy=accuracy_score(y_train,x_train_prediction)
# print('Training Accuracy:',training_accuracy)
# # print(titanic_data.head())

# x_test_prediction=model.predict(x_test)
# testing_accuracy=accuracy_score(y_test, x_test_prediction)
# print("Testing Accuracy:", testing_accuracy)


# plt.show()