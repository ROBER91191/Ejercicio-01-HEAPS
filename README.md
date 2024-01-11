Ejercicio de Feedback 01. Montículos
Ejercicio: Sistema de Prioridades en una Sala de Emergencias con Montículos Máx y Mín

### Contexto:

Te encuentras a cargo de la administración de una sala de emergencias en un hospital. Los pacientes que ingresan a esta sala tienen distintos niveles de urgencia, y es crucial que sean atendidos en función de estas prioridades.

Para gestionar la atención de estos pacientes, decides implementar dos montículos: uno máximo y uno mínimo.

Montículo Máximo: Representa la urgencia de atención médica. Cuanto más alta sea la urgencia, más alto es el valor. Este montículo permite desencolar rápidamente al paciente de mayor prioridad.
Montículo Mínimo: Representa el tiempo de espera de los pacientes. Cuanto más tiempo ha esperado un paciente, más pequeño es el valor (indicando horas desde su llegada). Este montículo te permite identificar rápidamente a aquellos pacientes que han estado esperando demasiado, independientemente de su nivel de urgencia.
Tareas:

### Implementación:
Diseña las clases Paciente (con atributos como nombre, nivel_urgencia y horas_espera) y SalaEmergencias (con los montículos max y min como atributos, y métodos para gestionarlos).
Simulación:
Genera una lista de pacientes aleatorios con niveles de urgencia y tiempos de espera variados.
Añade estos pacientes a la SalaEmergencias, asegurando que sean incorporados a ambos montículos.
Atención:
Desencola y atiende a los pacientes siguiendo estas reglas:
Si hay pacientes con un nivel de urgencia de 10 (el más alto), atiéndelos inmediatamente.
Si no hay pacientes con urgencia máxima, pero hay pacientes que han esperado más de 5 horas, atiéndelos.
En caso contrario, atiende al paciente con la mayor urgencia.
Reporte:
Luego de simular la atención de 20 pacientes, genera un reporte que muestre los pacientes atendidos, en qué orden y después de cuánto tiempo de espera.

### Formato de entrega:
Debes utilizar Git y GitHub para gestionar las versiones de tu código. En el repositorio deberás incorporar un fichero README.md en el que aparezcan tu nombre y apellidos y una explicación y reflexión acerca del proyecto realizado. Recuerda incorporar, al principio del fichero README el link al repositorio de GitHub.

En esta entrega a través del campus deberás enviar el repositorio exportado en formato ZIP. 