

def roman_to_integer(roman_num):
    result = 0
    i = 0

    while i < len(roman_num):
        if roman_num[i] == "I":
            if i + 1 < len(roman_num) and roman_num[i+1] == "V":
                result += 4
                i += 2
            elif i + 1 < len(roman_num) and roman_num[i+1] == "X":
                result += 9
                i += 2
            else:
                result += 1
                i += 1

        elif roman_num[i] == "V":
            result += 5
            i += 1

        elif roman_num[i] == "X":
            if i + 1 < len(roman_num) and roman_num[i+1] == "L":
                result += 40
                i += 2
            elif i + 1 < len(roman_num) and roman_num[i+1] == "C":
                result += 90
                i += 2
            else:
                result += 10
                i += 1

        elif roman_num[i] == "C":
            if i + 1 < len(roman_num) and roman_num[i+1] == "D":
                result += 400
                i += 2
            elif i + 1 < len(roman_num) and roman_num[i+1] == "M":
                result += 900
                i += 2
            else:
                result += 100
                i += 1

        elif roman_num[i] == "D":
            result += 500
            i += 1

        else:  # M
            result += 1000
            i += 1

    return result
