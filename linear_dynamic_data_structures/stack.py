

class Stack:
    """Stack is an abstract data type that serves as a collection of elements.

    The order in which elements come off a stack gives rise to its alternative name, LIFO (last in, first out).
    The name "stack" for this type of structure comes from the analogy to a set of physical items stacked on top of 
    each other, which makes it easy to take an item off the top of the stack, while getting to an item deeper in the 
    stack may require taking off multiple other items first.
    """

    def __init__(self):
        self._maxsize = 0
        self._top = 0
        self._items = []

    def push(self):
        """Add an element to the collection.

        :return: None
        """
        pass

    def pop(self):
        """Remove the most recently added element that was not yet removed.

        :return: Element
        """
        pass

    def top(self):
        """Get the value of the top element.

        :return: Element
        """
        pass
