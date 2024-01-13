from MinHeap import MinHeap
from Emergency_room import Emergency_room
from Patient import Patient

patient1=Patient('Roberto','4','4')
patient2=Patient('Esther','2','7')
patient3=Patient('Alfredo','5','4')
patient4=Patient('Chandler','10','6')
patient5=Patient('Rachel','8','4')

heap=MinHeap()

print('Esta vacio? ' + str(heap.is_empty()))
print('Tamaño actual: ' + str(heap.size()))

emergency_room1=Emergency_room(patient1)
emergency_room2=Emergency_room(patient2)
emergency_room3=Emergency_room(patient3)
emergency_room4=Emergency_room(patient4)

print('Insertamos nodo ')
heap.push(emergency_room1)
print('Tamaño actual: ' + str(heap.size()))
print("Parent: ",heap.peek())
print(heap.__str__())

print('Insertamos nodo ')
heap.push(emergency_room2)
print('Tamaño actual: ' + str(heap.size()))
print("Parent: ",heap.peek())
print(heap.__str__())


print('Insertamos nodo ')
heap.push(emergency_room3)
print('Tamaño actual: ' + str(heap.size()))
print("Parent: ",heap.peek())
print(heap.__str__())

print('Insertamos nodo ')
heap.push(emergency_room4)
print('Tamaño actual: ' + str(heap.size()))
print("Parent: ",heap.peek())
print(heap.__str__())
