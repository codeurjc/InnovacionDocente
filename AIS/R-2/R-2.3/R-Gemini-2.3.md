### PROMPT: 

Describe detalladamente lo que hace el siguiente código

```java
public class Wordle {
   
  private WordleAPI api;

  public Wordle(WordleAPI api) {
    this.api = api;
  }

  public char[] checkWord(String word) {
    if(word.length() != 5) {
      throw new RuntimeException("La palabra debe tener 5 letras");
    }
    String wordOfTheDay = api.getWord();
    char[] result = new char[5];
    for(int i = 0; i < wordOfTheDay.length(); i++) {
      if(word.charAt(i) == wordOfTheDay.charAt(i)) {
        result[i] = 'O';
      }else if(wordOfTheDay.contains(String.valueOf(word.charAt(i)))) {
        result[i] = '-';
      }else{
        result[i] = 'X';
      }
    }
    return result;
  }
}
```

### OUTPUT:

## Explicación del código Wordle en castellano

**Clase Wordle:**

Esta clase define un objeto que simula el juego Wordle. Para funcionar, necesita un objeto que implemente la interfaz `WordleAPI`, la cual se encarga de obtener la palabra del día de una fuente externa (como una API).

**Constructor:**

El constructor recibe como argumento un objeto que implemente la interfaz `WordleAPI`. Este objeto se usará para obtener la palabra del día.

**Método `checkWord`:**

Este método recibe como argumento una palabra y devuelve un array de caracteres. El array indica la cercanía de la palabra a la palabra del día:

* **'O'**: La letra está en la posición correcta.
* **'-'**: La letra está en la palabra del día, pero en otra posición.
* **'X'**: La letra no está en la palabra del día.

**Funcionamiento del método `checkWord`:**

1. **Validación:** Se comprueba que la palabra introducida tenga 5 letras. Si no es así, se lanza una excepción.
2. **Obtención de la palabra del día:** Se utiliza el objeto `WordleAPI` para obtener la palabra del día.
3. **Comprobación de las letras:** Se recorren las letras de la palabra introducida y se comparan con las letras de la palabra del día.
4. **Generación del resultado:** Se crea un array de caracteres con el resultado de la comparación.

**Ejemplo:**

Si la palabra del día es "casa" y se introduce la palabra "carro", el método `checkWord` devolvería el array `['O', '-', 'X', '-', 'X']`. Esto indica que la letra "c" está en la posición correcta, la letra "a" está en la palabra del día pero en otra posición, y las letras "r" y "o" no están en la palabra del día.

**En resumen:**

El código anterior define una clase que simula el juego Wordle. La clase permite comprobar la cercanía de una palabra a la palabra del día, proporcionando información sobre la posición y existencia de las letras.
