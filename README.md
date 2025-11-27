# === Tasks ===

Task 1.
Modify the code in the file named project1.py such that:
    a. Names will appear in all caps
    b. Age will be of the int data type
    c. Colour will start with a Capital letter

Task 2.
Add error handling lines of code to take care of:
    a. Non digit input for age
    b. Non alphabet input for names

Task 3.
Use appropriate control structures to control: 
    a. the number of items on the list before breaking or exiting

Task 4.
Make your team work readable using comments and docstrings.

## === How to Submit === 
1. After your work, modify this readme file to include:
    a. List of active team members
    
    The list of active team members were:
    1. Emele Onyinyechi Sussan
    2. Ebere Chukwuemeka emmanuel
    3. Kalu-Ogbonnaya Nwachinemerem Wisdom
    4. Benneth Obiageri Goodluck
    5. John Chimeremeze Destiny 
    b. Detail of work done
    The project uses an ETL process, that is, extract, transform and load process to extract data as a user input, transform the data by validating and handling errors that might be raised in the course of the data collection and then loading the data, that is, appending the data so collected and transformed into a csv file. 
    First, a file called 'record.csv' was created in append mode with headers: id, name, age, colour. This is where the data will be loaded to.  
    The data required as user input included the user name, the user age, the user favourite colour. The work was done in a way that the user id is given to each user that adds his or her data to the file.
    Some modifications that were made to the data included converting the user name to only capital letters and alphabets; age must be positive integers; colour must have its first letter capitalized; and user id must be integer and incremented by one and error messages thrown up when any error occurs in the course of inputing the data. 
    The user prompt loops up to 4 times, allowing multiple entries unless 'exit' is typed and each record is appended as a dictionary to data.

     
      
2. The team lead alone should:
    a. modify the .gitignore file to include proper ignore list
    b. add all changes
    c. commit all changes with proper message
    d. push the code to me on a branch whoes name is your team name
