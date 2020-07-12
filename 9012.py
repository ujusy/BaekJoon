T = int(input())
for i in range(T):
    stack = list(input())
    while len(stack):
        if stack[0] == ')':
            print("NO")
            break
        else:
            if ')' in stack:
                stack.remove(')')
                stack.remove('(')
            else:
                print("NO")
                break
    if len(stack) == 0:
        print("YES")