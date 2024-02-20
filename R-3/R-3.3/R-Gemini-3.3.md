### PROMPT: 

Desarrolla un test que compruebe el funcionamiento de de checkWord de la clase Wordle cuando el usuario introduce las parabras AUREO, CESTO y SESGO, siendo la palabra a adivinar SESGO.

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

### OUTPUT

**Aquí está el test que comprueba el funcionamiento de `checkWord` con las palabras AUREO, CESTO y SESGO, siendo la palabra a adivinar SESGO:**

```java
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class WordleTest {

    @Test
    void testCheckWordConAUREO_CESTO_y_SESGO() {
        // Arrange
        WordleAPI mockWordleAPI = mock(WordleAPI.class);
        when(mockWordleAPI.getWord()).thenReturn("SESGO");
        Wordle wordle = new Wordle(mockWordleAPI);

        // Act y Assert
        assertArrayEquals(new char[]{'X', 'X', '-', 'X', 'X'}, wordle.checkWord("AUREO"));
        assertArrayEquals(new char[]{'-', 'X', 'O', 'X', 'X'}, wordle.checkWord("CESTO"));
        assertArrayEquals(new char[]{'O', 'O', 'O', 'O', 'O'}, wordle.checkWord("SESGO"));
    }
}
```

**Explicación del test:**

1. **Arrange:**
   - Se crea un mock de `WordleAPI` que devuelve "SESGO" como la palabra del día.
   - Se crea un objeto `Wordle` con el mock de `WordleAPI`.

2. **Act y Assert:**
   - Se llama a `checkWord` con la palabra "AUREO" y se comprueba que el resultado es `['X', 'X', '-', 'X', 'X']`.
   - Se llama a `checkWord` con la palabra "CESTO" y se comprueba que el resultado es `['-', 'X', 'O', 'X', 'X']`.
   - Se llama a `checkWord` con la palabra "SESGO" y se comprueba que el resultado es `['O', 'O', 'O', 'O', 'O']` (palabra adivinada).

**Comentarios adicionales:**

- El test utiliza la anotación `@Test` de JUnit para indicar que es un caso de prueba.
- El método `assertArrayEquals` se utiliza para comprobar que dos arrays son iguales.
- El mock de `WordleAPI` permite controlar la palabra del día y evitar llamadas a una API externa.
- Se podrían añadir más tests para probar otros casos, como palabras con diferentes combinaciones de letras o con un número de letras incorrecto.
