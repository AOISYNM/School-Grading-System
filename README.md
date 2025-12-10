# School Grading System

A Python-based student grading system that calculates grades, GPA, percentages, and generates comprehensive reports with visualizations.

## Features

- Calculate total marks, percentage, and average for each student
- Assign letter grades (A+, A, B+, B, C+, C, F) based on percentage
- Calculate GPA on a 4.0 scale
- Determine pass/fail status
- Generate visualizations (grade distribution, subject performance, etc.)
- Export results to Excel with multiple sheets

## Technologies Used

- **NumPy**: Data manipulation
- **Pandas**: Data processing and analysis
- **Matplotlib**: Data visualization
- **openpyxl**: Excel file generation

## Installation
```bash
pip install pandas numpy matplotlib openpyxl
```

## Usage

1. Create `students_data.csv` with student information
2. Run the program:
```bash
python main.py
```
3. Check outputs: `grading_analysis.png` and `final_report.xlsx`

## Input Format

CSV file with columns: `student_id`, `name`, `math`, `physics`, `chemistry`, `english`, `computer`

## Output

- **grading_analysis.png**: Visual charts of class performance
- **final_report.xlsx**: Detailed Excel report with multiple sheets

## Author

PUNJAN