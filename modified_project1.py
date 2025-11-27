"""
Simple ETL Pipeline
Author: Uche Ohajuru
Date: 2025-11-17
"""
import csv # Import the csv module to handle CSV file reading and writing
data = []       # List that will hold multiple user records
user_id = 0     # Counter for user IDs, must be global to be incremented

"""--------------------SETUP FUNCTION---------------------"""
def set_file():
    '''This is function helps you set up your CSV file with the right headers.
    '''
    header_row = ['Id', 'Name', 'Age', 'Colour']
    # Define the header row names.
    # Open the file in 'w' (write) mode. This overwrites the file if it exists.
    # 'newline = ""' is necessary for proper CSV handling in Python.
    with open ("record.csv", "w", newline = "") as file:
        Writer = csv.writer(file)       # Create a CSV writer object.
        Writer.writerow(header_row)     # Write the header row to the file.  
    return 'File created successfully'

"""-------------------EXTRACT AND TRANSFORM FUNCTION---------------------"""
def get_data():
    """Collect user input, validate it it using try-except,
    transform values, and append the cleaned data to the global list."""

    global user_id, data  # Declare global variables to be modified inside the function.

    # Name Validation Using try-except
    while True: # Loop indefinitely until a valid name is provided.
        try: 
            user_name = input('Enter your name: ').strip() # Prompt input and remove leading/trailing whitespace.
            # Check if the name consists only of alphabetic characters (no spaces allowed by isalpha()).
            if not user_name.isalpha(): 
                raise ValueError ("Name must be alphabets") # Raise error if invalid character is found.
            # Transform name to ALL CAPS 
            user_name = user_name.upper()
            break # Exit the loop if the input is valid

        except ValueError as e:
            print(f'Invalid input: {e}') # Print error message and loop restarts.
    
    # Age Validation Using try-except
    while True: # Loop indefinitely until a valid age is provided.
        try: 
            user_age = input('Enter your age: ') # Transform name to ALL CAPS using .isalpha()
            # Check if the input consists only of digits.
            if not user_age.isdigit():
                raise ValueError ("Age must be an integer") # Raise error if non-digit character is found.
             # Transform to integer
            user_age2= int(user_age)
            break # Exit loop if input is valid

        except ValueError as e:
            print(f'Invalid input: {e}') # Print error message and loop restarts.
   
    #Colour Input and Transformation
    while True: # Loop indefinitely until a valid colour is provided.
        user_colour = input('Enter your favourite colour: ')
        # Validate that the colour consists only of alphabetic characters.
        if not user_colour.isalpha():
            print("Invalid input: Colour must be alphabets")
            continue # Restart the loop if invalid.

        # Transform: Capitalize the first letter of the colour string.
        user_colour = user_colour.capitalize()
        break # Exit loop if input is valid and transformed.

    user_id+= 1 # increment ID by 1 for the new record

    # Store record as a list of values using the transformed variable
    record = [user_id, user_name, user_age2, user_colour]
    data.append(record) # Append the record inputed to the global data list[]
    return record # Return the single record.

"""------------------- LOAD FUNCTION-------------------"""
def load_data():
    """Load(append) all user record to the csv file."""

    # Open the file in 'a' (append) mode.
    with open ('record.csv', 'a', newline = "") as file:
        writer = csv.writer(file)
        # writerows() is used to write a list of lists, making each inner list a new row.
        writer.writerows(data)
    print("Data loaded successfully!")

"""-------------- CONTROLLER FUNCTION -------------"""
def main():
    """Main ETL controller function
    Limits number of inputs and records using a control structure"""
    
    Max_input = 5    # Maximum number of records
    while True:      # Loop for collecting multiple records.
        print("Enter new record")

        get_data() # Collects inputs from user (Extract + Transform)

        #Control Structure: Check if the maximum limit has been reached.
        if len(data) >= Max_input:
            print(f"Limit reached! Only {Max_input} records allowed.")
            break # Exit the input loop.

    # Ask user if they want to continue 
        cont = input("Do you want to input another record? (yes/no): ")
        if cont != "yes":
            break # Exit the input loop if the answer is not "yes".
     
    # Load all collected records to the CSV file after the input loop breaks.
    load_data() 
        

if __name__ == "__main__":
    main() # Standard Python entry point: ensures main() runs when the script is executed directly.

# get_data()
# print(data)