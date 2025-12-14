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
    print("2. Create new file and add data manually")
    
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
#Function To Calculate Everything
def calculateGrades(df):
    subjects = ['math', 'physics', 'chemistry', 'english', 'computer']
    

    df['total_marks'] = df[subjects].sum(axis=1)
    df['percentage'] = (df['total_marks'] / 500) * 100
    df['average'] = df[subjects].mean(axis=1)


    def get_grade(pct):
        if pct >= 90: return 'A+'
        elif pct >= 80: return 'A'
        elif pct >= 70: return 'B+'
        elif pct >= 60: return 'B'
        elif pct >= 50: return 'C+'
        elif pct >= 40: return 'C'
        else: return 'F'
    
    df['grade'] = df['percentage'].apply(get_grade)

    def get_gpa(pct):
        if pct >= 90: return 4.0
        elif pct >= 80: return 3.6
        elif pct >= 70: return 3.2
        elif pct >= 60: return 2.8
        elif pct >= 50: return 2.4
        elif pct >= 40: return 2.0
        else: return 0.0
    
    df['gpa'] = df['percentage'].apply(get_gpa)

    df['status'] = df[subjects].apply(
        lambda row: 'Pass' if all(row >= 40) else 'Fail', 
        axis=1
    )
    df['rank'] = df['percentage'].rank(ascending=False, method='min').astype(int)

    # For Saving File
    import os
    filename = input("\nEnter filename to save (e.g., students.xlsx): ")
    filepath = os.path.join('Data', filename)
    
    with pd.ExcelWriter(filepath, engine='openpyxl') as writer:
        # Sheet 1: All student results
        #This is sorted according to rank
        df_output = df[[
            'rank', 'student_id', 'name', 
            'math', 'physics', 'chemistry', 'english', 'computer',
            'total_marks', 'percentage', 'average', 'grade', 'gpa', 'status'
        ]].sort_values('rank')
        
        df_output.to_excel(writer, sheet_name='All Students Data', index=False)
        
        
        # Sheet 2: Summary statistics
        summary = pd.DataFrame({
            'Metric': [
                'Total Students',
                'Students Passed',
                'Students Failed',
                'Pass Rate (%)',
                'Class Average (%)',
                'Highest Score (%)',
                'Lowest Score (%)',
                'Average GPA'
            ],
            'Value': [
                len(df),
                len(df[df['status'] == 'Pass']),
                len(df[df['status'] == 'Fail']),
                round((len(df[df['status'] == 'Pass']) / len(df)) * 100, 2),
                round(df['percentage'].mean(), 2),
                round(df['percentage'].max(), 2),
                round(df['percentage'].min(), 2),
                round(df['gpa'].mean(), 2)
            ]
        })
        summary.to_excel(writer, sheet_name='Summary', index=False)
        #Sheet 3 for failed students
        failed = df[df['status'] == 'Fail'][[
            'name', 'math', 'physics', 'chemistry', 'english', 'computer', 
            'percentage', 'status'
        ]]
        if len(failed) > 0:
            failed.to_excel(writer, sheet_name='Failed Students', index=False)
    
    return df



def generateReports():
    True
def createVisualizations():
    #This checks if images folder exists if it doesnot it creates a new one
    images_path = os.path.join('Output','Images')
    if not os.path.exists(images_path):
        os.makedirs(images_path)

def main():
    print("="*60)
    print("SCHOOL GRADING SYSTEM")
    print("="*60)

    df = dataReceiver()
    
    if df is None:
        print(" No data loaded. Exiting...")
        return
    
    print("\n" + "="*60)
    print(" Data Loaded Successfully")
    print("="*60)
    print(f"Total Students: {len(df)}")
    print("\n")

    choice = input("Do you want to proceed with calculations (y/n)? : ")
    
    if choice.lower() == 'y':
        print("\n[1] Calculating grades and statistics...")
        df = calculateGrades(df)
        print(" Calculations complete!")
        
        print("\n[2] Generating reports...")
        generateReports(df)
        print(" Reports generated!")
        
        print("\n[3] Creating visualizations...")
        createVisualizations(df)
        print(" Visualizations created!")
        
        print("\n" + "="*60)
        print(" All tasks completed successfully!")
        print("="*60)
    else:
        print("\n Program ended. Data saved!")
        print("\n  Check Your Output File For The Results")

