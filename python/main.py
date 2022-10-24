class LongList:
    def __init__(self, lst:list = None): # simple constructor
        if lst:
            self.__dictionary = {
                0: lst.copy(),
            }
        else:
            self.__dictionary = {
                0: [],
            }

    def get_last_list(self): # this function returns the last list of lists
        return self.__dictionary[[key for key in self.__dictionary][-1]].copy()

    def get_list(self,key):
        return self.__dictionary[key] if key in self.__dictionary else None

    def append(self, value): # this function append an element to the dictionary
        if len(self.__dictionary[[key for key in self.__dictionary][-1]]) != 536870912: # maximum length of list in python (536870912)
            self.__dictionary[[key for key in self.__dictionary][-1]].append(value) # normal append
        else:
            self.__dictionary[[key for key in self.__dictionary][-1]+1] = [value] # create list in the next key in the dictionary

    def insert(self, key, value): # this function inserts an element to the dictionary
        self.__dictionary[key].append(value)


    def pop(self,key=None,index=None): # this function pops an element from the dictionary
        if not key and not index:
            self.__dictionary[key].pop(index)
        else:
            self.__dictionary[[key for key in self.__dictionary][-1]].pop(-1)

    def remove(self,value):
        for key in self.__dictionary:
            for index in self.__dictionary[key]:
                if value == index:
                    self.__dictionary[key].remove(index)
                    return index

    def remove_all(self,value):
        _ = False
        for key in self.__dictionary:
            for index in self.__dictionary[key]:
                if value == index:
                    self.__dictionary[key].remove(index)
                    _ = True
        return index if _ else None

    def reverse(self):
        reversed_dict = {

        }
        cur_key = 0
        for key in [ key for key in self.__dictionary.keys() ][::-1]:
            reversed_dict[cur_key] = self.__dictionary[key][::-1]
            cur_key+=1
        self.__dictionary = reversed_dict
        return reversed_dict

    def index(self,value):
        for key in self.__dictionary:
            for index,val in enumerate(self.__dictionary[key]):
                if value == index:
                    return (key,value)

    def all_index(self,value):
        indexes = []
        for key in self.__dictionary:
            for index,val in enumerate(self.__dictionary[key]):
                if value == val:
                    indexes.append((key,index))
        return indexes

    def count (self,value):
        counter = 0
        for key in self.__dictionary:
            for index,val in enumerate(self.__dictionary[key]):
                if value == val:
                    counter+=1
        return counter

    def remove_all_duplicates (self):
        myset = set()
        long = LongList()
        for key in self.__dictionary:
            for val in self.__dictionary[key]:
                if not val in myset:
                    myset.add(val)
                    long.append(value=val)
        self.__dictionary = long.__dictionary

    def remove_duplicated_value (self,value):
        _ = True
        long = LongList()
        for key in self.__dictionary:
            for val in self.__dictionary[key]:
                if val == value:
                    if _:
                        long.append(val)
                        _ = False
                else:
                    long.append(val)
        self.__dictionary = long.__dictionary
        return value if not _ else None # if the function romomed any duplicated value it should return it else it returns None

    # TODO: sort method

# define new LongList
longlist = LongList([100,2,3,4,8,100,2,3,4,8])
# test my LongList
print(longlist.get_last_list())
longlist.reverse()
print(longlist.get_last_list())
print(longlist.index(3))
print(longlist.all_index(3))
print(longlist.count(3))
# longlist.remove_all_duplicates()
print(longlist.get_last_list())
print(longlist.remove_duplicated_value(value=100))
print(longlist.get_last_list())