from datastructures.linkedlist import LinkedList
from projects.project3.orderitem import OrderItem

class CustomerOrder:
    def __init__(self):
        self._name: str = ""
        self._order: LinkedList = LinkedList(data_type=OrderItem)
        self._number: int = 0 

    def _add_to_order(self, item:OrderItem):
        self._order.append(item)

    def _add_name(self, name:str):
        self._name = name
    
    def _number_of_drinks(self, num:int):
        self._number=num
    
    def _incorrect_order(self):
        self._order.clear()

    def get_order(self):
        order_list = []
        travel=self._order._head
        while travel is not None:
            order_list.append(str(travel.data))
            travel=travel.next
        return f"{self._name}: {order_list}"
