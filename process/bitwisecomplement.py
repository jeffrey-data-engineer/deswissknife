class Solution(object):
    def bitwiseComplement(self, N):
        """
        :type N: int
        :rtype: int
        """
        x = 1
        while x<N:
            x = 2*x+1
        return x-N

if __name__ == '__main__':
    print("hi")
    a = Solution()
    print(a.bitwiseComplement(6))
