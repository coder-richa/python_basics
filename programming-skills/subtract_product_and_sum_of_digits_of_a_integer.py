""" 
Given an integer number n, return the difference between the product of its digits and the sum of its digits.
 

Example 1:

Input: n = 234
Output: 15 
Explanation: 
Product of digits = 2 * 3 * 4 = 24 
Sum of digits = 2 + 3 + 4 = 9 
Result = 24 - 9 = 15
Example 2:

Input: n = 4421
Output: 21
Explanation: 
Product of digits = 4 * 4 * 2 * 1 = 32 
Sum of digits = 4 + 4 + 2 + 1 = 11 
Result = 32 - 11 = 21
 

Constraints:

1 <= n <= 10^5
"""

def difference_between_product_and_sum_of_digits(number:int) -> int:
    if number < 1:
        return 0
    
    # Holds sum and product of digits.
    sum = 0 
    product = 1
    
    # get digits of a number.
    while number > 0:
        rem  = number % 10
        number = number // 10
        sum += rem
        product *= rem
    
    # return difference
    return product - sum

def main():
    print(difference_between_product_and_sum_of_digits(4421))
    
if __name__ == "__main__":
    main()     