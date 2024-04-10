package es.codeurjc.test.exam.Twitter;

import static org.junit.jupiter.api.Assertions.assertDoesNotThrow;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.never;
import static org.mockito.Mockito.times;
import static org.mockito.Mockito.verify;
import static org.mockito.Mockito.when;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

public class TwitterTest {

    public TwitterAPI api;
    public Twitter twitter;

    public String VALID_TWEET = "This is a valid tweet";
    public String NO_VALID_TWEET = "This is a NOT valid tweet";

    @BeforeEach
    public void setUp() {
        api = mock(TwitterAPI.class);
        twitter = new Twitter(api);
    }

    @Test
    public void validTweetTest() {

        when(api.isValidTweet(VALID_TWEET)).thenReturn(true);
        
        assertDoesNotThrow(() -> 
            twitter.sendTweet(VALID_TWEET)
        );

        verify(api).isValidTweet(VALID_TWEET);
        verify(api, times(1)).publishTweet(VALID_TWEET);
    }

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
    
}
