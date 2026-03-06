class FlatIterator:
    def __init__(self, list_of_list):
        self.cursor1 = -1
        self.longlist =[]
        self.list_of_list = list_of_list
        for _ in range(len(self.list_of_list)):
            self.cursor1 += 1
            self.longlist.extend(self.list_of_list[_])


    def __iter__(self):
        self.cursor = -1
        return self

    def __next__(self):
        self.cursor += 1
        if len(self.longlist) == self.cursor:
            raise StopIteration
        item = self.longlist[self.cursor]
        return item


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):


        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()