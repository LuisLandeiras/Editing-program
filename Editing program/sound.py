from pydoc import plain
from pydub import AudioSegment
from pydub.playback import play

#This function get:
#time -> time in seconds to start music
#bost -> volume bost
def music(filename, bost, first, end, frame, savefile):
    song = AudioSegment.from_mp3(filename)
    if (frame == 0):
        song.frame_rate = song.frame_rate
    else:
        song.frame_rate = frame
    if (end == 0 or first > end or first == end == 0):
        first_seconds = 0
        last_seconds = song.frame_count()
    else:
        first_seconds = first * 1000
        last_seconds = end * 1000
    song = song[:] + bost
    song[first_seconds:last_seconds].export(savefile, format =  "mp3")
    play(song[first_seconds: last_seconds])
