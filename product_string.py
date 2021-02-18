#!/usr/bin/env python3
import math

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None


    def find_index(self, index=None):
        last = self.head
        counter = 0
        while (last.next):
            last = last.next
            if counter == index:
                break
            counter += 1
        return last


def recur_prod(n):
   if n == 1:
       return n
   else:
       return prod

n1 = 1
n2 = 2
n3 = 3
n4 = 4
n = [1, 2, 3, 4]
prod = [n2 * n3 * n4, n1 * n3 * n4, n1 * n2 * n4, n1 * n2 * n3]

if prod == 0:
    print("The prod of 0 is 0")
else:
    print("The prod of", n, "is", prod)
