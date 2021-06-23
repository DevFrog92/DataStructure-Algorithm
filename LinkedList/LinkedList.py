# Linked List 구현

# Linked List 를 구성하는 Node 클래스 생성
class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self,data):
        self.head = Node(data)

    def validate(self):
        if self.head == "":
            return '요소가 존재하지 않습니다.'

    def validate_index_under_zero(self,index):
        if index < 0:
            return '음의 인덱스는 입력할 수 없습니다.'

    def get_all_components(self):
        self.validate()
        current_node = self.head
        all_components_list = []
        while current_node:
            all_components_list.append(current_node.data)
            if current_node.next == None:
                break
            current_node = current_node.next
        return all_components_list

    def append_node(self,data):
        if self.head == '':
            self.head = Node(data)
            return

        current_data = self.head

        while current_data.next:
            current_data = current_data.next
        current_data.next = Node(data)
        return

    def delete_node_by_index(self,index):
        self.validate_index_under_zero(index)
        self.validate()

        if index == 0:
            self.head = self.head.next
            return

        current_node = self.get_node(index)
        deleted_node = current_node.next
        current_node.next = deleted_node.next
        return

    def append_node_by_index(self,index,data):

        self.validate_index_under_zero(index)
        self.validate()
        new_node = Node(data)

        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current_node = self.get_node(index)
        next_node = current_node.next
        current_node.next = new_node
        new_node.next = next_node
        return

    def get_node(self,index):
        self.validate_index_under_zero(index)
        self.validate()
        if index == 0:
            return self.head

        current_node = self.head
        count = 0
        while current_node.next:
            if count == index-1:
                break
            count += 1
            current_node = current_node.next
        return current_node.next

    def find_kth_node_from_endpoint_by_index(self,index):
        self.validate_index_under_zero(index)
        self.validate()
        length_of_linked_lit = self.length_of_linked_list()

        if index > length_of_linked_lit:
            return '리스트를 벗어난 영역의 인덱스 입니다.'

        if index == length_of_linked_lit:
            return self.head

        count = 1
        current_node = self.head
        while current_node:
            if count == length_of_linked_lit-index+1:
                return current_node
            count +=1
            current_node = current_node.next
        return None


    def length_of_linked_list(self):
        self.validate()
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next
        return count



linked_list = LinkedList(1)
for i in range(2,10):
    linked_list.append_node(i)
print(linked_list.get_all_components())
print()
linked_list.append_node_by_index(2,100)
linked_list.append_node_by_index(0,100)
linked_list.get_all_components()
linked_list.delete_node_by_index(3)
print()
print(linked_list.get_all_components())
print(linked_list.get_node(3).data)
print(linked_list.length_of_linked_list())
print(linked_list.find_kth_node_from_endpoint_by_index(3).data)