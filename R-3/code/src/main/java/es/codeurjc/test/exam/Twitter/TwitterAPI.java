package es.codeurjc.test.exam.Twitter;

public interface TwitterAPI {

    public boolean isValidTweet(String tweet);

    public void publishTweet(String tweet);
    
}