import copy
from math import sqrt
from typing import Callable, Iterator, Optional, Tuple

import numpy as np
from datastructures.ihashmap import KT, VT, IHashMap
from datastructures.array import Array
import pickle
import hashlib

from datastructures.linkedlist import LinkedList

class HashMap(IHashMap[KT, VT]):

    def __init__(self, number_of_buckets=7, load_factor=0.75, custom_hash_function: Optional[Callable[[KT], int]]=None) -> None:
        empty_init = [LinkedList(data_type=Tuple) for x in range(number_of_buckets)]
        self._buckets: Array = Array(starting_sequence= empty_init, data_type=LinkedList)
        self._load_factor = load_factor
        self._count:int = 0
        self._hash_function = HashMap._default_hash_function if custom_hash_function is None else custom_hash_function
        self._num_of_buckets = number_of_buckets
        

    def _get_bucket_index(self, key: KT, bucket_size: int)->int:
        bucket_index=self._hash_function(key)
        return bucket_index % bucket_size

    def __getitem__(self, key: KT) -> VT:
        for (k,v) in self._buckets[self._get_bucket_index(key, len(self._buckets))]:
            if k==key:
                return v
        raise KeyError(f"{key} does not exist in the HashMap")   

    def _resize(self):
        double = self._num_of_buckets * 2
        old_buckets = []
        for i in range(len(self._buckets)):
            old_buckets.append(self._buckets[i])
        def _next_prime(n:int):
            def is_prime(num:int) -> bool:
                prime: bool = False
                if not num < 2:
                    for i in range(2, (num)//2):
                        if num//i == 0:
                            prime = False
                        else:
                            prime = True
    
                    
        
            while not is_prime(n):
                n+=1

            return n
        self._buckets = Array(starting_sequence= [LinkedList(data_type=Tuple) for x in range(double)], data_type=LinkedList[Tuple])
        for i in range(len(old_buckets)):
            current = old_buckets[i]._head
            while current is not None:
                self.__setitem__(key=current.data[0], value=current.data[1])
                current = current.next
            

    def __setitem__(self, key: KT, value: VT) -> None:        
        if self._count / len(self._buckets) >= self._load_factor:
            self._resize
        index = self._get_bucket_index(key, len(self._buckets)) 
        if key in self._buckets:
            current = self._buckets[index]._head
            while current is not None:
                if current.data[0] == key:
                    current.data = (key, value)
        else:
            self._buckets[index].append((key, value))
            self._count += 1


        
        

    def keys(self) -> Iterator[KT]:
        raise
    
    def values(self) -> Iterator[VT]:
        raise NotImplementedError("HashMap.values() is not implemented yet.")

    def items(self) -> Iterator[Tuple[KT, VT]]:
        raise NotImplementedError("HashMap.items() is not implemented yet.")
            
    def __delitem__(self, key: KT) -> None:
        if key not in self._buckets:
            raise KeyError(f"{key} is not in hashmap.")
        index = self._get_bucket_index(key)
        current = self._buckets[index]._head
        while current is not None:
            if current.data[0] == key:
                current.previous.next = current.next
                current.next.previous = current.previous
                self._count -= 1
                return
    
    def __contains__(self, key: KT) -> bool:
        index = self._get_bucket_index(key, len(self._buckets)) 
        current = self._buckets[index]._head
        while current is not None:
            if current.data[0] == key:
                return True
            else:
                current = current.next
        return False
    
    def __len__(self) -> int:
        return self._count
    
    def __iter__(self) -> Iterator[KT]:
        for i in range(len(self._buckets)):
            current=self._buckets[i]._head
            while current is not None:
                yield current.data[0]
                current=current.next
    
    def __eq__(self, other: object) -> bool:
        raise NotImplementedError("HashMap.__eq__() is not implemented yet.")

    def __str__(self) -> str:
        return "{" + ", ".join(f"{key}: {value}" for key, value in self) + "}"
    
    def __repr__(self) -> str:
        return f"HashMap({str(self)})"

    @staticmethod
    def _default_hash_function(key: KT) -> int:
        """
        Default hash function for the HashMap.
        Uses Pickle to serialize the key and then hashes it using SHA-256. 
        Uses pickle for serialization (to capture full object structure).
        Falls back to repr() if the object is not pickleable (e.g., open file handles, certain C extensions).
        Returns a consistent integer hash.
        Warning: This method is not suitable
        for keys that are not hashable or have mutable state.

        Args:
            key (KT): The key to hash.
        Returns:
            int: The hash value of the key.
        """
        try:
            key_bytes = pickle.dumps(key)
        except Exception:
            key_bytes = repr(key).encode()
        return int(hashlib.md5(key_bytes).hexdigest(), 16)