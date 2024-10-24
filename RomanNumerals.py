

def from_roman_numeral(roman_numerals):
    i = 0
    output = 0
    mydict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    while i < len(roman_numerals):

        n1 = mydict[roman_numerals[i]]

        if i + 1 < len(roman_numerals):

            n2 = mydict[roman_numerals[i + 1]]

            if n1 < n2:
                output += n2 - n1
                i += 2
            else:
                output += n1
                i += 1
        else:
            output += n1
            i += 1

    return output


print(from_roman_numeral("MMMMM"))
