# -*- coding: utf-8 -*-
"""BUAN 6341.501_ML Assignment1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gYkXnyrLtbMDjL7vwsSehfWyyp3giN2y

#Classification of Iris flowers using Machine Learning

<h3>University of Texas at Dallas - MS Business Analytics </h3>
<h3>BUAN 6341.501 - Applied Machine Learning - S23 </h3>
<h3>Assignment 1: Building a test model - Douglas Obeng</h3>
<center><img src='https://raw.githubusercontent.com/obengdouglas/UTD-BUAN6341_AppliedML/main/Assignment1-Building_a_test_model/iris-flower.webp' width="600" height="314" alt="Image of iris flower"></center>

Notebook submitted for Assignment 1 of the Applied Machine Learning Course at The University of Texas at Dallas, Spring 2023

In this project, machine learning is used to model 3 species of iris flowers using some characteristics of the flowers.

The goal is to build a simple test model that can be used to predict unknown species of iris flowers.

# Assignment Specifics

- Create a data set of about 15 to 20 records and three to four features.
- Load your data into a Dataframe
- Split your data into two tables – One with features and one with outcomes (only one column – with a binary outcome)
- Clean your data set (Use a CSV file and it will be easier to clean)
- Build a model based
- Use the Predict method to predict a value that is not in your outcomes
- Due Date – Tuesday, January 31, 2022 by Midnight.
- You will upload your assignment in the dropbox  .

# Introduction

The iris is a common flowering plant (genus *iris*) mainly found in the temperate zones of the Northern hemisphere. There are about 310 species that come in various sizes, shapes and colours. 

Three of the most common species are the *iris setosa*, *iris versicolor* and *iris virginica*. These 3 look similar in color (bluish purple) and shape but may be distinguished from one another using the dimensions of their flower petals and sepals. 

The original Iris flower data set, also known as Fisher's Iris data or Anderson's Iris data set was used by British Biologist Statistician Ronald Fisher in his 1936 paper *The use of multiple measurements in taxonomic problems*. The data was collected by Edgar Anderson and consists of 50 samples of each of the 3 species (150 total).

**References**


[Neuraldesigner - Iris flower classification](https://www.neuraldesigner.com/learning/examples/iris-flowers-classification#DataSet)

[Analyticsvidhya - Iris flower classification using ML](https://www.analyticsvidhya.com/blog/2022/06/iris-flowers-classification-using-machine-learning/)

[Kaggle - Iris flower dataset](https://www.kaggle.com/datasets/arshid/iris-flower-dataset?select=IRIS.csv)

[Wikipedia - Iris flower](https://en.wikipedia.org/wiki/Iris_(plant))


[Wikipedia - Iris flower data set](https://en.wikipedia.org/wiki/Iris_flower_data_set)

#Data

The data for this project was downloaded from the Kaggle website - [Iris Flower Dataset](https://https://www.kaggle.com/datasets/arshid/iris-flower-dataset?select=IRIS.csv).

The data has been saved in my github repository for direct online access within this notebook: [DO Github - complete iris dataset](https://github.com/obengdouglas/UTD-BUAN6341_AppliedML/blob/main/Assignment1-Building_a_test_model/IRIS.csv).


**NOTE - For the purpose of this assignment, the original dataset has been modified to include only 20 records with 2 possible outcomes (iris setosa and iris versicolor). Two of the records have also been given null values for illustration of data cleaning. There is the option to use the complete data though**


The modified data has been saved in my github repository for direct online read in the notebook: [DO Github - modified iris dataset](https://raw.githubusercontent.com/obengdouglas/UTD-BUAN6341_AppliedML/main/Assignment1-Building_a_test_model/IRIS_modified.csv)

<center><img src='https://raw.githubusercontent.com/obengdouglas/UTD-BUAN6341_AppliedML/main/Assignment1-Building_a_test_model/iris_species.jpg' width="511" height="230" alt="image of the 3 iris species used in model - iris setosa, iris versicolor and iris virginica"></center>

The 4 independent features are Sepal Length, Sepal Width, Petal Length, and Petal Width. All the lengths are in centimeters. The dependent feature (outcome) is Species. Species refers to one of the species whose characteristics were measured.

# Libraries and packages
"""

#import libraries
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

"""#Load dataset into dataframe"""

irisdata = 'https://raw.githubusercontent.com/obengdouglas/UTD-BUAN6341_AppliedML/main/Assignment1-Building_a_test_model/IRIS_modified.csv' #save url of modified dataset location as object
#irisdata = 'https://raw.githubusercontent.com/obengdouglas/UTD-BUAN6341_AppliedML/blob/main/Assignment1-Building_a_test_model/IRIS.csv' #uncomment this line to use complete dataset

iris.df = pd.read_csv(irisdata) #read data

#This works fine in colab. in case of any issues, read the included dataset from your local directory
#iris.df = pd.read_csv('Desktop/Github/UTD-BUAN6341_AppliedML/Assignment1-Building_a_test_model/IRIS_modified.csv') #replace with local directory of dataset

iris.df #view dataframe

"""# Data Cleaning

Drop rows with null values
"""

iris.isnull() #dataframe showing boolean results for the presence of null values. Index 5 and 6 have TRUE for column 'petal_width'

iris.df.isnull().sum() #number of null values for each column. Column petal_width has 2 null values

iris_clean.df = iris.df.dropna(how="any") #drop all rows that have at least one null value (any)

iris_clean.df #view cleaned dataframe

"""#Exploratory Data Analysis (EDA)"""

import seaborn as sns
sns.pairplot(iris_clean.df, hue='species') #Use seaborn to plot pairwise relationship of independent features

"""#Split data into features and outcome"""

X = iris_clean.df.drop(columns = ['species']) #save features as X 
y = iris_clean.df['species'] #save outcome as y

X #view features dataframe

y #view outcome dataframe

"""#Model Training"""

model = DecisionTreeClassifier() #select type of model algorithm to use
model.fit(X,y) #fit model

"""#Model Prediction"""

predictions = model.predict([[6,3,1.5,0.3], [6,2.5,4,3.5]]) #predict the outcoe of 2unknown species of iris flowers with the specified feature dimensions in order
predictions #view prediction results

"""# Conclusion

The model has predicted the unknown species as *Iris*-setosa and Iris-versicolor respectively
"""