def song_decoder(song):
    song = song.split('WUB')
    print(len(song))
    i=0
    while i < len(song):
        if song[i]=="":
            song.pop(i)
        i+=1     
    
    for i , word in enumerate(song):
        if word == "":
            song.pop(i)
            
    
    oldsong= ""
    
    print(song)
    print(oldsong)
    return oldsong