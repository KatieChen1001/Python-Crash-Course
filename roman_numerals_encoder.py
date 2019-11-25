def solution(n):
    roman_numeral_dict = {
        0: ["I", "II", "III", "IV", "V","VI","VII", "VIII", "IX"], 
        1: ["X", "XX","XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],
        2: ["C", "CC","CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"], 
        3: ["M", "MM", "MMM"]
    }
    reversed_n = ""
    for i in str(n): 
        reversed_n = i + reversed_n
    digit = 0
    roman_numerals = ""

    while digit < len(reversed_n):
        for index in range(len(roman_numeral_dict[digit])+1): 
            if str(index+1) == reversed_n[digit]:
                roman_numerals = roman_numeral_dict[digit][index] + roman_numerals
                print(roman_numerals)
                break
        digit += 1
    return roman_numerals

solution(984)


"""
#best practice
def solution(n):
    roman_numerals = {1000:'M',
                      900: 'CM',
                      500: 'D',
                      400: 'CD',
                      100: 'C',
                      90: 'XC',
                      50: 'L',
                      40: 'XL',
                      10: 'X',
                      9: 'IX',
                      5: 'V',
                      4: 'IV',
                      1: 'I'
    }
    roman_string = ''
    for key in sorted(roman_numerals.keys(),reverse=True):
        while n >= key:
            roman_string += roman_numerals[key]
            n -= key
    return roman_string

#Clever
vals = zip(('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I'),
           (1000, 900, 500,  400, 100,   90,  50,   40,  10,    9,   5,    4,   1))

def solution(n):
    if n == 0: return ""
    return next(c + solution(n-v) for c,v in vals if v <= n)
    """
