import pandas as pd

df = pd.read_csv("students.csv")

df ["Total"] = df["Math"] + df["Physics"] + df["Chemistry"]

df ["Average"] = df["Total"] / 3

def get_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"

df ["Grade"] = df["Average"].apply(get_grade)

df ["Status"] = df ["Average"].apply(lambda x: "Pass" if x >= 40 else "Fail")

print("\n---Student Performance---")
print(df)

print("\n---Student Averages---")
print(df[["Name", "Average"]].sort_values("Average", ascending=False))

print("\n---Subject Averages---")
print("Math", df["Math"].mean())
print("Physics", df["Physics"].mean())
print("Chemistry", df["Chemistry"].mean())

print("\n---Highest Marks---")
print("Math", df["Math"].max())
print("Physics", df["Physics"].max())
print("Chemistry", df["Chemistry"].max())

print("\n---Lowest Marks---")
print("Math", df["Math"].min())
print("Physics", df["Physics"].min())
print("Chemistry", df["Chemistry"].min())

top_student = df.loc[df["Average"].idxmax()]

print("\n---Top Student---")
print("Name", top_student["Name"])
print("Average", round(top_student["Average"], 2))
print("Grade", top_student["Grade"])

print("\n---Grades---")
print(df["Grade"].value_counts())

print("\n---Pass/Fail---")
print(df["Status"].value_counts)

df.to_csv("Student_Performance_Result.csv", index = False)

print("Analysis Compleated")
print("Results saved to Student_Performance_result.csv")