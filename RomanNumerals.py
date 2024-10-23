

def from_roman_numeral(roman_numerals):
    output = 0
    mydict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    for i in range(len(roman_numerals)):

        n1 = mydict[roman_numerals[i]]

        if len(roman_numerals) == 1:
            output = n1
            return output

        while i < len(roman_numerals) - 1:
            n2 = mydict[roman_numerals[i + 1]]

            if n1 < n2:
                output += n2 - n1
                break
            else:
                output += n2 + n1
                break

    return output


print(from_roman_numeral("M"))
