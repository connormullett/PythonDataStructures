

class Node:

    def __init__(self, data, next):
        self.data = data
        self.next = None

    def insert_node(self, node, head):
        '''
        takes in two nodes and recursively
        inserts Node object into linked list
        '''
        if not head.next:
            head.next = node
        else:
            self.insert_node(node, head.next)


class LinkedList:

    def __init__(self):
        '''
        creates a new, blank linked_list
        with a size of 0
        '''
        self.head = None
        self.size = 0

    def _create_node(self, data)->Node:
        '''
        aux method that creates
        a node object for insertion
        '''
        return Node(data, None)

    def deleteList(self):
        '''
        deletes self one by one recursively
        until the list can be deleted
        '''
        pass

    def insert(self, data):
        '''
        inserts element into list
        using the head and _create_node
        '''
        node = self._create_node(data)
        if self.head is None:
            self.head = node
            self.size += 1
        else:
            node.insert_node(node, linked_list.head)

    def search(self):
        '''
        searches for value given in the list
        returns None if value is not found
        '''
        pass


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.insert(1)
    linked_list.insert(2)
    linked_list.insert(3)
    print(linked_list.head)
    print(linked_list.head.next)
    print(linked_list.head.next.next)
