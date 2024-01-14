from MaxHeap import MaxHeap
from Patient_list import patient_list




def create_heap(list_emergency_rooms):
    heap=MaxHeap()
    print('Esta vacio? ' + str(heap.is_empty()))
    for i in list_emergency_rooms:
        heap.push(i)
        print('Tamaño actual: ' + str(heap.size()))
        print("Parent: ",heap.peek(),"\n")
    
    return heap

def patient_care(list_heap)->list:
    
    print(list_heap.__str__())



if __name__ == '__main__':
    list_emergency_rooms=patient_list()
    test=create_heap(list_emergency_rooms)
    patient_care(test)
    print('hola')