import cv2

def face(frame):
    face_cascade = cv2.CascadeClassifier("haar_cascade/haar_cascade_frontal_face_default.xml")
    img_g = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(img_g,1.2,8)
    myface_list = []
    myface_list_area = []
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
cap = cv2.VideoCapture(0)
while True:
    _,frame = cap.read()
    face(frame)
    if not _:
        break
    cv2.imshow("Face_detection",frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
