#221RDB190 Daniels Tumans
from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]

def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i+1))

        if next in ")]}":
            if not opening_brackets_stack:
                return i+1
        
            pop = opening_brackets_stack.pop()
            if not are_matching(pop.char, next):
                return i+1
          
        if opening_brackets_stack:
            return opening_brackets_stack[0].position
        return "Success"


def main():
    select_input = input("input - F or I")
    if select_input.upper() == "F":
        file_path = input("choose file (input path)")
        with open(file_path, "r") as f:
            text = f.read()
            mismatch = find_mismatch(text)
            if mismatch == None:
                print("Success")
            else:
                print(mismatch)
    else:
        text = input()
        mismatch = find_mismatch(text)
        if mismatch == None:
            print("Success")
        else:
            print(mismatch)


if __name__ == "__main__":
    main()
