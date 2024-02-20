### PROMPT: 

Desarrolla un test que compruebe que al pasarle al método posibleMatricula de la clase GestorMatricula el ID de un alumno cuyas notas son 9.5, 10 y 9 a posibleMatricula, esta función devuelve true. 

```java
public class GestorMatricula {
   private BaseDatosAlumnos alumnos;
 
   public GestorMatricula(BaseDatosAlumnos alumnos){
      this.alumnos = alumnos;
   }
 
   public boolean posibleMatricula(long idAlumno){
      double[] notas = this.alumnos.getNotas(idAlumno);
      double suma = 0;
      for(double nota : notas){
         suma += nota;
      }
      return suma >= notas.length * 9.5;
   }
  
}
```

### OUTPUT:

## Test para el método `posibleMatricula`

```java
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class GestorMatriculaTest {

    @Test
    void testPosibleMatriculaConNotasAltas() {
        // Arrange
        long idAlumno = 12345;
        double[] notas = {9.5, 10, 9};
        BaseDatosAlumnos mockBDAlumnos = mock(BaseDatosAlumnos.class);
        when(mockBDAlumnos.getNotas(idAlumno)).thenReturn(notas);
        GestorMatricula gestorMatricula = new GestorMatricula(mockBDAlumnos);

        // Act
        boolean resultado = gestorMatricula.posibleMatricula(idAlumno);

        // Assert
        assertTrue(resultado, "El método posibleMatricula debería devolver true para un alumno con notas 9.5, 10 y 9");
    }
}
```

**Explicación del test:**

1. **Arrange:** Se crea un objeto `GestorMatricula` con un mock de `BaseDatosAlumnos`. Se define un ID de alumno (`idAlumno`) y un array de notas (`notas`) que representan un alumno con notas altas. Se configura el mock para que devuelva las notas cuando se le pida el ID del alumno.
2. **Act:** Se llama al método `posibleMatricula` del `GestorMatricula` con el ID del alumno como parámetro.
3. **Assert:** Se comprueba que el resultado del método `posibleMatricula` es `true`.

**Mejoras del test:**

* Se pueden añadir más tests para probar diferentes casos, como:
    * Un alumno con notas que no alcanzan la media.
    * Un alumno con notas negativas.
    * Un alumno con una sola nota.
* Se pueden utilizar herramientas de testing para automatizar la ejecución del test.

**Nota:** Este es un ejemplo básico de un test unitario. Se pueden añadir más assertions para verificar diferentes aspectos del comportamiento del método `posibleMatricula`.
