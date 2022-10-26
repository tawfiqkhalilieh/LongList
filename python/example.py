from long_list import LongList

long_list = LongList()
assert not long_list.last_list

long_list = LongList([1,2,3])

assert long_list.get_last_list() == [1,2,3]
assert long_list.get_list(0) == [1,2,3]
assert long_list.len == 3

long_list.append(4)

assert long_list.get_last_list() == [1,2,3,4]
assert long_list.get_list(0) == [1,2,3,4]
assert long_list.len == 4

long_list.insert(0, 0, 0)
assert long_list.get_last_list() == [0,1,2,3,4]
assert long_list.get_list(0) == [0,1,2,3,4]
assert long_list.len == 5

long_list.pop()

assert long_list.get_last_list() == [0,1,2,3]
assert long_list.get_list(0) == [0,1,2,3]
assert long_list.len == 4

long_list.pop(key=0,index=0)

assert long_list.get_last_list() == [1,2,3]
assert long_list.get_list(0) == [1,2,3]
assert long_list.len == 3

long_list.pop(key=0,index=1)

assert long_list.get_last_list() == [1,3]
assert long_list.get_list(0) == [1,3]
assert long_list.len == 2

long_list = LongList([5,2,3,4,56,8,5,3])

assert long_list.remove(3) == 3
assert long_list.get_last_list() == [5,2,4,56,8,5,3]
assert long_list.get_list(0) == [5,2,4,56,8,5,3]
assert not long_list.remove(989)

assert long_list.remove_all(5) == 5
assert long_list.get_last_list() == [2,4,56,8,3]
assert long_list.get_list(0) == [2,4,56,8,3]

assert long_list.index(2)["index"] == 0
assert long_list.index(2)["key"] == 0
assert not long_list.index(1)

long_list.append(1)
long_list.append(1)
long_list.append(1)

assert len(long_list.all_index(1)) == 3
assert long_list.all_index(1) == [
    {
        "key":0, "index":5
    },{
        "key":0, "index":6
    },
    {
        "key":0, "index":7
    }
]

long_list = LongList([10,55,0,3,55,10])

assert long_list.remove_duplicated_value(10) == 10
assert long_list.get_last_list() == [10,55,0,3,55]
assert long_list.remove_duplicated_value(55) == 55
assert long_list.get_last_list() == [10,55,0,3]
assert long_list.remove_duplicated_value(0) == None
assert long_list.get_last_list() == [10,55,0,3]

long_list = LongList([10,55,0,3,55,10])
long_list.remove_all_duplicates()

assert long_list.get_last_list() == [10,55,0,3]