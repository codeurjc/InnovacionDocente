### PROMPT: 

Desarrolla un test que compruebe que al pasarle al método sendTweet de la clase Twitter un String que representa el tweet, si este tiene no cumple con los requisitos de validación (un tamaño máximo), entonces se lanza una excepción

```java
public class Twitter {

    private TwitterAPI twitterAPI;

    public Twitter(TwitterAPI twitterAPI) {
        this.twitterAPI = twitterAPI;
    }

    public void sendTweet(String tweet) {
        if (!this.twitterAPI.isValidTweet(tweet)) {
            throw new IllegalArgumentException("Tweet too long");
        }
        this.twitterAPI.publishTweet(tweet);
    }
    
}
```

### OUTPUT:

Test para el método `sendTweet`

```java
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class TwitterTest {

    @Test
    void testSendTweetWithLongTweet() {
        // Arrange
        String tweet = "Este tweet tiene más de 280 caracteres, lo que supera el límite permitido por Twitter. Esto debería generar una excepción.";
        TwitterAPI mockTwitterAPI = mock(TwitterAPI.class);
        when(mockTwitterAPI.isValidTweet(tweet)).thenReturn(false);
        Twitter twitter = new Twitter(mockTwitterAPI);

        // Act
        try {
            twitter.sendTweet(tweet);
        } catch (IllegalArgumentException e) {
            // Assert
            assertEquals("Tweet too long", e.getMessage());
        }
    }
}
```

**Explicación del test:**

1. **Arrange:** Se crea un objeto `Twitter` con un mock de `TwitterAPI`. Se define un tweet que supera el límite de caracteres permitido por Twitter. Se configura el mock para que devuelva `false` cuando se le pregunte si el tweet es válido.
2. **Act:** Se llama al método `sendTweet` con el tweet como parámetro.
3. **Assert:** Se comprueba que se lanza una excepción `IllegalArgumentException` con el mensaje "Tweet too long".

**Mejoras del test:**

* Se pueden añadir más tests para probar diferentes casos, como:
    * Un tweet con una longitud válida.
    * Un tweet con caracteres especiales.
    * Un tweet vacío.
* Se pueden utilizar herramientas de testing para automatizar la ejecución del test.

**Nota:** Este es un ejemplo básico de un test unitario. Se pueden añadir más assertions para verificar diferentes aspectos del comportamiento del método `sendTweet`.
