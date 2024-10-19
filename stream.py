import cv2

rtsp_url = "rtsp://rover2.local:8554/cam"
#rtsp_url = "rtsp://rover.local:8554/cam"

video=cv2.VideoCapture(rtsp_url)

while(True):
    # Capture frame-by-frame
    ret, frame = video.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
video.release()
cv2.destroyAllWindows()