class LongList:
    def __init__(self, lst:list = None, long: dict = None): # simple constructor
        if long:
            self.__dictionary = long["dictionary"]
            self.values_dict = long["values_dict"]
            self.last_list = long["last_list"]
            self.len = long["len"]
        elif lst:
            self.__dictionary = {
                0: lst.copy(),
            }
            self.len = len(lst)
            self.last_list = self.__dictionary[0]
            self.values_dict = {}
            for index,val in enumerate(self.last_list):
                if val not in self.values_dict:
                    self.values_dict[val] = {
                        'count': 1,
                        'locations': [
                            {
                                'key': 0,
                                'index': index,
                            }
                        ]
                    }
                else:
                    self.values_dict[val]['count'] += 1
                    self.values_dict[val]['locations'].append({
                        'key': 0,
                        'index': index,
                    })
        else:
            self.__dictionary = {
                0: [],
            }
            self.len = 0
            self.last_list = self.__dictionary[0]
            self.values_dict = {}

            ''' 
            Example:
                    values_dict = {
                        1: {
                            'count': 2,
                            'locations': [
                                {'key': 0, 'index': 0},
                                {'key': 1, 'index': 10},
                            ]
                        },
                        2: {
                            'count': 2,
                            'locations': [
                                {'key: 0, index': 0},
                                {'key: 1, index': 10},
                            ]
                        },
                        5: {
                            'count': 5,
                            'locations': [
                                {'key: 0, index': 3},
                                {'key: 5, index': 20},
                            ]
                        }
                    }
            '''

    def get_last_list(self): return self.last_list

    def get_list(self,key): return self.__dictionary[key] if key in self.__dictionary else None

    def append(self, value): # this function append an element to the dictionary
        if len(self.last_list) != 536870912: # maximum length of list in python (536870912)
            self.last_list.append(value)
        else:
            self.__dictionary[list(self.__dictionary.keys())[-1]+1] = [value] # create list in the next key in the dictionary
            self.last_list = self.__dictionary[list(self.__dictionary.keys())[-1]]
        if value in self.values_dict:
            self.values_dict[value]['count'] += 1
            self.values_dict[value]['locations'].append({
                'key': list(self.__dictionary.keys())[-1],
                'index': len(self.last_list)-1,
            })
        else:
            self.values_dict[value] = {
                'count':1,
                'locations': [
                    {
                        'key': list(self.__dictionary.keys())[-1],
                        'index': len(self.last_list) - 1,
                    }
                ]
            }
        self.len += 1

    def insert(self, key, index ,value): # this function inserts an element to the dictionary
        if len(self.__dictionary[key]) < 536870911:
            self.__dictionary[key].insert(index, value)
            self.len += 1
            if value in self.values_dict:
                self.values_dict[value]['count'] += 1
                self.values_dict[value]['locations'].append({
                    'key': key,
                    'index': index,
                })
            else:
                self.values_dict[value] = {
                    'count': 1,
                    'locations': [
                        {
                            'key': key,
                            'index': index,
                        }
                    ]
                }
            for val in self.values_dict:
                for location in self.values_dict[val]['locations']:
                    if location['key'] == key and location['index'] > index:
                        location['index']-=1
            return value
        else: return None

    def pop(self,key=None,index=None): # this function pops an element from the dictionary
        if (key, index) != (None, None):
            value = self.__dictionary[key].pop(index)
            self.values_dict[value]['count'] -= 1
            for location in self.values_dict[value]['locations']:
                if location['key'] == key and location['index'] == index:
                    self.values_dict[value]['locations'].remove(location)
            if self.values_dict[value]['count'] < 1:
                del self.values_dict[value]
        else:
            value = self.last_list.pop()
            self.values_dict[value]['count'] -= 1
            for location in self.values_dict[value]['locations']:
                if location['key'] == key and location['index'] == index:
                    self.values_dict[value]['locations'].remove(location)
            if self.values_dict[value]['count'] < 1:
                del self.values_dict[value]
        self.len-=1

    def remove(self,value):
        if value in self.values_dict:
            for val in self.values_dict:
                for location in self.values_dict[val]['locations']:
                    if location['key'] == self.values_dict[value]['locations'][0]['key'] and location['index'] > self.values_dict[value]['locations'][0]['index']:
                        location['index']-=1
            self.__dictionary[self.values_dict[value]['locations'][0]['key']].remove(value)
            self.values_dict[value]['locations'] = self.values_dict[value]['locations'][1:]
            self.len -= 1
            return value
        else:
            return None

    def remove_all(self,value):
        while self.values_dict[value]['locations']: self.remove(value)
        return value

    def reverse(self):
        reversed_dict = {

        }
        reversed_values_dict = {

        }
        cur_key = 0
        for key in [ key for key in self.__dictionary.keys() ][::-1]:
            reversed_dict[cur_key] = self.__dictionary[key][::-1]
            cur_key+=1
        self.__dictionary = reversed_dict
        # return reversed_dict

        for key in ( key for key in self.__dictionary.keys() ):
            for index,value in enumerate(self.__dictionary[key]):
                if value not in reversed_values_dict:
                    reversed_values_dict[value] = {
                        'count' : 1,
                        'locations' : [
                            {
                                'key': key,
                                'index': index,
                            }
                        ]
                    }
                else:
                    reversed_values_dict[value]['count'] += 1
                    reversed_values_dict[value]['locations'].append({
                        'key': key,
                        'index': index,
                    })
        self.values_dict = reversed_values_dict

        return reversed_dict

    def index(self,value): return self.values_dict[value]['locations'][0] if value in self.values_dict else None

    def all_index(self,value): return self.values_dict[value]['locations'] if value in self.values_dict else None

    def count (self,value): return self.values_dict[value]['count']

    def remove_all_duplicates (self):
        _ = False
        for key in set([key for key in list(self.values_dict.keys())]):
            _ = self.remove_duplicated_value(key) or _
        return _ if _ else None

    def remove_duplicated_value (self,value):
        if self.values_dict[value]['count'] <= 1: return None
        _ = 1
        while len(self.values_dict[value]['locations']) > _:
            self.__dictionary[self.values_dict[value]['locations'][_]["key"]].pop(self.values_dict[value]['locations'][_]["index"])
            self.values_dict[value]['locations'].pop(-1)
        self.values_dict[value]['count'] = 1
        return value

    def contains(self, value): return value in self.values_dict

    def sort(self,fun=None):
        if not fun:
            long = LongList()
            keys = list(self.values_dict.keys())
            keys.sort()
            for key in keys:
                for _ in self.values_dict[key]['locations']:
                    long.append(key)
            self.__dictionary = long.__dictionary
            self.values_dict = long.values_dict
        else:
            fun(self.__dictionary,self.values_dict,self.len)