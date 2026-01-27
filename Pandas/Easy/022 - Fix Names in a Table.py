"""


1667. Fix Names in a Table
Solved
Easy
Topicss
SQL Schema
Pandas Schema
Table: Users

+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| user_id        | int     |
| name           | varchar |
+----------------+---------+
user_id is the primary key (column with unique values) for this table.
This table contains the ID and the name of the user. The name consists of only lowercase and uppercase characters.
 

Write a solution to fix the names so that only the first character is uppercase and the rest are lowercase.

Return the result table ordered by user_id.

The result format is in the following example.

 

Example 1:

Input: 
Users table:
+---------+-------+
| user_id | name  |
+---------+-------+
| 1       | aLice |
| 2       | bOB   |
+---------+-------+
Output: 
+---------+-------+
| user_id | name  |
+---------+-------+
| 1       | Alice |
| 2       | Bob   |
+---------+-------+

"""

import pandas as pd

def fix_names(users):
    df = pd.DataFrame(users, columns = ['user_id','name'])
    df['name']=(df['name'].str.lower())
    df['name']=(df['name'].str.capitalize())
    return df.sort_values('user_id')

users = [[1,'aLice'],
         [2,'boB']]


fix_names(users)