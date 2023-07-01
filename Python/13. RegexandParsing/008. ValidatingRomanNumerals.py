

regex_pattern = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"

import re
print(str(bool(re.match(regex_pattern, input()))))


#^: Start of the string.
# (M{0,3}): Matches 0 to 3 "M"s.
# (CM|CD|D?C{0,3}): Matches "CM", "CD", or "D" followed by 0 to 3 "C"s.
# (XC|XL|L?X{0,3}): Matches "XC", "XL", or "L" followed by 0 to 3 "X"s.
# (IX|IV|V?I{0,3}): Matches "IX", "IV", or "V" followed by 0 to 3 "I"s.
# $: End of the string.

#Guildlines:
#1. The number 1 is represented by the letter "I", and it is the smallest Roman numeral. 
#2. The letters "V", "L", and "D" cannot be repeated, and they have values of 5, 50, and 500 respectively. 
#3. The letters "I", "X", and "C" can be repeated up to three times in a row. When a letter is repeated, its value is added to itself. For example, "III" represents the number 3, and "XX" represents the number 20. 
#4. If a smaller letter appears before a larger letter, the smaller letter is subtracted from the larger letter. For example, "IV" represents the number 4 (5 - 1), and "IX" represents the number 9 (10 - 1). 
#5. If a smaller letter appears after a larger letter, the smaller letter is added to the larger letter. For example, "VI" represents the number 6 (5 + 1), and "XI" represents the number 11 (10 + 1). #6. The letters "I", "X", and "C" can be used to represent values that are one less than the following larger letter. For example, "IV" represents 4, "IX" represents 9, "XL" represents 40, and "XC" represents 90. 
#7. The letters "I", "X", and "C" can be used to represent values that are one more than the preceding smaller letter. For example, "VI" represents 6, "XI" represents 11, "LX" represents 60, and "CX" represents 110. 
#8. The maximum value of a Roman numeral is 3999, which is represented by the letters "MMMCMXCIX".