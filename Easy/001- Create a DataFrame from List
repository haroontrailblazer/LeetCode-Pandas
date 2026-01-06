"""
Write a solution to create a DataFrame from a 2D list called student_data.
This 2D list contains the IDs and ages of some students.

The DataFrame should have two columns, student_id and age, and be in the same order
as the original 2D list.

Example:
Input:
student_data = [
    [1, 15],
    [2, 11],
    [3, 11],
    [4, 20]
]

Output:
+------------+-----+
| student_id | age |
+------------+-----+
| 1          | 15  |
| 2          | 11  |
| 3          | 11  |
| 4          | 20  |
+------------+-----+

Explanation:
A DataFrame was created on top of student_data, with two columns named student_id and age.

"""

import pandas as pd

def createDataframe(student_data):
    df = pd.DataFrame(student_data,columns=["student_id","age"])
    return df

student_data:list = [
    [1, 15],
    [2, 11],
    [3, 11],
    [4, 20]
]

print(createDataframe(student_data))
