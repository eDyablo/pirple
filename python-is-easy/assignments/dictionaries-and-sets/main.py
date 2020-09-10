'''
Homework assignment for the 'Python is easy' course by Pirple.

Written be Ed Yablonsky.

It prints out the set of the attributes for one favorite song.
'''

SongData = {
    'Album': 'Stones and Honey', # The name of the album
    'Artist': 'The Hardkiss', # The name of the performer
    'BitsPerMinute': 83, # The tempo of the song
    'Duration': 3 * 60 + 11, # The length of the song in seconds
    'Genre': 'Pop',
    'Loudness': 0.7, # The higher the value, the louder the song
    'Title': 'Strange Moves (feat. Kazaky)', # The name of the song
    'Year': '2014', # The release year of the recording
}

for attribute in SongData:
    print(attribute + ': ' + str(SongData[attribute]))

# Extra credit

'''
Guess if the song data has an attribute with specific value.

Returns True when the song data contains the specified attribute
and its value is equal to the specified one. And returns False otherwise.
It compares textual representation of the values to allow to specify
value with the type different to the one that stored in the data.
'''
def guess(attribute, value):
    return attribute in SongData and str(SongData[attribute]) == str(value)
