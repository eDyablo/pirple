package eyablonsky.pirple.java.DataStructures;

import java.util.*;

/*
Homework assignment for the 'Fundamentals of Java' course by Pirple.

Written by Ed Yablonsky.

It prints out the set of the attributes for a favorite song.
*/

public class Program {
    public static void main(final String[] args) {
        Map<String, Object> songData = new HashMap<String, Object>();
        songData.put("ContentRating", 'G');// G - general audiences, M - mature audiences, R - restricted persons, X - adults only
        songData.put("Loudness",0.7f); // The higher the value, the louder the song
        songData.put("BitsPerMinute", 83); // The tempo of the song
        songData.put("Duration", 3 * 60 + 11); // The length of the song in seconds
        songData.put("Album", "Stones and Honey"); // The name of the album
        songData.put("Artist", "The Hardkiss"); // The name of the performer
        songData.put("Genre", "Pop");
        songData.put("Title", "Strange Moves (feat. Kazaky)"); // The name of the song
        songData.put("Year", "2014"); // The release year of the recording
        
        for (String key: songData.keySet()) {
            System.out.println(key + ": " + songData.get(key).toString());
        }
    }
}
