"""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

 

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s
Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d
 

Constraints:

1 <= word1.length, word2.length <= 100
word1 and word2 consist of lowercase English letters.
"""

def merge_strings(word1: str, word2: str) -> str:
    
    # return word2 if word1 is empty.
    if word1 == '':
        return word2
    
    # return word1 if word2 is empty.
    if word2 == '':
        return word1
    
    length_word1 = len(word1)
    length_word2 = len(word2)
    
    total_characters = length_word1 + length_word2
    merged_characters = [''] * total_characters
    
    alternate_characters_count = min(length_word1, length_word2)
    
    start = 0
    
    for i in range(alternate_characters_count):
        
        # merge first word chars
        merged_characters[start] = word1[i]
        start +=1
        
        # merge second word chars
        merged_characters[start] = word2[i]
        start +=1
    
    # Copy remaining chars from word1
    for i in range(alternate_characters_count, length_word1):
        merged_characters[start] = word1[i]
        start +=1
        
    # Copy remaining chars from word1    
    for i in range(alternate_characters_count, length_word2):
        merged_characters[start] = word2[i]
        start +=1    
        
    return ''.join(merged_characters)        

    
def main():
    test_cases = [
        {"input1":"abcd","input2":"pq","expected":"apbqcd"},
        {"input1":"ab","input2":"pqrs","expected":"apbqrs"},
        {"input1":"abc","input2":"pqr","expected":"apbqcr"}, 
    ]
    
    for test_case in test_cases:
        result = merge_strings(test_case['input1'], test_case['input2'])
        status = result == test_case['expected']
        print(f"{test_case['input1']} {test_case['input2']} {result} {status}")
        
if __name__ == '__main__':
    main()