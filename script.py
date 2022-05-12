"""
Nathan Kong
Rachel Schwartz
DSP 439
Final Exam
"""

#!/usr/bin/env python


from operator import index
from pickle import TRUE
import string
import pandas as pd





### Question 1: Possible
def possible(string,k):
    """
    This function takes in a string and kmers are arguments. 
    This function produces the number of possible substrings base off "ACTG". It only produce possible number of kmers
    based on the length of the string. It takes a comparison of two by selecting the minimum of the two.
    Return type is an integer.  
    """
    #var1 contains possible kmers based off length of string
    var1 = len(string)-k+1
    #var2 contain total number of kmers of size 4. 
    var2 = 4**k 
    lowest = 0
    #Make comparisons of the minimum and return the lowest. 
    if var1 < var2:
      lowest = var1
    if var2 < var1:
      lowest = var2
    
    #Handle the test case when the string is empty or when k is 0. 
    if string == "" or k == 0:
      lowest = 0
      return lowest
    
    return lowest
  

  
 

### Question 2: Observed
def observed(string, k) :
  """
  This function takes in a string and kmers are arguments.
  This function appends substrings of size kmers to a list and does not contain any duplicates. 
  The return type is an integer.
  """
  subString_list = []

  #Reads in the string, substring the string by incrementing based off k.
  for i in range(0, len(string)):
    temp = string[i:i+k]
    #Only appends whens there no duplicates and length of the substring is size k.
    if temp not in subString_list and len(temp) == k:
      subString_list.append(temp)

  #Handles test cases when the the string is empty, k values are less than 0 or negative and when k is greater than
  # than the length of the string we return a 0.
  if  string == "" or k <=0 or k > len(string):
    return 0 
  
  return len(subString_list)






### Question 3: Data Frame

def dataFrame(string,k):
  """
  This functions take in a string kmers are parameters.
  This function produces a table that contains the number of K, predicted observes and possibles.
  The return type is a dataframe/2d array. 
  """
  observed_count = 0
  possible_count = 0
  data = []

  #Calls observed and possible functions and append the information as list so it can be use as a dataframe.
  for i in range(1,k+1):
    observed_count = observed(string,i)
    possible_count = possible(string,i) 
    data.append([i,observed_count,possible_count])

  #Creates a table with columns.
  df = pd.DataFrame(data, columns = ["k", "Observed Kmers", "Possible Kmers"])
  #df = df.style.hide_index()

  #Handle testcase of the string is empty we raise a value error. 
  if string == "":
    raise ValueError("Empty String, please try again")
    
  return (df)







### Question 4: Linguistic Complexity 

def linguistic(string, k):
  """
  This function takes in a string and kmers are arguments
  This function calls the observed and possible functions and calculates the linguistic complexity of the 
  string by dividing the number of observeds by number of possibles.
  The return type is an integer
  """
  num_count = 0
  dem_count = 0
  #Calls observed and possible function and it stores as numerator and demoniator
  for i in range (k,0,-1) :
    num = observed(string, i)
    dem = possible(string, i)
    num_count += num
    dem_count += dem
    
  output = num_count/dem_count

  # Handles testcases where the strings are empty or k is 0, we print out a value error.
  if string == "" or k == 0 :
    raise ValueError("Retry and enter a value greater than 0")
  return(output)




## Get Data function 

def getData():
  """
  This function does not contains any arguments. The variable is a modified list that is free from \n.
  This function reads the seconds argument of the command line and extract each individual line and
  appends it to a list. 
  The return type is a list of characters. 
  """
  import sys
  modified = []

  #reads the text file argument which is the second argument in command line.
  with open(sys.argv[1], "r") as inFile:
    data = inFile.readlines()
    #print(data)

  #Strips the lines of "\n"
  for line in data: 
   
    modified.append(line.strip())

  return modified



def outFile(string, df):
  """
  This function takes in string and a data frame as arguments.
  This function write to another file that contains a dataframe.
  This function does not return anything and will runs as void.  
  """
  #Opens and close the string and write to a file, name aftered each string.
  with open(string, 'w') as f:
    dfAsString = df.to_string(header=TRUE, index=False)
    f.write(dfAsString)

def main():

  # Get the input data, Note! I was not to sure if you wanted us to strip the semi colon or not because I did not know if
  # it was sort of a test case.
  string = getData()
  string = [s.strip(';') for s in string]

  # Runs the linguistic function and output the complexity to terminal. 
  for i in string:
    output = linguistic(i,len(i))
    print("linguistic for ",i,"=",output)
  # Runs the dataFrame function and calls the outfile helper function to output a txt. 
  for i in string:
    df = dataFrame(i,len(i))
    #df.to_csv(i)
    outFile(i,df)

#calls main function
if __name__ == "__main__":
    main()
    

