package es.codeurjc.test.exam.Wordle;

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
