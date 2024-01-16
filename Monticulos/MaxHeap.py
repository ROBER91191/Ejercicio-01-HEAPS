from Heap import Heap

class MaxHeap(Heap):

    def __init__(self):

        super().__init__(lambda parent, child: parent< child)

