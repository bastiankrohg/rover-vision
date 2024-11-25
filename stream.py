from cv2 import VideoCapture
import cv2

#rtsp_url = "rtsp://coral-tpu-2.local:8555/cv"
rtsp_url = "rtsp://rover2.local:8554/cam"
#rtsp_url = "rtsp://rover.local:8554/cam"
iphone_url = "http://192.168.1.13:4747/video"


#video=VideoCapture(rtsp_url)
video=VideoCapture(iphone_url)


while(True):
    # Capture frame-by-frame
    ret, frame = video.read()

    # Our operations on the frame come here
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#    rotated=cv2.rotate(gray, cv2.ROTATE_90_COUNTERCLOCKWISE)
    #rotated=cv2.rotate(gray, cv2.ROTATE_90_CLOCKWISE)
    rotated=cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)

    # Display the resulting frame
    cv2.imshow('CuriosiTV',rotated)
    #cv2.imshow('CuriosiTV',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
video.release()
cv2.destroyAllWindows()