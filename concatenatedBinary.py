class Solution:
    def concatenatedBinary(self, n: int) -> int:
        binary_string = ""
        for i in range (1,n+1):
            binary_string = binary_string + str(bin(i)[2:])
        decimal_value = int(binary_string,2)
        return decimal_value%(10**9+7)