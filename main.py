# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    stack = []
    index=0
    for i, next in enumerate(text):
        if next in "([{":
            stack.append(next)
            if len(stack)<2:
                index=Bracket(next,i+1).position
            pass

        if next in ")]}":
            if len(stack)==0:
                return Bracket(next,i+1).position
            stackpop=stack.pop()
            if not are_matching(stackpop,next):
                return Bracket(next,i+1).position
            pass
    if len(stack)==0:
        return "Success"
    else:return index

def main():
    
        text = input()
        mismatch = find_mismatch(text)
        print(mismatch)
    
    


if __name__ == "__main__":
    main()
