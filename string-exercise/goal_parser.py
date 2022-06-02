""" 
You own a Goal Parser that can interpret a string command. The command consists of an alphabet of "G", "()" and/or "(al)" in some order. The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al". The interpreted strings are then concatenated in the original order.

Given the string command, return the Goal Parser's interpretation of command.

 

Example 1:

Input: command = "G()(al)"
Output: "Goal"
Explanation: The Goal Parser interprets the command as follows:
G -> G
() -> o
(al) -> al
The final concatenated result is "Goal".
Example 2:

Input: command = "G()()()()(al)"
Output: "Gooooal"
Example 3:

Input: command = "(al)G(al)()()G"
Output: "alGalooG"
 

Constraints:

1 <= command.length <= 100
command consists of "G", "()", and/or "(al)" in some order.

"""

def goal_parser(command: str) -> str:
    if command == '':
        return ''
    command = command.replace('()', 'o').replace('(al)', 'al')
    return command

def main():
    test_cases = [
        {"input":"(al)G(al)()()G","expected":"alGalooG"},
        {"input":"G()()()()(al)","expected":"Gooooal"},
        {"input":"G()(al)","expected":"Goal"},
    ]
    
    for test_case in test_cases:
        result = goal_parser(test_case['input'])
        status = result == test_case['expected']
        print(f"{test_case['input']}  {result} {status}")
        
if __name__ == '__main__':
    main()