def multi_bracket_validation(input):
    Round_Brackets = 0
    Square_Brackets = 0
    Curly_Brackets = 0
    for ch in input:
        if ch == "[":
            Square_Brackets += 1
        elif ch == "]":
            Square_Brackets -= 1
        if ch == "{":
            Curly_Brackets += 1
        elif ch == "}":
            Curly_Brackets -= 1
        if ch == "(":
            Round_Brackets += 1
        elif ch == ")":
            Round_Brackets -= 1
    if Round_Brackets == 0 and Square_Brackets == 0 and Curly_Brackets == 0:
        return True
    else:
        return False
