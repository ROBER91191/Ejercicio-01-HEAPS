
## GITHUB: https://github.com/ROBER91191/Ejercicio-01-HEAPS.git

# Nombre
### Roberto Serpa Olivera


# Exlpicación

### He creado crado pacientes, inicializando con el nombre, nivele de urgencia y horas de espera, he añadido 20 pacientes a una lista de pacientes, después de esto he añadido esa lista de espera a cada montículo (maxHeap, minHeap).
### Hemos creado una sala de mergencia en la que les pasamos como constructor los montículos creados anteriormente.

### Una vez tenemos la sala de espera con nuestros 20 pacientes, lo que hacemos es desencolar cada montidulo el MaxHeap vamos atendiendo a pacientes cuyo nivel de urgencia sea mayor, y en caso de coincidir miramos el timepo de espera del paciente y el que lleve mas tiempo se le atiende. En el minHeap atendemos a los pacientes atendiendo al tiempo de espera, el que tiene un mayor tiempo de espera (12-tiempo espera paciente)se le atiende antes.

### Métodos creados:
### def emergency_room(list_patients) => Añadimos los pacientes a los monticulos
### def patient_urgency_level(list_heap) => Imprimimos los pacientes por orden de urgencia
### def patient_wait_hours(list_heap) => Imprimimos los pacientes por orden de horas de espera
### if __name__ == '__main__'=> Ejecutamos el código

Método del Paciente para verificar las condiciones de urgencia
    def __lt__(self, other):
        '''
        Sobrecarga del operador < para comparar empleados según su número identificador.

        :param other: Otro objeto Empleado para la comparación.
        :return: True si este empleado tiene un número identificador menor que 'other'.
        '''

        if self.urgency_level==10 and other.urgency_level==10:
            if self.wait_hours<other.wait_hours:
                return True
            return False
        
        if self.urgency_level==other.urgency_level:
                if self.wait_hours<other.wait_hours:
                        return True
                return False
				
        return self.urgency_level < other.urgency_level


Método del Paciente para verificar las condiciones de horas de espera
    def __gt__(self, other):
        '''
        Sobrecarga del operador > para comparar empleados según su número identificador.

        :param other: Otro objeto Empleado para la comparación.
        :return: True si este empleado tiene un número identificador mayor que 'other'.
        '''
        total_wait_hours_father=12-self.wait_hours
        total_wait_hour_child=12-other.wait_hours
        if total_wait_hours_father==total_wait_hour_child:
                if self.urgency_level>other.urgency_level:
                        return True
                return False
        
        return total_wait_hours_father > total_wait_hour_child

### NOTA: No he podido realizar el proceso de desencolar los monticulos, de cuando eliminas un paciente en un montículo que se elimine en otro.
