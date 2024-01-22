import cv2
import numpy as np


# Define upper and lower blue values in hsv
LOWER_BLUE = np.array([60, 35, 140])
UPPER_BLUE = np.array([180, 255, 255])


def main() -> None:
    # Grabs the camera we want to use
    camera: cv2.VideoCapture = cv2.VideoCapture(0)
    
    while True:
        _, frame = camera.read() # We only care about grabbing the second variable of the return tuple
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # Here we init the color change for the mask of the video
        mask = cv2.inRange(hsv, LOWER_BLUE, UPPER_BLUE) # This is where we get the mask
        result = cv2.bitwise_and(frame, frame, mask = mask) # this is the final result of the mask plus color filter
        # Display the 3 video states
        cv2.imshow('frame', frame) # Normal
        cv2.imshow('mask', mask) # Just the mask
        cv2.imshow('result', result) # Mask with color filter
        
        # DO NOT QUIT PROGRAM
        # USE THE Q KEY TO END THE PROGRAM
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break
    
    # Frees the camera for later use
    camera.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
