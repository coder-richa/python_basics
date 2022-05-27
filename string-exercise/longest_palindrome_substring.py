""" 
Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 
"""

from operator import sub
from turtle import position


def get_longest_palindrome_substring(s: str) -> str:
    """
    The function takes a string and returns the longest palindrome substring.
    :param s: string .
    :return: the longest substring equal to its reverse.
    """
    # return empty string if the string is empty.
    if not s:
        return ''
    
    # return the string if it is a single character.
    if s == s[::-1]:
        return s
    
    # Pick the first character as the center of the palindrome. 
    start = 0
    max_palindrome_length = 1
    
    # Loop to find the longest palindrome. 
    for current_position in range(1,len(s)):
        
        # Check if the current position and maximum palindrome length differ by odd number.
        if current_position - max_palindrome_length - 1 >= 0:
            
            # Check substring from 1 element before max substring length to the scurrent position.
            substring = s[current_position-max_palindrome_length-1:current_position+1]
            
            # if the substring is equal to its reverse, then update the maximum length substring.
            if substring == substring[::-1]:
                start = current_position - max_palindrome_length - 1
                max_palindrome_length += 2
                continue
        
        # Check if the current position and maximum palindrome length differ by odd number.
        if current_position-max_palindrome_length >=0:
            
            # Check substring from element before max substring length to the current element.
            substring = s[current_position-max_palindrome_length:current_position+1]
                    
            # if the substring is equal to its reverse, then update the maximum length substring.        
            if substring == substring[::-1]:
                start = current_position - max_palindrome_length
                max_palindrome_length += 1
    
    # return the substring from the start index to the maximum length. 
    return s[start:start + max_palindrome_length]


def main():
    print(get_longest_palindrome_substring("cbbd"))

if __name__ == '__main__':
    main()