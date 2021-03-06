import cv2
from face_recog import face_recog

# Encode faces from a folder
sfr = face_recog()
sfr.load_encoding_images("images/Kushal","Kushal")
sfr.load_encoding_images("images/Tushar","Tushar")
sfr.load_encoding_images("images/Chris Evans","Chris Evans")
sfr.load_encoding_images("images/Chris Hemsworth","Chris Hemsworth")
sfr.load_encoding_images("images/Mark Ruffalo","Mark Ruffalo")
sfr.load_encoding_images("images/Robert Downey Jr","Robert Downey Jr")
sfr.load_encoding_images("images/Scarlett Johansson","Scarlett Johansson")

# Load Camera
cap = cv2.VideoCapture(0)


while True:
    ret, frame = cap.read()

    # Detect Faces
    face_locations, face_names = sfr.detect_known_faces(frame)
    for face_loc, name in zip(face_locations, face_names):
        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

        cv2.putText(frame, name,(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()