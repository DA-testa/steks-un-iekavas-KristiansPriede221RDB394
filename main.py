# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
             opening_brackets_stack.append(i)
            pass

        if next in ")]}":
            # Process closing bracket, write your code here
           rigth _index= rigth.index(i)
            pass


def main():
    text = input()
    mismatch = find_mismatch(text)
    if  opening_brackets_stack and ( opening_brackets_stack[-1]==rigth[rigth_index])
     opening_brackets_stack.pop()
        else:
        return rigth_index
    if len( opening_brackets_stack)==0
    return "Success"
    # Printing answer, write your code here
    
    


if __name__ == "__main__":
    main()
