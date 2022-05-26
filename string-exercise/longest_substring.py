"""
Given a string s, find the length of the longest substring without repeating characters.
Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""

def get_length_of_longest_substring(s: str) -> int:
    """
    The function takes a string and returns the length of the longest substring without repeating characters.
    :param s: string
    :return: length of the longest substring without repeating characters
    """
    # return 0 if string is empty.
    if len(s) < 1:
            return 0
    # Hold number of times element appeared in array.
    element_occurances = {}
    # Hold Previous character
    previous_character = ''
    
    # Loop over all characters in the string to find the duplicate character.
    for char in s:
        # Append char to previous character when different from previous character.
        if char not in previous_character:
            previous_character += char
        # Update value of previous character.
        else:
             index = previous_character.index(char)
             if len(previous_character) > index+1:
                previous_character = previous_character[index+1:] + char
             else:
                previous_character =  char

        # Add the substring to the dictionary with number of characters as value. 
        element_occurances.update({previous_character:len(previous_character)})
    
    # find the length longest substring in the dictionary.  
    max_occurances = max(element_occurances.values())    
    # print(element_occurances)
    # return maximum length of the substring.
    return max_occurances


def main():
    print(get_length_of_longest_substring("ababd"))

if __name__ == '__main__':
    main()