#!/usr/bin/env python
# coding: utf-8

# # U.S. Medical Insurance Costs

# # Background
#    US Medical Costs are for a section of the US public are provided on a CSV file called 'insurance.csv'. The file contains information such as age, sex, BMI, # of children, whether or not they are a smoker, what region they live in (broken down to: Northeast, Northwest, Southeast, Southwest), and their costs. The goal of the project is two-fold: 1.) Showcase a mastery in Python basics and 2.)Develop one's own answers to questions. 

# # Project Scope
#     My goal in this exercise with the data provided is to answer the following questions:
#     1.) Which age demographic (broken down below) has the lowest insurance cost?
#     
#     Graph the results as we go along to demonstrate mastery in a Python module (Numpy and Seaborn).
#     
#  Age ranges for demographics: 18 - 24, 25 - 34, 35 - 44, 45 - 54, 55 and older

# # Predictions
#     The lowest average insurance cost for an age demographic will be the 25 - 34 year age range

# In[2]:


# import the modules we need
import csv
import numpy as np 
import pandas as pd


# In[3]:


# Generate lists based on the categories within the dataset to parse through later

with open('insurance.csv') as insurance:
    insurance_dict = {}
    
    csvreader = csv.reader(insurance, delimiter = ',')
    fieldnames = next(csvreader)
    age = []
    sex = []
    bmi = []
    num_children = []
    smoker_status = []
    region = []
    charges = []
    
    for i in csvreader:
        age.append(i[0])
        sex.append(i[1])
        bmi.append(i[2])
        num_children.append(i[3])
        smoker_status.append(i[4])
        region.append(i[5])
        charges.append(i[6])
#test one to make sure I have the information extracted
#print(len(age))
#returns 1338
unique_keys = list(range(0,1337,1))
#print(unique_keys)


# Now that we have the information we need to start looking into our data - we need to convert the ages, bmi and charges into an interger to be able to work with them. Currently, they are strings and objects, respectively which doesn't help us when we later build out the functions to break down the charges. 

# In[4]:


# Iterator for converting age into Interger
#print("Original list is : " +str(age))

# Use map() to perform conversion
age = list(map(int, age))

# Verify the result
#print("Modified list is: " +str(age))


# In[5]:


# Iterator for converting BMI into a float type

# Print orginal bmi
#print("Original BMI is : " +str(bmi))

# Convert using map() to a floating type
bmi = list(map(float, bmi))

#print("New BMI is: " +str(bmi))


# In[6]:


# Iterator for converting charges into float

#print("Current charges are: " +str(charges))

#convert using map() to a floating type
charges = list(map(float, charges))

# Print("New Charges are a floating type: " +str(charges))


# In[7]:


# Build the dictionary


def build_medical_dictionary(unique_keys, age, sex, bmi, num_children, smoker_status, region, charges):
    medical_ins_data = {}
    for i in unique_keys:
        medical_ins_data[unique_keys[i]] = {"Age": age[i],
                                           "Sex": sex[i],
                                           "BMI": bmi[i],
                                           "Number of Children": num_children[i],
                                           "Smoker Status": smoker_status[i],
                                           "Region": region[i],
                                           "Charges": charges[i]}
    return medical_ins_data

medical_data = build_medical_dictionary(unique_keys, age, sex, bmi, num_children, smoker_status, region, charges)
#print(medical_data)


# We have the dictionary, but it's hard to read everything, let's clean it up with Pandas.

# In[9]:


df = pd.DataFrame.from_dict(
                medical_data, 
                orient='index')
print(df.head(5))


# Now that we have our data organized better into a dictionary, we can tackle the demographic - cost relationship. We will define our demographic data, split the costs into lists, and anaylze the average cost based on demographic. 

# In[25]:


young_demo = df[(df.Age >= 18) & (df.Age <= 24)]
mid_demo = df[(df.Age >= 25) & (df.Age <= 34)]
old_mid_demo = df[(df.Age >= 35) & (df.Age <= 44)]
older_demo = df[(df.Age >= 45) & (df.Age <= 54)]
seniors_demo = df[df.Age >= 55]


# In[26]:


print(young_demo.head(5))
print(mid_demo.head(5))
print(old_mid_demo.head(5))
print(older_demo.head(5))
print(seniors_demo.head(5))


# Now that the tables are split by demographic, we can run the average charges for each demographic. 

# In[27]:


eighteen_to_twenty_five = young_demo['Charges'].mean()
twenty_six_to_thirty_four = mid_demo['Charges'].mean()
thirty_five_to_forty_four = old_mid_demo['Charges'].mean()
forty_five_to_fifty_four = older_demo['Charges'].mean()
fifty_five_and_older = seniors_demo['Charges'].mean()


# In[28]:


print('The average charges for someone between eighteen to twenty five is ' +str(eighteen_to_twenty_five))
print('The average charges for someone between twenty-six and thirty-four is ' +str(twenty_six_to_thirty_four))
print('The average charges for someone between thirty-five and forty-four is ' +str(thirty_five_to_forty_four))
print('The average charges for someone between forty-five and fifty-four is ' +str(forty_five_to_fifty_four))
print('The average charges for someone between fifty-five and older is ' +str(fifty_five_and_older))


# Conclusion:
# The lowest average cost is for the 18 - 25 demographic, which for me was slightly surprising. I presumed that the cost for that demgoraphic would be slightly higher as they would still be involved in riskier activities, such as smoking, fast driving, etc. The twenty-six to thirty-four demographic was my prediction. I will add to this project later on to break down to see if anything influenced the charges in the age demographics (was there several smokers or a few high charge individuals that offset the group?)
