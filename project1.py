"""
Simple ETL Pipeline
Author: Uche Ohajuru
Date: 2025-11-17
"""
import csv
data = []
user_id = 0
def set_file():
    '''This is function helps you set up your CSV file with the right headers.
    '''
    header_row = ['Id', 'Name', 'Age', 'Colour']
    with open ("record.csv", "w", newline = "") as file:
        Writer = csv.writer(file)
        Writer.writerow(header_row)     
    return 'file created successfully'
def get_data():
    """This function should allow you get data from the user and 
    append it to the list as a list of lists"""
    user_name = input('Enter your name: ')
    user_age = input('Enter your age: ')
    user_colour = input("Enter your favourite colour: ")
    global user_id
    user_id +=1
    global data
    data.append(user_id)
    data.append(user_name)
    data.append(user_age)
    data.append(user_colour)
    return data


def load_data():
    """Load data to destination using the append mode."""
    with open ('record.csv', 'a', newline = "") as file:
        writer = csv.writer(file)
        writer.writerow(data)
    print("Data loaded successfully!")

def main():
    # ETL process
    set_file()
    get_data()
    load_data()
        

if __name__ == "__main__":
    main()

# get_data()
# print(data)