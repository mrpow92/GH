def song_decoder(song):
    song = song.split('WUB')
    song = [n for n in song if n != ""]
    return " ".join(song)



    
import codewars_test as Test
Test.assert_equals(song_decoder("AWUBBWUBC"), "A B C","WUB should be replaced by 1 space")
Test.assert_equals(song_decoder("AWUBWUBWUBBWUBWUBWUBC"), "A B C","multiples WUB should be replaced by only 1 space")
Test.assert_equals(song_decoder("WUBAWUBBWUBCWUB"), "A B C","heading or trailing spaces should be removed")