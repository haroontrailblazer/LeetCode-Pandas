
"""

1527. Patients With a Condition
Solved
Easy
Topics
Companies
SQL Schema
Pandas Schema
Table: Patients

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| patient_id   | int     |
| patient_name | varchar |
| conditions   | varchar |
+--------------+---------+
patient_id is the primary key (column with unique values) for this table.
'conditions' contains 0 or more code separated by spaces. 
This table contains information of the patients in the hospital.
 

Write a solution to find the patient_id, patient_name, and conditions of the patients who have Type I Diabetes. Type I Diabetes always starts with DIAB1 prefix.

Return the result table in any order.

The result format is in the following example.

 

Example 1:

Input: 
Patients table:
+------------+--------------+--------------+
| patient_id | patient_name | conditions   |
+------------+--------------+--------------+
| 1          | Daniel       | YFEV COUGH   |
| 2          | Alice        |              |
| 3          | Bob          | DIAB100 MYOP |
| 4          | George       | ACNE DIAB100 |
| 5          | Alain        | DIAB201      |
+------------+--------------+--------------+
Output: 
+------------+--------------+--------------+
| patient_id | patient_name | conditions   |
+------------+--------------+--------------+
| 3          | Bob          | DIAB100 MYOP |
| 4          | George       | ACNE DIAB100 | 
+------------+--------------+--------------+
Explanation: Bob and George both have a condition that starts with DIAB1.


"""


import pandas as pd

def find_conditions(patients):
    df = pd.DataFrame(patients, columns=['patient_id', 'name', 'condition'])
    return df[df['condition'].str.split().explode().str.startswith('DIAB1').groupby(level=0).any()]

patients = [[1,'Daniel','YFEV COUGH'],
            [2,'Alice',''],
            [3,'Bob','DIAB100'],
            [4,'George','ACNE DIAB100'],
            [5,'Alian','DIAB201']]


print(find_conditions(patients))