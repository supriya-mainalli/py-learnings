brackets = "{[]{()}}"

open_brackets = ["{", "(", "["]
closed_brackets = ["}", ")", "]"]

my_stack = []

for item in range(len(brackets)):

    if brackets[item] in open_brackets:
        my_stack.append(brackets[item])
        print("The stack after appending {}".format(my_stack))
    else:
        print("Stack before popping {}".format(my_stack))
        if closed_brackets.index(brackets[item]) == open_brackets.index(my_stack[-1]):
            my_stack.pop()
            print("Stack after popping {}".format(my_stack))
        else:
            break

if len(my_stack) == 0:
    print("Given input is balanced")
else:
    print("Not balanced")
