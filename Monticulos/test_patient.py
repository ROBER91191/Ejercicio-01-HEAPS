from MaxHeap import MaxHeap
from MinHeap import MinHeap
from Patient_list import patient_list


def patients_Max_heap(list_emergency_rooms):
    heap = MaxHeap()
    # print('¿Está vacío? ' + str(heap.is_empty()))
        
    for i in list_emergency_rooms:
        heap.push(i)
        
        # print("Padre: ", heap.peek(), "\n")
    print('Total patients: ' + str(heap.size()))
    return heap



def patient_care(list_heap):
	print("Ordered Patients by priority")
	for val in list_heap.heap:
          print(val.value)

def patients_Min_heap(list_emergency_rooms):
    heap = MinHeap()
    # print('¿Está vacío? ' + str(heap.is_empty()))
        
    for i in list_emergency_rooms:
        heap.push(i)
        
        # print("Padre: ", heap.peek(), "\n")
    print('Total patients: ' + str(heap.size()))
    return heap

if __name__ == '__main__':
    list_emergency_rooms=patient_list()
    # test=patients_Max_heap(list_emergency_rooms)
    test=patients_Min_heap(list_emergency_rooms)
    patient_care(test)
