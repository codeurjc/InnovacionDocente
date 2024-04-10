package es.codeurjc.test.exam.Twitter;

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