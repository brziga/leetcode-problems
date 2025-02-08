# https://leetcode.com/problems/design-a-number-container-system/

from sortedcontainers import SortedDict

class NumberContainers:

    def __init__(self):
        self.ind2num = {}
        self.num2ind = {}

    def change(self, index: int, number: int) -> None:
        if index in self.ind2num:
            old_number = self.ind2num[index]
            if old_number in self.num2ind:
                self.num2ind[old_number].pop(index, None)
                if not self.num2ind[old_number]:
                    del self.num2ind[old_number]

        self.ind2num[index] = number

        if number not in self.num2ind:
            self.num2ind[number] = SortedDict()
        self.num2ind[number][index] = None

    def find(self, number: int) -> int:
        return next(iter(self.num2ind[number]), -1) if number in self.num2ind else -1

        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)