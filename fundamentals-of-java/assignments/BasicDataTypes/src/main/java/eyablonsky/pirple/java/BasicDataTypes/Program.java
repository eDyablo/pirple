package eyablonsky.pirple.java.BasicDataTypes;

/*
Homework assignment for the 'Fundamentals of Java' course by Pirple.

It prints out the set of the attributes for one favorite song.
*/

public class Program {
    public static void main(final String[] args) {
        char ContentRating = 'G'; // G - general audiences, M - mature audiences, R - restricted persons, X - adults only
        float Loudness = 0.7f; // The higher the value, the louder the song
        int BitsPerMinute = 83; // The tempo of the song
        int Duration = 3 * 60 + 11; // The length of the song in seconds
        String Album = "Stones and Honey"; // The name of the album
        String Artist = "The Hardkiss"; // The name of the performer
        String Genre = "Pop";
        String Title = "Strange Moves (feat. Kazaky)"; // The name of the song
        String Year = "2014"; // The release year of the recording
        
        System.out.println(Title);
        System.out.println(Artist);
        System.out.println(Duration);
        System.out.println(Album);
        System.out.println(Year);
        System.out.println(Genre);
        System.out.println(BitsPerMinute);
        System.out.println(Loudness);
        System.out.println(ContentRating);
    }
}
