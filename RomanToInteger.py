def romanToInteger(roman: str) -> int:
    """
    -- Return integer equivalent of a valid Roman Numeral
    -- Roman Numeral must be valid, it does not check the validity of Roman Numeral

    """

    roman_mapping = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    num = 0
    i = 0
    
    while i < len(roman) - 1:
        flag = False
        
        if roman[i] == 'I':
            if roman[i+1] in ['X', 'V']:
                flag = True
        elif roman[i] == 'X':
            if roman[i+1] in ['L', 'C']:
                flag = True
        elif roman[i] == 'C':
            if roman[i+1] in ['D', 'M']:
                flag = True
        
        if flag:
            num = num + roman_mapping[roman[i+1]] - roman_mapping[roman[i]]
            i = i + 1
        else:
            num = num + roman_mapping[roman[i]]
        
        i = i + 1

    if i == len(roman) - 1:
        num = num + roman_mapping[roman[i]]
    
    return num

if __name__ == '__main__':

    print('Enter a valid Roman Numeral:')
    roman = input()
    
    resInt = romanToInteger(roman)

    print('The integer equivalent is:')
    print(resInt)