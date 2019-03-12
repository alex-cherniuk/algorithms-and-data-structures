class HashTable:
    """
    Hash table which uses strings for keys. Value can be any object.
    Example usage:
        table = HashTable(10)
        table.set('apple', 10).set('banana', 20).set('cucumber', 35)
        table['cucumber'] = 30
    """
    def __init__(self, capacity=1000):
        self.capacity = capacity
        self.data = [[] for _ in range(capacity)]
        self._keys = []
        self.size = 0

    def hash_function(self, key_string):
        return sum((ord(char) for char in key_string)) % self.capacity

    def _find(self, key):
        index = self.hash_function(key)
        cell = self.data[index]
        for item in cell:
            if item[0] == key:
                return item, cell
        return None, cell

    def set(self, key, value):
        """ Insert value with key into hash table. If key already exists, then the value will be updated. """
        item, cell = self._find(key)
        if item:
            item[1] = value
        else:
            cell.append([key, value])
            self._keys.append(key)
            self.size += 1
        return self

    def get(self, key):
        """ Get value with key (key must be a string). If not found, it will raise a KeyError. """
        item, _ = self._find(key)
        if item:
            return item[1]
        raise KeyError(key)

    def remove(self, key):
        """
        Remove the value associated with key from the hashtable. If found,
        the value will be returned. If not found, KeyError will be raised.
        """
        item, cell = self._find(key)
        if item:
            cell.remove(item)
            self._keys.remove(key)
            self.size -= 1
            return
        raise KeyError(key)

    def __len__(self):
        return self.size

    # Python's dict interface
    def __setitem__(self, key, value):
        self.set(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def __delitem__(self, key):
        return self.remove(key)

    def __repr__(self):
        return '{ ' + ', '.join([key + ':' + str(self.get(key)) for key in self._keys]) + ' }'


if __name__ == "__main__":
    table = HashTable(3)
    table.set('apple', 10)
    table['banana'] = 20
    table.set('pineapple', 30)
    table.set('cucumber', 40)
    table['tomato'] = 15
    print(table)
    print(table.get('tomato'))
    print(table['pineapple'])
    del table['apple']
    print(table)
    try:
        del table['egg']
    except KeyError as error:
        print('Unknown key:', error)
    print(len(table))
