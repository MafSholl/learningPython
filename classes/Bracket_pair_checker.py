
def bracket_pair_checker(brackets: str) -> bool:
    stack: list[str] = []
    for bracket in brackets:
        if bracket in "({[":
            stack.append(bracket)
        if bracket in ")}]":
            peep = stack[-1]
            if bracket == ")" and peep == "(":
                stack.pop()
            elif bracket == "}" and peep == "{":
                stack.pop()
            elif bracket == "]" and peep == "[":
                stack.pop()
            else:
                return False
    return len(stack) == 0

print(bracket_pair_checker('(){}{[]()'))
