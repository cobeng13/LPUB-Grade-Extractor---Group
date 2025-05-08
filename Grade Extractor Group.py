import os
from bs4 import BeautifulSoup
import pandas as pd

def extract_student_data(html_path):
    with open(html_path, encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")

    # Extract student name
    student_tag = soup.find("span", id="spnStudentName")
    student_name = student_tag.get_text(strip=True).replace(",", "").replace(" ", "_") if student_tag else "Unknown_Student"

    # Extract course codes and grades
    grade_table = soup.find("table", class_="user_data")
    grades_dict = {}
    original_count = 0
    passing_count = 0

    if grade_table:
        for row in grade_table.find_all("tr"):
            cells = row.find_all("td")
            if len(cells) >= 2:
                code = cells[0].text.strip()
                grade_raw = cells[1].text.strip()

                if not code or "GWA" in grade_raw or code.lower().startswith("total"):
                    continue

                original_count += 1

                try:
                    grade = float(grade_raw)
                except ValueError:
                    continue  # Skip non-numeric grades like INC, OD, etc.

                # Keep only best passing grade (≤ 3.00)
                if grade <= 3.00:
                    passing_count += 1
                    if code not in grades_dict or grade < grades_dict[code]:
                        grades_dict[code] = grade

    grades_dict["Student Name"] = student_name
    return student_name, grades_dict, original_count, passing_count

def process_and_combine(folder_path, output_file, log_file):
    combined_records = []
    log_entries = []

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".html"):
            html_path = os.path.join(folder_path, filename)
            student_name, grades_dict, total_subjects, passed_subjects = extract_student_data(html_path)

            if passed_subjects == 0:
                log_entries.append(f"{student_name}: ❌ No passing grades found in {total_subjects} subjects.")
            else:
                log_entries.append(f"{student_name}: ✅ {passed_subjects} passing grades out of {total_subjects} subjects.")
                combined_records.append(grades_dict)

    if combined_records:
        df = pd.DataFrame(combined_records)
        df = df.set_index("Student Name")
        df.to_excel(output_file)
        print(f"📘 Combined Excel saved as: {output_file}")
    else:
        print("⚠️ No valid student records to write.")

    # Write log file
    with open(log_file, "w", encoding="utf-8") as log:
        log.write("Grade Extraction Log\n====================\n\n")
        for entry in log_entries:
            log.write(entry + "\n")
    print(f"📝 Log saved to: {log_file}")

def main():
    # ✏️ EDIT THESE PATHS
    input_folder = r"C:\Users\aaron\Desktop\Grade Extractor\Raw HTML"
    output_excel = r"C:\Users\aaron\Desktop\Grade Extractor\Combined_Grades.xlsx"
    output_log = r"C:\Users\aaron\Desktop\Grade Extractor\log.txt"

    process_and_combine(input_folder, output_excel, output_log)

if __name__ == "__main__":
    main()
