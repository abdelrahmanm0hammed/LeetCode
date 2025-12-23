def roman_to_integer(roman_num):
    char = list(roman_num)
    result = 0
    i = 0

    while i < len(char):
        if char[i] == "I":
            if i + 1 < len(char):
                if char[i + 1] == "V":
                    result += 4
                    i += 2
                elif char[i + 1] == "X":
                    result += 9
                    i += 2
                else:
                    result += 1
                    i += 1
            else:
                result += 1
                i += 1

        elif char[i] == "V":
            result += 5
            i += 1

        elif char[i] == "X":
            if i + 1 < len(char):
                if char[i + 1] == "L":
                    result += 40
                    i += 2
                elif char[i + 1] == "C":
                    result += 90
                    i += 2
                else:
                    result += 10
                    i += 1
            else:
                result += 10
                i += 1

        elif char[i] == "C":
            if i + 1 < len(char):
                if char[i + 1] == "D":
                    result += 400
                    i += 2
                elif char[i + 1] == "M":
                    result += 900
                    i += 2
                else:
                    result += 100
                    i += 1
            else:
                result += 100
                i += 1

        elif char[i] == "D":
            result += 500
            i += 1

        else:  # M
            result += 1000
            i += 1

    return result

print(roman_to_integer("IVVI"))