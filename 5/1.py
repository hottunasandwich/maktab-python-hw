from functools import total_ordering



@total_ordering
class Mylist(list):
    def __eq__(self, other):
        return (sum(self) / len(self)) == (sum(other) / len(other))

    def __lt__(self, other):
        return (sum(self) / len(self)) < (sum(other) / len(other))


# li = MyList([1, 2, 3, 4, 5])

# li2 = MyList([1, 1, 1, 1])


li = [[1, 2], [2.1, 5.4, 3], [1, 4], [100, 100, 100], [90, 90, 90, 90, 90], [0, 100, 100]] 
li = [Mylist(item) for item in li] 
print(sorted(li))


class Mylist2(list):

    def __eq__(self, other):
        return Mylist.__eq__(self, other)

    def __ne__(self, other):
        return sum(self) / len(self) != sum(other) / len(other)

    def __lt__(self, other):
        return Mylist.__lt__(self, other)

    def __le__(self, other):
        return sum(self) / len(self) <= sum(other) / len(other)

    def __gt__(self, other):
        return sum(self) / len(self) > sum(other) / len(other)

    def __ge__(self, other):
        return sum(self) / len(self) >= sum(other) / len(other)


l1 = Mylist2([0, 100, 100]) #66.66666666666667
l2 = Mylist2([101, 0]) #50.5
l3 = Mylist2([100, 0, 100]) #66.66666666666667
print('1:', l1 < l2) #66.66666666666667 < #50.5
print('2:', l1 > l2)
print('4:', l1 <= l2) 
print('5:', l1 >= l2) 
print('6:', l1 == l3)
print('7:', l1 != l3) 
print(sorted(Mylist(x) for x in [l1, l2, l3]))
