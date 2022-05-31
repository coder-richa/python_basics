from typing import List
""" 
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
"""

def longest_common_prefix(strs: List[str]) -> str:
    # Get length of list.
    number_of_strings = len(strs)
    
    # Check if list is empty.
    if number_of_strings < 1:
        return ""
    
    # Sort the list
    strs.sort()
    common_prefix = ""
    
    # Get first and last string.
    first_string = strs[0]
    last_string = strs[-1]
    
    # Get minimum length of first and last string.
    max_chars_of_common_prefix = min(len(first_string),len(last_string))
    
    # Loop to get the common prefix.
    for index in range(0,max_chars_of_common_prefix):
        # Update common prefix if the character at index is same in all strings.
        if first_string[:index+1] == last_string[:index+1]:
            common_prefix = first_string[:index+1]
        else:
            # Return the common prefix.
            return common_prefix
    
    # No common prefix found   
    return common_prefix
    

def main():
    test_cases = {
        0:{"input":["flower","flow","flight"], "Expected":"fl"},
        1:{"input":["a"], "Expected":"a"},
        2:{"input":[], "Expected":""},
        3:{"input":["a","ab"], "Expected":"a"}
    }
    
    for test_case in test_cases:
        result = longest_common_prefix(test_cases[test_case]["input"])
        pass_status = result == test_cases[test_case]["Expected"]
        # if not pass_status:
        print(test_case, "input" , test_cases[test_case]["input"] , " Expected = ", test_cases[test_case]["Expected"], " Output = ",result,"Result", result == test_cases[test_case]["Expected"])

    
    
if __name__ == "__main__":
    main()

