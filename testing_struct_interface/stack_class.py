from exceptions import *


class Stack:

    def __init__(self, *stack_data):
        self.__stack = list(stack_data)

    def size(self):
        return len(self.__stack)

    def push(self, element):
        if element is None:
            raise Null_Exception("You are Trying to Add and empty Element")
        self.__stack.append(element)

    def pop(self):
        if len(self.__stack) == 0:
            raise Empty_Exception(
                "You are Trying to Remove and Element but the Stack is Empty")

        return self.__stack.pop()

    def peek(self):
        if len(self.__stack) == 0:
            raise Empty_Exception(
                "You are Trying to get the last Element but the Stack is Empty")
        return self.__stack[-1]

    def is_empty(self):
        return len(self.__stack) == 0


my_list = Stack()
my_list.pop()
