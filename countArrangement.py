import numpy as np

class Solution:

    def __init__(self):
        self.counter = 0

    def compute(self, visited, position, n):
        if position > n:
            self.counter = self.counter + 1
        for i in range(1, n+1):
            if (visited[i] == False and (position % i == 0 or i % position == 0)):
                visited[i] = True
                self.compute(visited, position + 1, n)
                visited[i] = False

    def countArrangement(self, n: int) -> int:
        visited = [False] * (n+1)
        self.compute(visited, 1, n)
        return self.counter


if __name__ == "__main__":
    sol = Solution()

    print(sol.countArrangement(2))
