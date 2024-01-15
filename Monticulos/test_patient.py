from MaxHeap import MaxHeap
from Patient_list import patient_list


def create_heap(list_emergency_rooms):
    heap = MaxHeap()
    print('¿Está vacío? ' + str(heap.is_empty()))
    
    for i in list_emergency_rooms:
        heap.push(i)
        print('Tamaño actual: ' + str(heap.size()))
        print("Padre: ", heap.peek(), "\n")
        print("Ordered Patients")
		
        for indice, patients in enumerate(heap.heap):
            print(patients)
            
    return heap


def patient_care(list_heap):
    
	for val in list_heap.heap:
          print(val.value)


if __name__ == '__main__':
    list_emergency_rooms=patient_list()
    test=create_heap(list_emergency_rooms)
    # patient_care(test)
