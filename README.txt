Grade Extractor – Combined Report with Logging
==============================================

This script processes multiple student grade HTML files and compiles all valid student data into a single Excel file, while generating a log report of processed records.

Features:
- Extracts student name, course codes, and grades.
- Keeps only the highest passing grade (≤ 3.00) per subject.
- Combines all students into one Excel file.
- Generates a log file (log.txt) that summarizes each student's record.

Folder Structure:
-----------------
📂 Raw HTML/             → Place all student HTML files here  
📄 Grade Extractor Group.py

Requirements:
-------------
- Python 3.7+
- Packages:
  beautifulsoup4, pandas, openpyxl

Install via pip:
----------------
pip install beautifulsoup4 pandas openpyxl

How to Use:
-----------
1. Open Grade Extractor Group.py.
2. Edit the paths in the main() function:
   input_folder = r"C:\Path\To\Raw HTML"
   output_excel = r"C:\Path\To\Combined_Grades.xlsx"
   output_log = r"C:\Path\To\log.txt"
3. Run the script:
   python Grade Extractor Group.py

Output Files:
-------------
Combined_Grades.xlsx
| Student Name                  | PHAR_1 | GEC-RPH | PHAR_CHEM_1 | ... |
|-------------------------------|--------|---------|--------------|-----|
| MAGBOO_MARK_CHRISTIAN_DENOYO | 1.75   | 2.00    | 2.25         | ... |

log.txt
Grade Extraction Log
====================
MAGBOO_MARK_CHRISTIAN_DENOYO: ✅ 58 passing grades out of 64 subjects.
JUAN_DELA_CRUZ: ❌ No passing grades found in 6 subjects.

License:
--------
MIT License
