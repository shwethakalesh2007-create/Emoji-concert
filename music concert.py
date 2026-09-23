import winsound
import random
import time

# Emoji → (frequency Hz, duration ms)
emoji_beats = {
    "🥁": (300, 300),   # drum = low beat
    "🎹": (500, 300),   # piano = mid tone
    "🎸": (700, 300),   # guitar = high tone
    "🎺": (900, 300),   # trumpet = bright tone
    "🎻": (600, 400),   # violin = longer tone
    "🎷": (400, 500)    # sax = deeper tone
}

print("🎵 Emoji Concert 🎵")

# Make a random "song" of 8 emojis
song = [random.choice(list(emoji_beats.keys())) for _ in range(8)]

# Print the full emoji song
print("Song:", " ".join(song))

# Play each emoji's beat in order
for emoji in song:
    print("Playing:", emoji)
    freq, dur = emoji_beats[emoji]
    winsound.Beep(freq, dur)
    time.sleep(0.2)  # short pause between beats
