from MaxHeap import MaxHeap
from MinHeap import MinHeap
from Patient_list import patient_list
from Emergency_room import Emergency_room


def emergency_room(list_patients):
    heap_urgency_levels = MaxHeap()
    heap_wait_hours=MinHeap()
        
    for i in list_patients:
        heap_urgency_levels.push(i)
        heap_wait_hours.push(i)
    emergency_room=Emergency_room (heap_urgency_levels,heap_wait_hours)
    return emergency_room


def patient_urgency_level(list_heap):
    print("Ordered Patients by priority Urgency level \n")
    for val in list_heap.heap:
        print(val)
    print("\n")


def patient_wait_hours(list_heap):
    print("Ordered Patients by priority Wait hours \n")
    for val in list_heap.heap:
        print(val)
    print("\n")


if __name__ == '__main__':
    list_emergency_rooms=patient_list()
    patients_emergency_rooms=emergency_room(list_emergency_rooms)

    print("Nº Total de pacientes: ",patients_emergency_rooms.max_heap.size())
    index=0
    patient_urgency_level(patients_emergency_rooms.max_heap)
    patient_wait_hours(patients_emergency_rooms.min_heap)
    for patient, patient2 in zip(patients_emergency_rooms.max_heap.heap,patients_emergency_rooms.min_heap.heap):
        patients_emergency_rooms.max_heap.pop()
        if index%2==0:
            print("Pacientes por nivel de urgencia despues de antender a ",patient.name)
            patient_urgency_level(patients_emergency_rooms.max_heap)
            for  j, patient2 in enumerate(patients_emergency_rooms.min_heap.heap):
                if patient.equals(patient2):
                    patients_emergency_rooms.min_heap.pop()
                    patient_wait_hours(patients_emergency_rooms.min_heap)
                    break
        else:
            print("Pacientes por nivel de urgencia despues de antender a ",patient2.name)
            patient_wait_hours(patients_emergency_rooms.min_heap)
            for  j, patient2 in enumerate(patients_emergency_rooms.max_heap.heap):
                if patient.equals(patient2):
                    patients_emergency_rooms.min_heap.pop()
                    patient_urgency_level(patients_emergency_rooms.max_heap)
        index+=1




     
    