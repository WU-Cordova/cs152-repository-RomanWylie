from __future__ import annotations

from dataclasses import dataclass
import os
from types import NoneType
from typing import Optional, Sequence
from datastructures.ilinkedlist import ILinkedList, T


class LinkedList[T](ILinkedList[T]):

    @dataclass
    class Node:
        data: T
        next: Optional[LinkedList.Node] = None
        previous: Optional[LinkedList.Node] = None

    def __init__(self, data_type: type = object) -> None:
        self._data_type=data_type
        self._head: LinkedList.Node = None
        self._tail: LinkedList.Node =None
        self._size:int=0
        
    @staticmethod
    def from_sequence(sequence: Sequence[T], data_type: type=object) -> LinkedList[T]:
        for i in range(len(sequence)):
            if not isinstance(sequence[i],data_type):
                raise TypeError("Sequence must only contain the correct type")
        linlis = LinkedList(data_type=data_type)
        for item in sequence:
            linlis.append(item)
        return linlis

    def append(self, item: T) -> None:
        if not isinstance(item, self._data_type):
            raise TypeError("Item is of incorrect type")
        new_node=LinkedList.Node(data=item)
        if self._size==0:
            self._head = new_node
            self._tail = new_node
        else:
            self._tail.next=new_node
            new_node.previous=self._tail
            self._tail=new_node
        self._size +=1

    def prepend(self, item: T) -> None:
        if not isinstance(item, self._data_type):
            raise TypeError("Item is of incorrect type")
        new_node=LinkedList.Node(data=item)
        if self._size==0:
            self._head = new_node
            self._tail = new_node
        else:
            self._head.previous=new_node
            new_node.next=self._head
            self._head=new_node
        self._size+=1

    def insert_before(self, target: T, item: T) -> None:
        if not isinstance(item, self._data_type):
            raise TypeError("Item is of incorrect type")
        if not isinstance(target, self._data_type):
            raise TypeError("Target is of incorrect type")
        if not target in iter(self):
            raise ValueError("Target not in list")
        new_node=LinkedList.Node(data=item)
        travel=self._head
        while travel is not None:
            if travel.data==target:
                break
            else:
                travel=travel.next
        new_node.previous=travel.previous
        travel.previous.next = new_node
        travel.previous=new_node
        new_node.next = travel
        self._size +=1
        
    def insert_after(self, target: T, item: T) -> None:
        if not isinstance(item, self._data_type):
            raise TypeError("Item is of incorrect type")
        if not isinstance(target, self._data_type):
            raise TypeError("Target is of incorrect type")
        if not target in iter(self):
            raise ValueError("Target not in list")
        new_node=LinkedList.Node(data=item)
        travel=self._head
        while travel is not None:
            if travel.data==target:
                break
            else:
                travel=travel.next
        new_node.previous=travel
        travel.next.previous = new_node
        new_node.next = travel.next
        travel.next=new_node
        self._size +=1
        
    def remove(self, item: T) -> None:
        if not isinstance(item, self._data_type):
            raise TypeError("Item is of incorrect type")
        if not item in iter(self):
            raise ValueError("Item is not in list")
        travel=self._head
        while travel is not None:
            if travel.data==item:
                break
            else:
                travel=travel.next
        travel.previous.next=travel.next
        travel.next.previous=travel.previous
        self._size-=1
        

    def remove_all(self, item: T) -> None:
        if not isinstance(item, self._data_type):
            raise TypeError("Item is of incorrect type")
        if not item in iter(self):
            raise ValueError("Item is not in list")
        travel=self._head
        while travel is not None:
            if travel.data==item and travel.next is not None:
                travel.next.previous=travel.previous
                travel.previous.next=travel.next
                self._size-=1
                travel=travel.next
            elif travel.data==item:
                travel.previous.next=None
                self._size-=1
                travel=travel.next
            else:
                travel=travel.next
        
    def pop(self) -> T:
        if self._tail is None:
            raise IndexError("List is empty")
        removed_item=self._tail
        self._tail=self._tail.previous
        self._tail.next=None
        self._size-=1
        return removed_item.data
        

    def pop_front(self) -> T:
        if self._head is None:
            raise IndexError("List is empty")
        removed_item=self._head
        self._head=self._head.next
        self._head.previous=None
        self._size-=1
        return removed_item.data

    @property
    def front(self) -> T:
        if isinstance(self._head, NoneType):
            raise IndexError("Linked list is empty")
        else:    
            return self._head.data

    @property
    def back(self) -> T:
        if isinstance(self._tail, NoneType):
            raise IndexError("Linked list is empty")
        else:    
            return self._tail.data

    @property
    def empty(self) -> bool:
        return self._size == 0
    
    def __len__(self) -> int:
        return self._size

    def clear(self) -> None:
        self._tail = None
        self._head = None
        self._size = 0

    def __contains__(self, item: T) -> bool:
        return item in iter(self)

    def __iter__(self) -> ILinkedList[T]:
        travel=self._head
        iterable=[]
        while travel is not None:
            item = travel.data
            iterable.append(item)
            travel=travel.next
        iterable=iter(iterable)
        return iterable
    
    def __next__(self) -> T:
        return

    def __reversed__(self) -> ILinkedList[T]:
        travel=self._tail
        rev_list = LinkedList(data_type=self._data_type)
        while travel is not None:
            item = travel.data
            rev_list.append(item)
            travel=travel.previous
        return rev_list
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, LinkedList):
            return False
        elif not self._data_type == other._data_type:
            return False
        elif not self._size == other._size:
            return False
        else:
            travel=self._head
            other_travel=other._head
            equal:bool = False
            while travel is not None:
                equal=travel.data==other_travel.data
                if equal==False:
                    break
                travel=travel.next
                other_travel=other_travel.next
            return equal
            

    def __str__(self) -> str:
        items = []
        current = self._head
        while current:
            items.append(repr(current.data))
            current = current.next
        return '[' + ', '.join(items) + ']'

    def __repr__(self) -> str:
        items = []
        current = self._head
        while current:
            items.append(repr(current.data))
            current = current.next
        return f"LinkedList({' <-> '.join(items)}) Count: {self._size}"


if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'OOPS!\nThis is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')
