import cv2

car_cascade=cv2.CascadeClassifier("C://Users//Arya//AppData//Local//Programs//Python//Python310//pedestrian_haarcascade.xml")
body_cascade=cv2.CascadeClassifier("fullbody.xml")

def detect_cars_and_ped(frame):
    cars=car_cascade.detectMultiScale(frame,1.15,4)
    ped=body_cascade.detectMultiScale(frame,1.15,4)
    for (x,y,w,h) in cars:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(90,70,30),2)
        cv2.rectangle(frame,(x+1,y+1),(x+w,y+h),(190,170,30),2)
    for (x,y,w,h) in ped:
         cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,30),2)
    print(len(cars), "cars detected")
    print(len(ped), "ped detected")
    return frame
         
def simulator():
    carvideo=cv2.VideoCapture("C:\\Users\\Arya\\Downloads\\cars.mp4")
    while carvideo.isOpened():
        ret,frame=carvideo.read()
        key=cv2.waitKey(1)
        if ret:
            cars_frame=detect_cars_and_ped(frame)
            cv2.imshow("detected cars and people",cars_frame)
        else:
            break
        if key==ord('q'):
            break
    carvideo.release()
    cv2.destroyAllWindows()


simulator()