import simpleaudio as sa
import time

audio = 'bad_apple.wav'

# create list with all 6000+ frames

frames = []

for i in range(6571):
    ip = i + 1
    with open(f'frames/frame{ip}.txt', 'r') as f:
        frames.append(f.read())

sa.WaveObject.from_wave_file(audio).play()
for i in range(6571):
    print(frames[i])
    time.sleep(0.0293)
    # time.sleep(0.0295)
    print("\033[H\033[J")