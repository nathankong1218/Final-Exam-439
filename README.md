# Final-Exam-439
This code produces the number of possible substrings that can be computed with in a given string of size 4 kmers, the number of observed substrings of size k that contains no duplicates, a table that contains the number of possible substrings and observed substrings indexes by the number of kmers, and an output to the terminal that contains the linguistic complexity between the observed and possible substrings. The program read in a text file and extract each individual string from the file and stores it in a list calls strings. NOTE: For the third string, there was a character of type ; in the text file. The colon was removed to respect the given argument of only computing on a string of letters, so prediction might be different or not. The functions observed and possible are computed onto strings and then is called in the dataframe function. There is a helper function that write the table to a txt table which contains the headers. It is noted the linguistic complexity of the strings are called in the main function, which is then printed onto the terminal. 

To Run the program enter these arguments into the terminal as follows.
Python script.py samplednatxt.txt
argv[0] = script.py
argv[1] = samplednatxt.txt 
Notes these files must be in the same folder. 

To run the test file, enter this argument into the terminal. 
python -m unittest test_script.py, or run a py test extension on the file. 

Some tests cases includes
Possible - seeing if a value of 1 would produce the correct result, handling the case of an empty string or when k is set to 0.
Observed - seeing if a value of 9 would produce the correct result, handling the case of an empty string, when values are negative and values that are greater than the length of a given string.
DataFrame - Handling the case when a dataframe is empty, thus raising a value error.
Linguistic- Raising a value error when k is equal to 0. 
