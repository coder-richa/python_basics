"""
Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).

 

Example 1:

Input: low = 3, high = 7
Output: 3
Explanation: The odd numbers between 3 and 7 are [3,5,7].
Example 2:

Input: low = 8, high = 10
Output: 1
Explanation: The odd numbers between 8 and 10 are [9].
"""

def is_odd(number: int) -> bool:
    return number % 2 != 0

def count_odd_numbers_in_range(low: int, high: int) -> int:
    """
    Count the number of odd numbers between low and high (inclusive) .
    :param low: Lowest number in range.
    :param high: Highest number in range.
    """
    
    #  check if low is greater than high.
    if low > high:
        return 0
     
    start = low
    
    if not is_odd(start):
        start +=1
    
    if not is_odd(high):
        high -=1
    
    # Calculate the number of odd numbers between low and high.
    number_of_odds = ((high - start) // 2) + 1
    
    return number_of_odds

def main():
    print(count_odd_numbers_in_range(8,10))
    

if __name__ == '__main__':
    main()
    