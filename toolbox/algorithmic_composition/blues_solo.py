""" Synthesizes a blues solo algorithmically """

from Nsound import *
import numpy as np
from random import choice

def add_note(out, instr, key_num, duration, bpm, volume):
    """ Adds a note from the given instrument to the specified stream

        out: the stream to add the note to
        instr: the instrument that should play the note
        key_num: the piano key number (A 440Hzz is 49)
        duration: the duration of the note in beats
        bpm: the tempo of the music
        volume: the volume of the note
	"""
    freq = (2.0**(1/12.0))**(key_num-49)*440.0
    stream = instr.play(duration*(60.0/bpm),freq)
    stream *= volume
    out << stream

# this controls the sample rate for the sound file you will generate
sampling_rate = 44100.0
Wavefile.setDefaults(sampling_rate, 16)

bass = GuitarBass(sampling_rate)	# use a guitar bass as the instrument
solo = AudioStream(sampling_rate, 1)

""" these are the piano key numbers for a 3 octave blues scale in A
	See: http://en.wikipedia.org/wiki/Blues_scale """
blues_scale = [25, 28, 30, 31, 32, 35, 37, 40, 42, 43, 44, 47, 49, 52, 54, 55, 56, 59, 61]

blues_tonic = [0, 6, 12, 18]
beats_per_minute = 45				# Let's make a slow blues solo
#starts in tonic note
curr_note = choice(blues_tonic)
print curr_note
add_note(solo, bass, blues_scale[curr_note], 1.0, beats_per_minute, 1.0)

##using 6 licks
licks = [ [ [1,0.5], [1,0.5], [1, 0.5], [1, 0.5] ],[ [-1,0.5],[-1,0.5],[-1,0.5],[-1,0.5] ],[ [1, 0.25],[1, 0.25],[1, 0.5],[1, 1.0] ],[ [1,0.3],[-3,0.7],[2,0.5],[1,0.5] ], [ [-2, 0.5*1.1], [-2, 0.5*0.9], [-2, 0.5*1.1], [-2, 0.5*0.9] ],[ [1, 0.5*1.1], [1, 0.5*0.9], [1, 0.5*1.1], [1, 0.5*0.9] ]  ]
for i in range(20):
    lick = choice(licks)
    volume=1.0
    
    for note in lick:
        
        curr_note += note[0]
        #cresendo
        volume+=0.3

        ##if the note is lower than 0 make the note to 0
        if curr_note<0:
            curr_note=0
        ##elif note is biger than the index make the note to 18
        elif curr_note>len(blues_scale)-1:
            curr_note=len(blues_scale)-1
        
        add_note(solo, bass, blues_scale[curr_note], note[1], beats_per_minute, volume)

backing_track = AudioStream(sampling_rate, 1)
Wavefile.read('backing.wav', backing_track)

m = Mixer()

solo *= 0.5             # adjust relative volumes to taste
backing_track *= 2.0

m.add(2.25, 0, solo)    # delay the solo to match up with backing track    
m.add(0, 0, backing_track)

m.getStream(500.0) >> "slow_blues.wav"

beats_per_minute = 45				# Let's make a slow blues solo

add_note(solo, bass, blues_scale[0], 1.0, beats_per_minute, 1.0)

solo >> "blues_solo.wav"

