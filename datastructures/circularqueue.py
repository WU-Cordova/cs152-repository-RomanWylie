from typing import Any

from datastructures.array import Array
from datastructures.iqueue import IQueue, T

class CircularQueue(IQueue[T]):
    """ Represents a fixed-size circular queue. The queue
        is circular in the sense that the front and rear pointers wrap around the
        array when they reach the end. The queue is full when the rear pointer is
        one position behind the front pointer. The queue is empty when the front
        and rear pointers are equal. This implementation uses a fixed-size array.
    """

    def __init__(self, maxsize: int = 0, data_type=object) -> None:
        ''' Initializes the CircularQueue object with a maxsize and data_type.
        
            Examples:
                >>> q = CircularQueue(maxsize=5, data_type=int)
                >>> q.maxsize
                5
                >>> q.empty
                True
                >>> q.full
                False
                >>> q.front
                IndexError('Queue is empty')
                >>> q.rear
                IndexError('Queue is empty')

            Arguments:
                maxsize: The maximum size of the queue
                data_type: The type of the elements in the queue
        '''
        self.type = data_type
        self.capacity=maxsize
        initial_list:list = [data_type() for x in range(maxsize)]
        self.queue=Array(starting_sequence=initial_list, data_type=data_type)
        self.__front=0
        self.__count=0

    def enqueue(self, item: T) -> None:
        ''' Adds an item to the rear of the queue

            Examples:
                >>> q = CircularQueue(maxsize=5, data_type=int)
                >>> q.enqueue(1)
                >>> q.enqueue(2)
                >>> q.enqueue(3)
                >>> q.front
                1
                >>> q.rear
                3
                >>> q.enqueue(4)
                >>> q.enqueue(5)
                >>> q.full
                True
                >>> q.enqueue(6)
                IndexError('Queue is full')
            
            Arguments:
                item: The item to add to the queue
                
            Raises:
                IndexError: If the queue is full
        '''
        if self.full==True:
            raise IndexError("Queue is full")
        else:
            next_position = (self.__front + self.__count)%self.capacity
            self.queue[next_position]=item
            self.__count+=1

    def dequeue(self) -> T:
        ''' Removes and returns the item at the front of the queue

            Examples:
                >>> q = CircularQueue(maxsize=5, data_type=int)
                >>> q.enqueue(1)
                >>> q.enqueue(2)
                >>> q.enqueue(3)
                >>> q.dequeue()
                1
                >>> q.dequeue()
                2
                >>> q.dequeue()
                3
                >>> q.dequeue()
                IndexError('Queue is empty')
                >>> q.dequeue()
                IndexError('Queue is empty')

            Returns:
                The item at the front of the queue

            Raises:
                IndexError: If the queue is empty
        '''
        if self.empty==True:
            raise IndexError("Queue is empty")
        else:
            item_to_return=self.queue[self.__front]
            self.__front=(self.__front + 1) % self.capacity
            self.__count -=1 
            return item_to_return

    def clear(self) -> None:
        ''' Removes all items from the queue 
        
            Examples:
                >>> q = CircularQueue(maxsize=5, data_type=int)
                >>> q.enqueue(1)
                >>> q.enqueue(2)
                >>> q.enqueue(3)
                >>> q.clear()
                >>> q.empty
                True
                >>> q.front
                IndexError('Queue is empty')
                >>> q.rear
                IndexError('Queue is empty')
        '''
        for i in range(self.capacity):
            self.queue[i]=self.type()
            self.front=0
            self.count=0

    @property
    def front(self) -> T:
        ''' Returns the item at the front of the queue without removing it

            Examples:
                >>> q = CircularQueue(maxsize=5, data_type=int)
                >>> q.enqueue(1)
                >>> q.enqueue(2)
                >>> q.enqueue(3)
                >>> q.front
                1
                >>> q.dequeue()
                1
                >>> q.front
                2
                >>> q.dequeue()
                2
                >>> q.front
                3
                >>> q.dequeue()
                3
                >>> q.front
                IndexError('Queue is empty')

            Returns:
                The item at the front of the queue

            Raises:
                IndexError: If the queue is empty
        '''
        if self.empty==True:
            raise IndexError
        else: 
            return self.queue[self.__front]

    @property
    def full(self) -> bool:
        ''' Returns True if the queue is full, False otherwise 

            Examples:
                >>> q = CircularQueue(maxsize=5, data_type=int)
                >>> q.full
                False
                >>> q.enqueue(1)
                >>> q.full
                False
                >>> q.enqueue(2)
                >>> q.full
                False
                >>> q.enqueue(3)
                >>> q.full
                False
                >>> q.enqueue(4)
                >>> q.full
                False
                >>> q.enqueue(5)
                >>> q.full
                True
                >>> q.dequeue()
                1
                >>> q.full
                False
                >>> q.dequeue()
                2
                >>> q.full
                False
                >>> q.dequeue()
                3
                >>> q.full
                False
                >>> q.dequeue()
                4
                >>> q.full
                False
                >>> q.dequeue()
                5
                >>> q.full
                False
        
            Returns:
                True if the queue is full, False otherwise
        '''
        return self.__count==self.capacity

    @property
    def empty(self) -> bool:
        ''' Returns True if the queue is empty, False otherwise

            Examples:
                >>> q = CircularQueue(maxsize=5, data_type=int)
                >>> q.empty
                True
                >>> q.enqueue(1)
                >>> q.empty
                False
                >>> q.enqueue(2)
                >>> q.empty
                False
                >>> q.enqueue(3)
                >>> q.empty
                False
                >>> q.enqueue(4)
                >>> q.empty
                False
                >>> q.enqueue(5)
                >>> q.empty
                False
                >>> q.dequeue()
                1
                >>> q.empty
                False
                >>> q.dequeue()
                2
                >>> q.empty
                False
                >>> q.dequeue()
                3
                >>> q.empty
                False
                >>> q.dequeue()
                4
                >>> q.empty
                False
                >>> q.dequeue()
                5
                >>> q.empty
        
            Returns:
                True if the queue is empty, False otherwise
        '''
        return self.__count==0
    
    @property
    def maxsize(self) -> int:
        ''' Returns the maximum size of the queue

            Examples:
                >>> q = CircularQueue(maxsize=5, data_type=int)
                >>> q.maxsize
                5

            Returns:
                The maximum size of the queue
        '''
        return self.capacity

    def __eq__(self, other: object) -> bool:
        ''' Returns True if this CircularQueue is equal to another object, False otherwise
        
            Equality is defined as:
                - The element values at the front and rear pointers are equal
                - The element values between the front and rear pointers are equal
                - The maxsize of the queue is equal
                - The data_type of the queue is equal
                - Two queues are equal if they have the same elements in the same order, regardless of the index
                  of the front and rear pointers.

            Examples:
                >>> q1 = CircularQueue(maxsize=5, data_type=int)
                >>> q2 = CircularQueue(maxsize=5, data_type=int)
                >>> q1 == q2
                True
                >>> for i in range(5): q1.enqueue(i)
                >>> for i in range(5): q2.enqueue(i)
                >>> q1 == q2
                True
                >>> q1.dequeue()
                0
                >>> q1 == q2
                False
                
            Arguments:
                other: The object to compare this CircularQueue to
                
            Returns:
                True if this CircularQueue is equal to another object, False otherwise
        '''
        
        if self.__count==other.__count:
            list_self=[]
            list_other=[]
            for i in range(self.capacity):
                list_self.append(self.queue[(self.__front+i+self.__count)%self.capacity])
                list_other.append(other.queue[(other.__front+i+other.__count)%self.capacity])
            return list_self==list_other
        else:
            return False

    
    def __len__(self) -> int:
        ''' Returns the number of items in the queue

            Examples:
                >>> q = CircularQueue(maxsize=5, data_type=int)
                >>> len(q)
                0
                >>> q.enqueue(1)
                >>> len(q)
                1
                >>> q.enqueue(2)
                >>> len(q)
                2
                >>> q.enqueue(3)
                >>> len(q)
                3
                >>> q.dequeue()
                1
                >>> len(q)
                2
                >>> q.dequeue()
                2
                >>> len(q)
                1
                >>> q.dequeue()
                3
                >>> len(q)
                0
        
            Returns:
                The number of items in the queue
        '''
        return self.__count

    def __str__(self) -> str:
        ''' Returns a string representation of the CircularQueue

            Examples:
                >>> q = CircularQueue(maxsize=5, data_type=int)
                >>> q.enqueue(1)
                >>> q.enqueue(2)
                >>> q.enqueue(3)
                >>> print(q)
                [1, 2, 3]
        
            Returns:
                A string representation of the queue
        '''
        return str(self.queue)

    def __repr__(self) -> str:
        ''' Returns a developer string representation of the CircularQueue object

            Examples:
                >>> q = CircularQueue(maxsize=5, data_type=int)
                >>> q.enqueue(1)
                >>> q.enqueue(2)
                >>> q.enqueue(3)
                >>> repr(q)
                'ArrayQueue([1, 2, 3])'
        
            Returns:
                A string representation of the CircularQueue object
        '''
        return f'ArrayQueue({repr(self.queue)})'
                                  
