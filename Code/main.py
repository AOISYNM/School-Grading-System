import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


def dataReceiver ():
    print("=" * 60)
    print("STUDENT DATA RECEIVER")
    print("=" * 60)
    print("\nChoose an option:")
    print("1. Read existing file after u have uploaded it")
    print("2. Create new file and add data manually")\
    
    choice = input("\n Enter Choice (1 or 2) : ")

    if choice == '1':
        filename = input("Enter the filename (e.g., students_data.csv): ")
        filepath = os.path.join('Data', filename)
        try:
            if filename.endswith('.csv'):
                StdData = pd.read_csv(filepath)
            elif filename.endswith('.xlsx'):
                StdData = pd.read_excel(filepath)
            else:
                print(" Invalid file type! Use .csv or .xlsx")
                return None
            print(f"Loaded {len(StdData)} students from Data/{filename}")
            print("\nPreview:")
            print(StdData.head())
            return StdData
        except FileNotFoundError:
            print(f" File 'Data/{filename}' not found!")
            return None
    elif choice == '2':
    
        students = []
        num = int(input("\nHow many students to add? "))

        for i in range(num):
            print(f"\n--- Student {i+1} ---")
            student = {
                'student_id': int(input("Student ID: ")),
                'name': input("Name: "),
                'math': int(input("Math marks (0-100): ")),
                'physics': int(input("Physics marks (0-100): ")),
                'chemistry': int(input("Chemistry marks (0-100): ")),
                'english': int(input("English marks (0-100): ")),
                'computer': int(input("Computer marks (0-100): "))
            }
            students.append(student)
            print(f" {student['name']} added!")

        
        StdData = pd.DataFrame(students)

        
        filename = input("\nEnter filename to save (e.g., students.csv): ")
        filepath = os.path.join('Data', filename)
        StdData.to_csv(filepath, index=False)
        print(f" Data saved to 'Data/{filename}'")

        print("\nPreview of saved data:")
        print(StdData.head())

        return StdData

    else:
        print(" Invalid choice!")
        return None



dataReceiver()