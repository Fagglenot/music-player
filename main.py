import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] ="hide"
import pygame

def play_music(folder, filename):
    file_path = os.path.join(folder, filename)
    try:
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        print(f"Playing: {filename}")
        print("Commands: 'p' to pause, 'r' to resume, 's' to stop")
        while True:
            command = input("Enter command: ").strip().lower()
            if command == 'p':
                pygame.mixer.music.pause()
                print("Music paused.")
            elif command == 'r':
                pygame.mixer.music.unpause()
                print("Music resumed.")
            elif command == 's':
                pygame.mixer.music.stop()
                print("Music stopped.")
                break
            else:
                print("Invalid command. Please enter 'p', 'r', or 's'.")
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    except pygame.error as e:
        print(f"Could not play the file {filename}. Error: {e}")
def main():
    try:
        pygame.mixer.init()
    except pygame.error as e:
        print("Audio initialization failed! ", e)

    folder ="music"

    if not os.path.isdir(folder):
        print(f"The folder '{folder}' does not exist.")
        return
    
    mp3_files = [file for file in os.listdir(folder) if file.endswith(('.mp3', '.wav', '.ogg'))]
    if not mp3_files:
        print(f"No audio files found in the folder '{folder}'.")
        return
    while True:
        print("\nAvailable audio files:")
        for idx, file in enumerate(mp3_files, start=1):
            print(f"{idx}. {file}")
        choice_input = input("Enter the number of the audio file to play (or 'q' to quit): ")
        
        if choice_input.lower() == 'q':
            print("Exiting the program.")
            break
        if not choice_input.isdigit():
            print("Invalid choice. Please try again.")
            continue 
        choice = int(choice_input) -1
        if choice >= 0 or choice < len(mp3_files):
            play_music(folder, mp3_files[choice])
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()  