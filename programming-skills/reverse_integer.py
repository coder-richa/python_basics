""" 
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 

Constraints:

-231 <= x <= 231 - 1
"""

def reverse(x: int) -> int:
    # Check  if given number is negative. 
    is_negative = x < 0
    
    # reverse number.
    if is_negative:
        number = -1 * int(str((-x))[-1::-1])
    else:
        number = int(str((x))[-1::-1])
    
    # Check if reverse is 32-bit integer. 
    if not -2**31 <= number <= 2**31 -1:
        return 0
    # return reversed number.
    return number


def main():
    print(reverse(123))
    
if __name__ == "__main__":
    main()