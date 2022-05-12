# -*- coding: utf-8 -*-
"""DSP 439 Final Exam .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YVxnA3-kR8OprQ8p9YYlmdpTzx9QWFJT

Nathan Kong
 
Professor Schwartz 

DSP 439

11 May 2021
"""

import pandas as pd

"""Question 1: Possible Kmers """

def possible(string,k):
  """
  Description of the function,

  identify paramaters:

  return type
  """
  # subString_list = []

  # for i in range(0, len(string)):

  #   temp = string[i:i+k] 
  #   if len(temp) == k:
  #     subString_list.append(temp)
  
  return (min(len(string)-k+1,4**k))

  
  #return (subString_list) 

  # if string == "":
  #   print("Please Try Again")
  # if k > len(string):
  #   return(0)
  # else: 
  #    return (subString_list) 
    

#4^1 = 1
# I got the possible fit 
# how many kmers can I have ? which is 4, need 4^k 

output = possible("ATGGTCTTATGG", -4) 
output2 = possible("ATTTGGATT", 1)

print(output2)

"""Question 2: Unobserved Kmers"""

def observed(string, k) :

  #temp_List = []
  subString_list = []

  for i in range(0, len(string)):
    temp = string[i:i+k]
    if temp not in subString_list and len(temp) == k:
      subString_list.append(temp)

  # for i in range(0, len(subString_List)):
  #   if (len(subString_List[i]) != k):
  #     subString_List.pop()
  
  # for i in subString_List:
  #   if i not in temp_List:
  #     temp_List.append(i)

  

  return len(subString_list)

output = observed("ATATATATATATA",2)
output2 = observed("ATTTGGATT",4)
output3 = observed("ATGGTCTTATGG", 4)
print(output)
print(output3)

"""Question 3: Data Frame"""

def dataFrame(string,k):

  observed_count = 0
  possible_count = 0
  data = []

  for i in range(1,k+1):
    observed_count = observed(string,i)
    possible_count = possible(string,i) 
    data.append([i,observed_count,possible_count])

  df = pd.DataFrame(data, columns = ["k", "Observed Kmers", "Possible Kmers"])
  df = df.style.hide_index()
  return (df)

output = dataFrame("ATTTGGATT", 9)
output

""" Question 4: Linguistic Complexity 



"""

def linguistic(string, k):
  
  num_count = 0
  dem_count = 0

  for i in range (k,0,-1) :

    num = observed(string, i)
    dem = possible(string, i)
    num_count += num
    dem_count += dem
    #print("num = ", num, "dem = ",dem)

  output = num_count/dem_count
  print(output)
  # return output

linguistic("ATTTGGATT", 9)

__init__ == "main"

  ### Input ###
  
  read.openfile()

  "ATTGAAGGTTWA"
  "AJFJFWJAWFJF"
  "ADJWDJADWJWAJD"
  argv[1]
  argv[2]

  ### Call our function on the data ###


  ### Call our test cases ###


  ### output ###