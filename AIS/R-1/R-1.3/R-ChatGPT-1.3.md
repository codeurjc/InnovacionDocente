### PROMPT: 

Describe la diferencia entre un test unitario sociable y un test unitario solitario

### OUTPUT:

La diferencia entre un test unitario sociable y un test unitario solitario radica en el alcance y la complejidad de las interacciones que el test tiene con los componentes del sistema bajo prueba. Aquí tienes una descripción de cada uno:

1. **Test Unitario Sociable**:
   - Un test unitario sociable evalúa el comportamiento de un componente (como una clase o un módulo) en relación con sus dependencias externas, que pueden ser otros componentes, servicios, bases de datos, etc.
   - Estos tests interactúan con las dependencias del componente bajo prueba, aunque generalmente se utilizan "dobles" (mocks, stubs, fakes) en lugar de las implementaciones reales de las dependencias.
   - El objetivo es probar la interacción entre el componente y sus dependencias externas, así como asegurarse de que el componente se comporte correctamente ante diferentes escenarios.
   - Estos tests suelen ser más integradores que los tests unitarios solitarios, ya que implican la interacción con otros componentes.

2. **Test Unitario Solitario**:
   - Un test unitario solitario se centra en evaluar el comportamiento de un componente de manera aislada, sin interactuar con sus dependencias externas.
   - Las dependencias externas se simulan o se utilizan objetos de prueba (fakes) que imitan el comportamiento de las dependencias reales, pero no realizan ninguna acción externa ni dependen de servicios externos.
   - El objetivo es probar la lógica interna y el comportamiento del componente de forma independiente de su entorno externo.
   - Estos tests suelen ser más simples y rápidos de ejecutar que los tests unitarios sociables, ya que no requieren la configuración ni el uso de componentes externos.

En resumen, mientras que un test unitario sociable evalúa cómo interactúa un componente con sus dependencias externas, un test unitario solitario se centra en probar el comportamiento del componente de forma aislada, sin considerar su entorno externo. Ambos enfoques son importantes y se utilizan según las necesidades específicas de la aplicación y del componente bajo prueba.