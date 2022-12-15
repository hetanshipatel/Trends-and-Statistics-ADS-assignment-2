# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 15:32:03 2022

@author: Hetanshi
"""


# In[ ]:
   
    
# import libraries for performing functions
import pandas as pd
import numpy as np
import matplotlib.pyplot as pylt
from scipy import stats

# In[ ]:

    

# LIFE EXPENTANCY BAR GRAPH
   

# reads file and stores it in a variable
output_LE = open("Life Expentancy.csv", "r")
print("\nLife Expentancy Output: \n", output_LE) # printing the file
life_expe_rows=[] # creates rows array


# reads CSV and stores it in variable
life_expe = pd.read_csv("Life Expentancy.csv")
print("\n Life Expentancy: \n", life_expe)


# drop particular columns
drp_lifeexp_column = life_expe.drop(['Country Code', 'Indicator Name', 'Indicator Code', '2021'], axis=1)
print("\nLife Expectancy after dropping particular columns: \n", drp_lifeexp_column)


# selects particular rows using slicing method
new_life_expe = drp_lifeexp_column.iloc[[18,33,37,42,58,75,109,120],:] #we used iloc for choosing particular rows and all columns
print("\nExtracted Life Expentancy: \n", new_life_expe)


# removes NaN values from dataset
drp_lifeexp_null = new_life_expe.dropna()
print("\nExtracted Life Expentancy after removing NaN: \n", drp_lifeexp_null)


# calculates Normal Distribution of particular year through "scipy" module
print("\nNormal Distribution: \n", stats.skew(new_life_expe["2000"])) # we used "skew" is for calculating normal distribution


# calculates average of total life expectancy through "numpy" module
print("\nAverage Life Expentancy: \n", life_expe.mean()) # we used "mean" for averaging


# removes first two lines
drp_lifeexp_null = drp_lifeexp_null.iloc[2:]
print("\nRemoving first two lines from Life Expectancy: \n", drp_lifeexp_null)


# indexes the "Country Name" column
lifeexpe_index = drp_lifeexp_null.set_index('Country Name')
print("\nLife Expectancy Country Name Index: \n", lifeexpe_index)


# selects "Country Name" column for further use
lifeexp_sel_cols = (new_life_expe["Country Name"])


# arranges length of column
x = np.arange(len(lifeexp_sel_cols))


# extracts particular years and stores it in a variable
lifeexp_one = (new_life_expe["1969"])
lifeexp_two = (new_life_expe["1979"])
lifeexp_three = (new_life_expe["1989"])
lifeexp_four = (new_life_expe["1999"])
lifeexp_five = (new_life_expe["2009"])
lifeexp_six = (new_life_expe["2019"])


# plots figure and adjusts figure size in plot
pylt.figure(figsize=(12,8))


# bar graph plot
pylt.bar(x-0.3,lifeexp_one, width=0.1, label="1969", edgecolor="black", color="blue")
pylt.bar(x-0.2,lifeexp_two, width=0.1, label="1979", edgecolor="black", color="yellow")
pylt.bar(x-0.1,lifeexp_three, width=0.1, label="1989", edgecolor="black", color="brown")
pylt.bar(x+0.1,lifeexp_four, width=0.1, label="1999", edgecolor="black", color="purple")
pylt.bar(x+0.2,lifeexp_five, width=0.1, label="2009", edgecolor="black", color="red")
pylt.bar(x+0.3,lifeexp_six, width=0.1, label="2019", edgecolor="black", color="cyan")


# manipulates ticks on x-axis
pylt.xticks(x, lifeexp_sel_cols, rotation = 45) # we used rotation to refer the angle of ticks on x-axis

pylt.xlabel("Countries")
pylt.ylabel("Life Expectancy")
pylt.legend()
pylt.show()


# DEATH RATE BAR GRAPH


# reads file and stores it in a variable
output_DR = open("Death Rate.csv", "r")
print("\nDeath Rate Output: \n", output_DR) #prints the file
rows=[]


# function which reads rows in file and populates header with header information
for rows in output_DR:
    print("\nDeath Rate Rows in Output: \n",rows)
    print()


# reads CSV and stores it in variable
death_rates = pd.read_csv("Death Rate.csv")
print("\nDeath Rate: \n", death_rates)

drp_deathr_column = death_rates.drop(['Country Code', 'Indicator Name', 'Indicator Code', '2021'], axis=1)
print("\nLife Expectancy after dropping particular columns: \n", drp_deathr_column)


# selects particular rows using slicing method
new_death_rate = drp_deathr_column.iloc[[18,33,37,42,58,75,109,120],:] # iloc used for choosing particular rows and all columns
print("\nExtracted Forest Area: \n", new_death_rate)


# removes NaN values from dataset
drp_deathr_null = new_death_rate.dropna()
print("\nExtracted Forest Area after dropping NaN: \n", drp_deathr_null)


# removes first two lines
drp_deathr_null = drp_deathr_null.iloc[2:]
print("\nRemoving first two lines from Forest Area: \n", drp_deathr_null)


# indexes the "Country Name" column
deathr_index = drp_deathr_null.set_index('Country Name')
print("\nForest Area Country Name Index: \n", deathr_index)


# selects "Country Name" column for further use
deathr_sel_cols = (new_death_rate["Country Name"])


# arranges length of column
x = np.arange(len(deathr_sel_cols))


# extracts particular years and stores it in a variable
deathr_one = (new_death_rate["1969"])
deathr_two = (new_death_rate["1979"])
deathr_three = (new_death_rate["1989"])
deathr_four = (new_death_rate["1999"])
deathr_five = (new_death_rate["2009"])
deathr_six = (new_death_rate["2019"])


# plots figure and adjusts figure size in plot
pylt.figure(figsize=(12,8))


# bar graph plot
pylt.bar(x-0.3,deathr_one, width=0.1, label="1969", edgecolor="black", color="red")
pylt.bar(x-0.2,deathr_two, width=0.1, label="1979", edgecolor="black", color="blue")
pylt.bar(x-0.1,deathr_three, width=0.1, label="1989", edgecolor="black", color="orange")
pylt.bar(x+0.1,deathr_four, width=0.1, label="1999", edgecolor="black", color="brown")
pylt.bar(x+0.2,deathr_five, width=0.1, label="2009", edgecolor="black", color="violet")
pylt.bar(x+0.3,deathr_six, width=0.1, label="2019", edgecolor="black", color="green")


# manipulates ticks on x-axis
pylt.xticks(x, deathr_sel_cols, rotation = 45) # we used rotation to refer the angle of ticks on x-axis

pylt.xlabel("Countries")
pylt.ylabel("Death Rate")
pylt.legend()
pylt.show()


# In[ ]:

    

#URBAN POPULATION LINE GRAPH


# reads file and stores it in a variable
output_urpop = open("Urban Population.csv", "r")
print("\nUrban Population Output: \n", output_urpop) # prints the file
rows=[]

    

# transpose function
def transpose(output_urpop):
    output_urpop = open("Urban Population.csv", "w")
    print("\nUrban Population Output: \n", output_urpop)
    output_urpop = pd.DataFrame.transpose(output_urpop)
    print("\nUrban Population Transpose: \n", output_urpop)
    
    return transpose(output_urpop) #returns transposed file


# reads csv file and stores it in a variable
urpop = pd.read_csv("Urban Population.csv")
print("\nUrban Population: \n", urpop)


# drops particular columns
urpop = urpop.drop(['Indicator Code', 'Indicator Name', '2021'], axis=1)
print("\nUrban Population after dropping particular columns: \n",urpop)


# transposes the dataframe
urpop = pd.DataFrame.transpose(urpop)
print("\nUrban Population Transpose: \n", urpop)


# populates header with header information
header3 = urpop.iloc[0].values.tolist()
urpop.columns = header3
print("\nUrban Population Header: \n",urpop)


# removes first two lines
urpop = urpop.iloc[2:]
print("\nRemoving first two lines from Urban Population: ", urpop)


# arranges length of column
print(len(urpop))


# extractes particular countries and stores it in a variable
urpop = urpop[urpop["Benin"].notna()]
urpop = urpop[urpop["Botswana"].notna()]
urpop = urpop[urpop["Switzerland"].notna()]
urpop = urpop[urpop["Cameroon"].notna()]
urpop = urpop[urpop["Denmark"].notna()]
urpop = urpop[urpop["Finland"].notna()]
urpop = urpop[urpop["India"].notna()]
urpop = urpop[urpop["Kazakhstan"].notna()]



# indexes change as integer type
urpop.index = urpop.index.astype(int)


# plots figure and adjusts figure size in plot
pylt.figure(figsize=(12,8))


# line graph plot
pylt.plot(urpop.index, urpop["Benin"], label="Benin", linestyle='dashed')
pylt.plot(urpop.index, urpop["Botswana"], label="Botswana", linestyle='dashed')
pylt.plot(urpop.index, urpop["Switzerland"], label="Switzerland", linestyle='dashed')
pylt.plot(urpop.index, urpop["Cameroon"], label="Cameroon", linestyle='dashed')
pylt.plot(urpop.index, urpop["Denmark"], label="Denmark", linestyle='dashed')
pylt.plot(urpop.index, urpop["Finland"], label="Finland", linestyle='dashed')
pylt.plot(urpop.index, urpop["India"], label="India", linestyle='dashed')
pylt.plot(urpop.index, urpop["Kazakhstan"], label="Kazakhstan", linestyle='dashed')

pylt.xlabel("Year")
pylt.ylabel("Urban Population")
pylt.legend(bbox_to_anchor=(1,0.5), loc="center left")
pylt.show()


# In[ ]:
    
    

# FERTILITY LINE GRAPH


# reads file and stores it in a variable
output_fer = open("Fertility Rate.csv", "r")
print("\nFertility Rate Output: \n", output_fer) #prints the file
rows=[]

# function which reads rows in file and populates header with header information
for rows in output_fer:
    print("\nFertility rate rows in Output: \n", rows)
    print()
    
    
# transposes function
def transpose(output_fer):
    output_fer = open("Fertility Rate.csv", "w")
    print("\n Fertility rate Output: \n", output_fer)
    output_fer = pd.DataFrame.transpose(output_fer)
    print("\nFertility rate Transpose: \n", output_fer)
    
    return transpose(output_fer) #returns transposed file


# reads csv file and stores it in a variable
fer = pd.read_csv("Fertility Rate.csv")
print("\nFertility Rate: \n", fer)


# drops particular columns
fer = fer.drop(['Country Code', 'Indicator Name', 'Indicator Code', '2021'], axis=1)
print("\nFertility Rate after dropping particular columns: \n", fer)


# transposes the dataframe
fer = pd.DataFrame.transpose(fer)
print("\nFertility rate Transpose: \n", fer)


# populates header with header information
header4 = fer.iloc[0].values.tolist()
fer.columns = header4
print("\nFertility rate Header: \n", fer)


# removes first two lines
fer = fer.iloc[2:]
print("\nRemoving first two lines from fertility rate: \n", fer)


# arranges length of column
print(len(fer))


# extractes particular countries and stores it in a variable
fer = fer[fer["Benin"].notna()]
fer = fer[fer["Botswana"].notna()]
fer = fer[fer["Switzerland"].notna()]
fer = fer[fer["Cameroon"].notna()]
fer = fer[fer["Denmark"].notna()]
fer = fer[fer["Finland"].notna()]
fer = fer[fer["India"].notna()]
fer = fer[fer["Kazakhstan"].notna()]


# indexes change as integer type
fer.index = fer.index.astype(int)


# plots figure and adjusts figure size in plot
pylt.figure(figsize=(12,8))


# line graph plot
pylt.plot(fer.index, fer["Benin"], label="Benin", linestyle='dashed')
pylt.plot(fer.index, fer["Botswana"], label="Botswana", linestyle='dashed')
pylt.plot(fer.index, fer["Switzerland"], label="Switzerland", linestyle='dashed')
pylt.plot(fer.index, fer["Cameroon"], label="Cameroon", linestyle='dashed')
pylt.plot(fer.index, fer["Denmark"], label="Denmark", linestyle='dashed')
pylt.plot(fer.index, fer["Finland"], label="Finland", linestyle='dashed')
pylt.plot(fer.index, fer["India"], label="India", linestyle='dashed')
pylt.plot(fer.index, fer["Kazakhstan"], label="Kazakhstan", linestyle='dashed')


pylt.xlabel("Year")
pylt.ylabel("Fertility Rate")
pylt.legend(bbox_to_anchor=(1.0,0.5), loc="center left")
pylt.show()





