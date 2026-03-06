# Задание 3 сделал отдельный класс для преобразования многоуровнего списка
class Parting:
    def parsing_lists1(parsing_list):
        longlist = []
        for _ in range(len(parsing_list)):
            list1 = parsing_list[_]
            while True:
                count = 0
                for i in range(len(list1)): # проверяем есть ли ещё вложенные списки
                    if isinstance(list1[i], list):
                        count += 1 # ведём подсчёт вложенных списков
                #print(count)
                list2 = []
                if count != 0: # если счётчик не нулевой, значит есть вложенные списки
                    for i in range(len(list1)):
                        if isinstance(list1[i], list): # продолжанм преобразование
                            for j in range(len(list1[i])):
                                list2.append(list1[i][j])
                        else: # если список одноуровневый, то добавляем элемент в общий список
                            list2.append(list1[i])
                    list1 = list2
                else:
                    longlist.extend(list1) # если список одноуровневый, то добавляем его в основной список
                    break
        return longlist

class FlatIterator:
    def __init__(self, list_of_list):
        #self.longlist = []
        self.list_of_list = list_of_list
        self.longlist = Parting.parsing_lists1(self.list_of_list)


        #print(self.longlist)


    def __iter__(self):
        self.cursor = -1
        return self

    def __next__(self):
        self.cursor += 1
        if len(self.longlist) == self.cursor:
            raise StopIteration
        item = self.longlist[self.cursor]
        #print(self.cursor)
        return item




def test_3():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()
