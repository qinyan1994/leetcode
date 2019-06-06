class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        result = 0
        str_in = str.lstrip()
        if str_in in ['', '-', '+']:
            return result
        if str_in[0] in ['-', '+']:
            if str_in[1].isdigit():
                for i in range(2, len(str_in) + 1):
                    if i == len(str_in):
                        result = int(str_in[:i])
                    else:
                        if not str_in[i].isdigit():
                            result = int(str_in[:i])
                            break
                    i += 1
        elif str_in[0].isdigit():
            for i in range(1, len(str_in) + 1):
                if i == len(str_in):
                    result = int(str_in[:i])
                else:
                    if not str_in[i].isdigit():
                        result = int(str_in[:i])
                        break
                i += 1
        if int(result) < -2 ** 31:
            return -2 ** 31
        elif int(result) > 2 ** 31 - 1:
            return 2 ** 31 - 1
        return result