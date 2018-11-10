import face_recognition
import cv2

cap = cv2.VideoCapture(0)

while 1:
    r,frame = cap.read()
    cnv = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    face_landmarks_list = face_recognition.face_landmarks(cnv)
    # print(face_landmarks_list)
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Find all the faces and face encodings in the current frame of video
    face_locations = face_recognition.face_locations(small_frame, model="cnn")

    # Display the results
    for top, right, bottom, left in face_locations:
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Extract the region of the image that contains the face
        face_image = frame[top:bottom, left:right]
        cv2.imshow('faces',face_image)

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
cv2.destroyAllWindows()
cap.release()
