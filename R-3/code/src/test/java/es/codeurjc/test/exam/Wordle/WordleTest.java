package es.codeurjc.test.exam.Wordle;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.never;
import static org.mockito.Mockito.times;
import static org.mockito.Mockito.verify;
import static org.mockito.Mockito.when;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

public class WordleTest {

    private WordleAPI api;
    private Wordle wordle;

    @BeforeEach
    public void setUp() {
        api = mock(WordleAPI.class);
        wordle = new Wordle(api);
    }

    @Test
    public void wordleTest() {
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

    @Test
    public void wordleTest_error(){

        RuntimeException ex = assertThrows(RuntimeException.class, () -> {
            wordle.checkWord("UNO");
        });

        assertEquals("La palabra debe tener 5 letras", ex.getMessage());
        
        verify(api, never()).getWord();

    }
    
}
