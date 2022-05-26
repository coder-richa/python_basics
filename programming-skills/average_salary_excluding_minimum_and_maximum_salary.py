from typing import List
"""
You are given an array of unique integers salary where salary[i] is the salary of the ith employee.

Return the average salary of employees excluding the minimum and maximum salary. Answers within 10-5 of the actual answer will be accepted.
 

Example 1:

Input: salary = [4000,3000,1000,2000]
Output: 2500.00000
Explanation: Minimum salary and maximum salary are 1000 and 4000 respectively.
Average salary excluding minimum and maximum salary is (2000+3000) / 2 = 2500
Example 2:

Input: salary = [1000,2000,3000]
Output: 2000.00000
Explanation: Minimum salary and maximum salary are 1000 and 3000 respectively.
Average salary excluding minimum and maximum salary is (2000) / 1 = 2000
"""

def average(salary: List[int]) -> float:
    if len(salary) < 3:
        return 0
    salary.sort()
    salaries_excluding_min_max = salary[1:-1]
    average_salary = sum(salaries_excluding_min_max) / len(salaries_excluding_min_max)
    return average_salary


def main():
    print(average([4000,3000,1000,2000]))
    

if __name__ == '__main__':
    main()
    