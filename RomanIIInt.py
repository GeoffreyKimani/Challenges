"""
Code challenge @ Leetcode(https://leetcode.com/problems/roman-to-integer/)

Description:
    Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
            Symbol       Value
            I             1
            V             5
            X             10
            L             50
            C             100
            D             500
            M             1000

    Key;
    -> Roman numerals are usually written largest to smallest from left to right.
    Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII.
     Instead, the number four is written as IV. Because the one is before the five we subtract it making four.
     The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is
     used.


 Task:
    Write a program s.t given a roman numeral, convert it to an integer.
"""


class RomanToInt:
    def convertor(self, roman):
        """
        function will receive a roman number and return an integer

        cases;
            I: The roman number is simple and follows the rule ... Large to small
            II. The roman number contains letters ordered like a IV i.e. simple rule
            does not apply conventionally

        :param roman:
        :return: int
        """

        # define a mapping of letter to value
        rom_dict = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }

        # convert the received roman to the same case
        roman = roman.upper()

        # read left to right sequentially
        # create a value list from the returned
        rom_vals = []
        num = 0

        for i in range(len(roman)):
            # is letter recognized in roman alphabet
            if roman[i] in rom_dict:
                # create a value list
                rom_vals.append(rom_dict[roman[i]])
            else:
                raise ValueError

        # print(f'{roman}: {rom_vals}')

        """
        Go through the list as a whole
        do operations on numbers -- (pairs) that are 'unconventional' first

        After resolving those do normal operation next with assumption large to small even if this might not be true
        We are confident since this was already resolved.
        """

        if len(rom_vals) == 1:
            return rom_vals[0]

        i = 0
        while i < len(rom_vals)-1:
            # print(f'\ni:{i} with {rom_vals}')

            # check if a pair of values break the
            # Largest to the smallest conventional rule
            if rom_vals[i] < rom_vals[i + 1]:
                num = rom_vals[i + 1] - rom_vals[i]

                # remove those numbers from the list
                # print(f'Resolved {rom_vals[i]}, {rom_vals[i + 1]} to {num}')
                del rom_vals[i:i + 1 + 1]

                # add the resolved number at the correct position
                rom_vals.insert(i, num)
                # print(f'New roman {rom_vals}')

            i += 1

        # sum the numbers
        result = sum(rom_vals)
        print(f'{roman}: {result}')
        return result


conv = RomanToInt()
conv.convertor("i")
conv.convertor("ii")
conv.convertor("iii")
conv.convertor("v")
conv.convertor("vi")
conv.convertor("iX")
conv.convertor("xiv")
conv.convertor("xXiv")
conv.convertor("MCMXCIV")
