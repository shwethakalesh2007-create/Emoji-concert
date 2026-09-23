import winsound
import random
import time

# Emoji → (frequency Hz, duration ms)
emoji_beats = {
    "🥁": (300, 300),
    "🎹": (500, 300),
    "🎸": (700, 300),
    "🎺": (900, 300),
    "🎻": (600, 400),
    "🎷": (400, 500)
}

print("🎵 Music Concert 🎵")
print()

# Choose song length
print("Choose your song length:")
print("1. 4 emojis")
print("2. 8 emojis")
print("3. 12 emojis")
print("4. 16 emojis")
print("5. 25 emojis")

choice = input("\nEnter your choice: ")

if choice == "1":
    song_length = 4
elif choice == "2":
    song_length = 8
elif choice == "3":
    song_length = 12
elif choice == "4":
    song_length = 16
elif choice == "5":
    song_length = 25
else:
    print("Invalid choice! Using 8 emojis.")
    song_length = 8


# Choose speed
print("\nChoose your concert speed:")
print("1. Slow")
print("2. Normal")
print("3. Fast")
print("4. Super Fast")

speed_choice = input("\nEnter your choice: ")

if speed_choice == "1":
    speed = 1.5
elif speed_choice == "2":
    speed = 1
elif speed_choice == "3":
    speed = 0.5
elif speed_choice == "4":
    speed = 0.35
else:
    print("Invalid choice! Using normal speed.")
    speed = 1


# Replay the concert
while True:

    # Create a random song
    song = [
        random.choice(list(emoji_beats.keys()))
        for _ in range(song_length)
    ]

    # Show the song
    print("\n🎶 Your Song:")
    print(" ".join(song))

    print("\n🎵 Playing...\n")

    # Play each emoji
    for emoji in song:
        print("Playing:", emoji)

        freq, dur = emoji_beats[emoji]

        # Change duration according to speed
        new_duration = int(dur * speed)

        winsound.Beep(freq, new_duration)

        time.sleep(0.2 * speed)

    print("\n🎉 Concert finished!")

    # Ask if the user wants another song
    again = input("\n🎵 Play another round? (y/n): ")

    if again.lower() != "y":
        print("\nThanks for attending the concert! 🎶")
        break
