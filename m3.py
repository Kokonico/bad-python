import simpleaudio as sa
import time
import curses
import os
from pathlib import Path

AUDIO = 'bad_apple.wav' # get audio controller
DIRECTORY = 'frames' # get frames directory
FPS = 30 # set frames per second

# Use os.scandir() to count files
fcount = len([f for f in os.scandir(DIRECTORY) if f.is_file()])

# Use list comprehension to create frames list
frames = [open(Path(DIRECTORY) / f'frame{i+1}.txt').read() for i in range(fcount)]

badapple = sa.WaveObject.from_wave_file(AUDIO)

# Initialize curses
try:
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
except curses.error:
    print(EnvironmentError("Error initializing curses, are you using a terminal? (the VSCode output menu doesn't work)"))
    exit(1)

last_frame = -1

audio = badapple.play()
start = time.perf_counter()

try:
    while audio.is_playing():
        elapsed = time.perf_counter() - start
        current_frame = int(elapsed * FPS)
        
        if current_frame != last_frame:
            stdscr.clear()
            
            if current_frame < len(frames):
                height, width = stdscr.getmaxyx()
                
                resized_frame = '\n'.join(line[:width] for line in frames[current_frame].split('\n')[:height])
                
                try:
                    stdscr.addstr(0, 0, resized_frame)
                except curses.error:
                    print(EnvironmentError("Error drawing frame, is your terminal too small?"))
                    exit(1)
                stdscr.refresh()
            
        last_frame = current_frame
finally:
    # Cleanup curses
    curses.echo()
    curses.nocbreak()
    curses.endwin()