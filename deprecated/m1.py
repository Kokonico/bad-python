import ascii_magic
import simpleaudio as sa
import cv2
import time

# options = ConverterOptions(gradient=gradients.BLOCK, saturation=0.25, width=48, height=36)
# converter = GrayscaleConverter(options)
frame_count = 0
audio = 'bad_apple.wav'

# Open the video file
cap = cv2.VideoCapture('badapple.mp4')
sa.WaveObject.from_wave_file(audio).play()
while(cap.isOpened()):
    # Read the next frame
    ret, frame = cap.read()

    if ret is True:

        imgfile = f'imgs/frame{frame_count}.jpg'
        # Convert the frame to ASCII art
        cv2.imwrite(imgfile, frame)

        # ascii_art = Image(imgfile, converter)
        ascii_art = ascii_magic.from_image(imgfile)
        
        frame_count += 1

        # Display the ASCII art
        # ascii_art.view()
        print("\033[H\033[J")
        ascii_art.to_terminal(columns=48, monochrome=True)

        # Delay for a while before processing the next frame
        time.sleep(0.0193)
    else:
       break

# Release the video file
cap.release()
