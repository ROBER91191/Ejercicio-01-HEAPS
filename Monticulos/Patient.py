class Patient:
    

    def __init__(self,name,urgency_level,wait_hours):

        self.urgency_level=urgency_level
        self.wait_hours=wait_hours
        self.name=name


    def compare_to(self, patient1):

        if self.urgency_level > patient1.urgency_level:
            return 1
        elif self.urgency_level < patient1.urgency_level:
            return -1
        else:
            return 0


    def equals(self, patient1) -> bool:

        if self>patient1:
            resultado = True
        # Aquí irían los criterios de igualdad
        return resultado
    
    def __str__(self):
        return str(self.urgency_level ) + ' ' + self.name + ' ' +  str(self.wait_hours)


    def __lt__(self, other):
        '''
        Sobrecarga del operador < para comparar empleados según su número identificador.

        :param other: Otro objeto Empleado para la comparación.
        :return: True si este empleado tiene un número identificador menor que 'other'.
        '''

        if self.urgency_level==10 and other.urgency_level==10:
            if self.wait_hours<other.wait_hours:
                return True

        # if other.urgency_level == 10:
        #     return True

        # # Regla 2: Si no hay pacientes con urgencia máxima y han esperado más de 5 horas, atenderlos
        # if other.urgency_level==0 and other.wait_hours > 5:
        #     return True
        
        return self.urgency_level < other.urgency_level


    def __le__(self, other):
        '''
        Sobrecarga del operador <= para comparar empleados según su número identificador.

        :param other: Otro objeto Empleado para la comparación.
        :return: True si este empleado tiene un número identificador menor o igual que 'other'.
        '''
        return self.urgency_level <= other.urgency_level


    def __gt__(self, other):
        '''
        Sobrecarga del operador > para comparar empleados según su número identificador.

        :param other: Otro objeto Empleado para la comparación.
        :return: True si este empleado tiene un número identificador mayor que 'other'.
        '''
        return self.urgency_level > other.urgency_level
    


    # Comentado ya que parece haber un error en la implementación
    def __ge__(self, other):
        '''
        Sobrecarga del operador >= para comparar empleados según su número identificador.

        :param other: Otro objeto Empleado para la comparación.
        :return: True si este empleado tiene un número identificador mayor o igual que 'other'.
        '''
        return self.urgency_level >= other.urgency_level

    def __eq__(self, other):
        '''
        Sobrecarga del operador == para comparar empleados según su número identificador.

        :param other: Otro objeto Empleado para la comparación.
        :return: True si este empleado tiene un número identificador igual a 'other'.
        '''
        return self.urgency_level == other.urgency_level

    def __ne__(self, other):
        '''
        Sobrecarga del operador != para comparar empleados según su número identificador.

        :param other: Otro objeto Empleado para la comparación.
        :return: True si este empleado tiene un número identificador distinto de 'other'.
        '''
        return not(self.__eq__(other))