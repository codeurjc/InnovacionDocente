# Innovación Docente: Uso de IA para la resolución de preguntas y ejercicios

## 1. Preguntas de teoría

*Descripción*: El alumno contara con una pregunta similar a la que se puede encontrar en un exámen que verse sobre un concepto de la teoría. Esta pregunta deberá poder responderse de manera concisa con el material de clase.

IAs a utilizar:

- [Microsoft Copilot (cuenta de la universidad)](https://copilot.microsoft.com/) 
- [Google Gemini](https://gemini.google.com/)
- [ChatGPT (3.5)](https://chat.openai.com/)

>**Pregunta 1.1:** *Explica las diferencias entre un test de caja blanca y un test de caja negra.*

- **R-Propia-1.1:** *Los test de caja blanca se escriben considerando cómo está construido el software bajo pruebas internamente, mientras que en un test de caja negra solo se cuenta con la descripción de la funcionalidad observable del software bajo pruebas.*


- [**R-Gemini-1.1**](R-1/R-1.1/R-Gemini-1.1.md): Respuesta larga y detallada


- [**R-Copilot-1.1**](R-1/R-1.1/R-copilot-1.1.md): Respuesta larga y detallada con imágenes


- [**R-ChatGPT-1.1**](R-1/R-1.1/R-ChatGPT-1.1.md): Respuesta larga y detallada


>**Pregunta 1.2:** *¿En qué consiste una regresión software?*

- **R-Propia-1.1:** Es una pérdida de una funcionalidad existente a consecuencia de un nuevo código añadido en el software

- [**R-Gemini-1.2:**](R-1/R-1.2/R-Gemini-1.2.md): Respuesta larga y detallada

*En el desarrollo de software, una regresión se refiere a la introducción accidental de errores o defectos en el software como resultado de un cambio realizado en el código. Este cambio puede ser una nueva función, una corrección de errores o incluso una simple modificación en la configuración [...]*

- [**R-Copilot-1.2:**](R-1/R-1.2/R-Copilot-1.2.md): Respuesta larga y detallada -> No responde a qué es una regresión, si no qué es un test de regresión

- [**R-ChatGPT-1.2:**](R-1/R-1.2/R-ChatGPT-1.2.md): Respuesta larga y detallada

*La regresión de software es un fenómeno que ocurre cuando un cambio en el código o en la configuración de un sistema provoca que una funcionalidad que antes funcionaba correctamente deje de hacerlo. En otras palabras, es la reaparición de errores previamente corregidos o el surgimiento de nuevos problemas como resultado de cambios en el software.*

> **Pregunta 1.3:** *Describe la diferencia entre un test unitario sociable y un test unitario solitario*

- **R-Propia-1.3:** En un test unitario solitario todas las dependencias son sustituidas por dobles, mientras que en un test solitario sociale, solo se utilizan dobles cuando las dependencias acceden a disco o a otros sistemas vía red.

- [**R-Gemini-1.3:**](R-1/R-1.3/R-Gemini-1.3.md) Respuesta larga y detallada, pero que contiene errores: no se especifica que en los sociables habría que dejar fuera aquellas dependencias que aumentan el tiempo de ejecución) 

- [**R-Copilot-1.3:**](R-1/R-1.3/R-Copilot-1.3.md)  R-Copilot-1.3.txt  (respuesta larga y detallada, pero le faltan detalles concretos)

- [**R-ChatGPT-1.3:**](R-1/R-1.3/R-ChatGPT-1.3.md) R-Chat GPT-1.3.txt (respuesta larga y detallada, pero contiene errores: no se especifica que en los sociables habría que dejar fuera aquellas dependencias que aumentan el tiempo de ejecución) 

## 2. Explicar un código

*Descripción*: El alumno contará con un código y deberá describir cuál es su función. Este código no ha sido presentado en las diapositivas, pero será similar.


> **Pregunta 2.1:** Describe detalladamente lo que hace el siguiente código

**C-2.1**
``` java
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

- [**R-Gemini-2.1:**](R-2/R-2.1/R-Gemini-2.1.md)

> **Pregunta 2.2:** Describe detalladamente lo que hace el siguiente código

**C-2.2**

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

- [**R-Gemini-2.2:**](R-2/R-2.2/R-Gemini-2.2.md)

> **Pregunta 2.3:** Describe detalladamente lo que hace el siguiente código

**C-2.3**

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

- [**R-Gemini-2.3:**](R-2/R-2.3/R-Gemini-2.3.md)

## 3. Pregunta cuya respuesta sea un código

*Descripción*: El alumno contará con un enunciado (que puede contener o no código base) y deberá desarrollar una solución escribiendo código. Idealmente, deberá ser una pregunta que requiera comprender la asignatura


> **Pregunta 3.1:** Desarrolla un test que compruebe que al pasarle al método posibleMatricula de la clase GestorMatricula el ID de un alumno cuyas notas son 9.5, 10 y 9 a posibleMatricula, esta función devuelve true. 

**C-3.1**
``` java
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


**R-Propia-3.1**
```java
@Test
public void test(){
       // GIVEN
       BaseDatosAlumnos bd = mock(BaseDatosAlumnos.class);
       GestorMatricula gestor = new GestorMatricula(bd);
       double[] notas = {10.0, 10.0, 10.0};
       when(bd.getNotas(anyLong())).thenReturn(notas);
       long fakeID = 1L;
       // WHEN
       boolean matriculaConcedida = gestor.posibleMatricula(fakeID);
       // THEN
       assertTrue(matriculaConcedida);
       verify(bd).getNotas(fakeID);
}
```
- [**R-Gemini-3.1:**](R-3/R-3.1/R-Gemini-3.1.md)

> **Pregunta 3.2:** Desarrolla un test que compruebe que al pasarle al método sendTweet de la clase Twitter un String que representa el tweet, si este tiene no cumple con los requisitos de validación (un tamaño máximo), entonces se lanza una excepción

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

**R-Propia-3.2**
```java
@Test
public void inValidTweetTest() {

    when(api.isValidTweet(NO_VALID_TWEET)).thenReturn(false);

    IllegalArgumentException ex = assertThrows(IllegalArgumentException.class, () -> 
        twitter.sendTweet(NO_VALID_TWEET)
    );

    assertEquals("Tweet too long", ex.getMessage());

    verify(api).isValidTweet(NO_VALID_TWEET);
    verify(api, never()).publishTweet(NO_VALID_TWEET);
}
```

- [**R-Gemini-3.2:**](R-3/R-3.2/R-Gemini-3.2.md)

> **Pregunta 3.3:** Desarrolla un test que compruebe el funcionamiento de de checkWord de la clase Wordle cuando el usuario introduce las parabras AUREO, CESTO y SESGO, siendo la palabra a adivinar SESGO.

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

**R-Propia-3.3**

```java 
@Test
public void wordleTest() {

    WordleAPI api = mock(WordleAPI.class);
    Wordle wordle = new Wordle(api);

    when(api.getWord()).thenReturn("SESGO");
    
    char[] result1 = wordle.checkWord("AUREO");
    char[] expected1 = {'X', 'X', 'X', '-', 'O'};
    assertArrayEquals(expected1, result1);

    char[] result2 = wordle.checkWord("CESTO");
    char[] expected2 = {'X', 'O', 'O', 'X', 'O'};
    assertArrayEquals(expected2, result2);

    char[] result3 = wordle.checkWord("SESGO");
    char[] expected3 = {'O', 'O', 'O', 'O', 'O'};
    assertArrayEquals(expected3, result3);
    
    verify(api, times(3)).getWord();
}
```

- [**R-Gemini-3.3:**](R-3/R-3.3/R-Gemini-3.3.md)

