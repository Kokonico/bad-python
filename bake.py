"""bake video frames for higher resolution playback"""

import ascii_magic
import cv2

frame_count = 0

VIDEO = 'badapple.mp4'

# Open the video file
cap = cv2.VideoCapture(VIDEO)
while(cap.isOpened()):
    # Read the next frame
    ret, frame = cap.read()

    if ret is True:
        # save frame as JPEG file
        imgfile = f'imgs/frame{frame_count}.jpg'
        cv2.imwrite(imgfile, frame)

        # Convert the frame to ASCII art
        ascii_art = ascii_magic.from_image(imgfile)

        frame_count += 1
        print(frame_count)

        # Display the ASCII art
        ascii_art.to_file(columns=72, monochrome=True, path=f'frames/frame{frame_count}.txt')

    else:
       break

# Release the video file
cap.release()

print("Done!")