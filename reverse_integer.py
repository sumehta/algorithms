class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        str_x = str(x)
        sign = ''
        if str_x[0] == '-'
        	sign='-'
        	str_x = str_x[1:]

        res = int(isign+str_x[::-1])
        if res.bit_length() > 32:
        	return 0
        else:
        	return res

