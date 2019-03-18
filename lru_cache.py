class Node(object):

    def __repr__(self):
        return "<Node %s: %s>" % (self.key, self.value)

    def __init__(self, key, value, prev=None, next_=None):
        self.prev = prev
        self.next_ = None
        self.value = value
        self.key = key



class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.storage = {}
        self.head = None
        self.tail = None


    def put(self, key, value):

        # if key is already stored, update the value

        if self.storage.get(key):
            self.remove_node(self.storage[key])

        new_node = Node(key, value)

        if len(self.storage) + 1 > self.capacity:
            self.remove_node(self.head)

        self.add_node(new_node)


    def get(self, key):
        

        if not self.storage.get(key):
            return -1

        node = self.storage.get(key)

        self.remove_node(node)
        self.add_node(node)

        return node.value



    def add_node(self, node):
        
        if not self.head:
            self.head = self.tail = node
            self.storage[node.key] = node
            return

        # set link from new tail to previous tail (which will now be second-to-last node)
        node.prev = self.tail
        self.tail.next_ = node
        self.tail = node
        self.tail.next_ = None
        self.storage[node.key] = node

        return

    def remove_node(self, node):
        

        # there are nodes before it
        if node.prev is not None:
            node.prev.next_ = node.next_

        # there are nodes after it
        if node.next_ is not None:
            node.next_.prev = node.prev

        if node == self.head:
            self.head = node.next_

        if node == self.tail:
            self.tail = node.prev

        # in all cases, remove from storage
        del self.storage[node.key]

