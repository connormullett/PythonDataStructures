

class Node:

    def __init__(self, data, next):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)

    def delete_node(self, node, data):
        '''
        deletes a node by finding if the next nodes
        value is the one to be deleted, then reassigns
        the nodes next value to the node to deletes next node
        therefore 'deleting' that node
        returns None if no node contains searched value
        '''
        while node.next:
            if node.next.data == data:
                node.next = node.next.next
            else:
                node = node.next

    def insert_node(self, node, head):
        '''
        takes in two nodes and recursively
        inserts Node object into linked list
        '''
        if not head.next:
            head.next = node
        else:
            self.insert_node(node, head.next)

    def search_node(self, node, data):
        '''
        traverses the list looking for the data given
        returns none if the data is never found
        and returns the data of the node if found
        '''
        if not node.next:
            return None
        elif node.data == data:
            print('found node')
            return node.data
        else:
            print('recursing')
            self.search_node(node.next, data)


class LinkedList:

    def __init__(self):
        '''
        creates a new, blank linked_list
        with a size of 0
        '''
        self.head = None
        self.size = 0

    def __repr__(self):
        node = self.head
        out = '[ '
        while node.next:
            if not node.next.next:
                out += f'{node}'
            else:
                out += f'{node}, '
            node = node.next
        out += ' ]'
        return out

    def _create_node(self, data) -> Node:
        '''
        aux method that creates
        a node object for insertion
        '''
        return Node(data, None)

    def delete(self, data):
        '''
        deletes the first occurence of value in list
        '''
        self.head.delete_node(self.head, data)

    def delete_list(self):
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
        else:
            node.insert_node(node, linked_list.head)
        self.size += 1

    def search(self, data):
        '''
        searches for value given in the list
        returns None if value is not found
        '''
        print('entered search ..')
        return_data = self.head.search_node(self.head, data)
        print('exited search ..')
        return return_data


if __name__ == '__main__':
    linked_list = LinkedList()

    for i in range(1, 11):
        linked_list.insert(i)

    print(linked_list)

    linked_list.delete(5)

    print(linked_list)

    # deleted_data = linked_list.search(5)
    # print(f'searching for 5 :: {deleted_data}')
    data = linked_list.search(3)
    print(f'searching for 3 :: {data}')
