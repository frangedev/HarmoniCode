import random
from music21 import stream, note, chord, scale, meter, tempo, instrument, midi

# Function to generate a melody with a rhythmic motif
def generate_melody(length, scale_obj):
    melody = stream.Part()
    melody.insert(0, instrument.Piano())  # Piano as the instrument
    
    # Define a simple rhythmic motif (e.g., quarter, eighth, eighth)
    motif = [0.5, 0.25, 0.25]
    durations = [0.25, 0.5, 1.0]  # Base durations for variation
    
    for i in range(length):
        # Apply motif periodically, otherwise random duration
        if i % 3 == 0 and i + len(motif) <= length:
            for dur in motif:
                pitch = random.choice(scale_obj.getPitches())
                n = note.Note(pitch, quarterLength=dur)
                melody.append(n)
        else:
            pitch = random.choice(scale_obj.getPitches())
            dur = random.choice(durations)
            n = note.Note(pitch, quarterLength=dur)
            melody.append(n)
    
    return melody

# Function to generate a chord progression
def generate_chord_progression(key, length):
    chords = stream.Part()
    chords.insert(0, instrument.Piano())
    
    scale_obj = scale.MajorScale(key)
    pitches = scale_obj.getPitches()
    
    # I-IV-V-I progression with some variation
    progression = [
        [pitches[0], pitches[2], pitches[4]],  # I
        [pitches[3], pitches[5], pitches[7]],  # IV
        [pitches[4], pitches[6], pitches[1]],  # V
        [pitches[0], pitches[2], pitches[4]]   # I
    ]
    
    for i in range(length):
        chord_pitches = progression[i % len(progression)]
        # Add some variation with inversions occasionally
        if random.random() > 0.7:  # 30% chance of inversion
            chord_pitches = chord_pitches[1:] + [chord_pitches[0]]
        c = chord.Chord(chord_pitches, quarterLength=2.0)
        chords.append(c)
    
    return chords

# Main function to compose and export music
def harmonicode_compose(filename="harmonicode_output.mid"):
    # Get user input
    key = input("Enter the key (e.g., 'C', 'G', 'F#'): ").strip() or 'C'
    try:
        bpm = int(input("Enter tempo (BPM, e.g., 120): ") or 120)
    except ValueError:
        bpm = 120
    
    # Create a score
    score = stream.Score()
    score.insert(0, tempo.MetronomeMark(number=bpm))
    score.insert(0, meter.TimeSignature('4/4'))
    
    # Validate and set scale
    try:
        major_scale = scale.MajorScale(key)
    except:
        print(f"Invalid key '{key}', defaulting to C Major")
        major_scale = scale.MajorScale('C')
    
    # Generate melody and chords
    melody = generate_melody(length=16, scale_obj=major_scale)
    chords = generate_chord_progression(key=key, length=8)
    
    # Add parts to the score
    score.insert(0, melody)
    score.insert(0, chords)
    
    # Export to MIDI
    midi_file = midi.translate.streamToMidiFile(score)
    midi_file.open(filename, 'wb')
    midi_file.write()
    midi_file.close()
    
    print(f"HarmoniCode composition saved as {filename}")
    # score.show()  # Uncomment to display score if GUI is available

# Run the composer
if __name__ == "__main__":
    # Requires music21: pip install music21
    print("Welcome to HarmoniCode - Your Algorithmic Music Composer!")
    harmonicode_compose("harmonicode_composition.mid")