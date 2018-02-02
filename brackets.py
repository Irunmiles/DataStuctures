#https://stepik.org/lesson/41234/step/1

def braces_check(line):
    stack = []
    opening_stack = []
    braces_dict = {'(':')', '[':']', '{':'}'}
    curr = 1
    for brace in line:
        if brace not in "(){}[]":
            curr += 1
            continue
        if brace in "({[":
            stack.append(brace)
            opening_stack.append(curr)
            curr += 1
        else:
            if stack == []:
                return curr
            else:
                br = stack.pop()
                if braces_dict[br] == brace:
                    opening_stack.pop()
                    curr += 1
                else:
                    return curr

    if stack == []:
        return "Success"
    else:
        return opening_stack.pop()

line = input()
print(braces_check(line))

