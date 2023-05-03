import cv2
import mediapipe as mp
import threading
from playsound import playsound
from time import sleep

def hello():
    playsound("hello.mp3")

def Baba():
    playsound("Babaau.mp3")
    sleep(2)

def Extended():
    playsound("Extendedau.mp3")
    sleep(2)

def Jay():
    playsound("Jay Hindusthanau.mp3")
    sleep(2)

def No():
    playsound("Noau.mp3")
    sleep(2)

def Rock():
    playsound("Rockau.mp3")
    sleep(2)

def super():
    playsound("Superau.mp3")
    sleep(2)

cap = cv2.VideoCapture(0) # Replace with your own video and webcam

mpHands = mp.solutions.hands
hands = mpHands.Hands() 
mpDraw = mp.solutions.drawing_utils
def coordinate(id, h, w):
    cx, cy = lm.x*w, lm.y*h
    return int(cx), int(cy)
Delay=0

Take_photo=0

while True:
    success, img = cap.read()
    
    if not success: 
        break
    
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    h, w, c = img.shape
    handsup=0
    thumbs_correct=0
    fingers_correct=0
    ok=0
    no=0
    extended=0
    rock=0
    
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                if id == 0: 
                    __, cy_0 = coordinate(0, h, w)
                if id == 10: 
                    __, cy_10 = coordinate(10, h, w)
                if id == 1: 
                    __, cy_1 = coordinate(1, h, w)
            
                if id == 2:
                    __, cy_2 = coordinate(2, h, w)
                if id == 3:
                    __, cy_3 = coordinate(3, h, w)
                if id == 4:
                    __, cy_4 = coordinate(4, h, w)

            
                if id == 5: 
                    cx_5, cy_5 = coordinate(5, h, w)
                if id == 9: 
                    __, cy_9 = coordinate(9, h, w)
                if id == 10:
                    cx_10 , cy_10 = coordinate(10,h,w)
                if id == 11:
                    cx_11 , cy_11 = coordinate(11,h,w)
                if id == 13: 
                    __, cy_13 = coordinate(13, h, w)
                if id == 17: 
                    cx_17, cy_17 = coordinate(17, h, w)
                    
                if id == 8: 
                    __, cy_8 = coordinate(8, h, w)  
                if id == 12: 
                    __, cy_12 = coordinate(12, h, w)
                if id == 16: 
                    __, cy_16 = coordinate(16, h, w)
                if id == 20: 
                    __, cy_20 = coordinate(20, h, w)
                mpDraw.draw_landmarks(img,handLms,mpHands.HAND_CONNECTIONS)
            print(cx_5,cx_17)
            if cy_10 < cy_0:
                handsup=1
            else:
                handsup=0
                    
            if (cy_2 > cy_10 and cy_2 < cy_0) and (cy_3 > cy_10 and cy_3 < cy_0):
                thumbs_correct=1
            else:
                thumbs_correct=0
            
            if (cy_5 > cy_8) and (cy_9 > cy_12) and (cy_13 > cy_16) and (cy_17 > cy_20):
                fingers_correct=1
            else:
                figners_correct=0
            
            
            if (cy_4>cy_0):
                no=1
            else:
                no=0
            if (cy_1>cy_4) and (cy_5>cy_8):
                extended=1
            else:
                extended=0
            if (cy_0>cy_8) and (cy_0>cy_20):
                rock=1
            else:
                rock=0
            if (cy_0>cy_12) and (cy_0>cy_16) and (cy_0>cy_20):
                super=1
            else:
                super=0
        
            
            
            if handsup==1 and thumbs_correct==1 and fingers_correct==1 and (cx_5 > cx_17) and (cy_10 > cy_8 and cy_11 > cy_12 and cy_11 > cy_16):
                cv2.putText(img, 'Hello', (int(w/2),int(h/2)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 3)
                m1 = threading.Thread(target=hello)
                m1.start()
            elif handsup==1 and no==1 :
                cv2.putText(img, 'no', (int(w/2),int(h/2)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 3)
                m2 = threading.Thread(target=No)
                m2.start()
            elif handsup==1 and extended==1:
                cv2.putText(img, 'extended', (int(w/2),int(h/2)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 3)
                m3 = threading.Thread(target=Extended)
                m3.start()
            elif handsup==1 and rock==1:
                cv2.putText(img, 'rock', (int(w/2),int(h/2)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 3)
                m4 = threading.Thread(target=Rock)
                m4.start()
            elif handsup==1 and super==1:
                cv2.putText(img, 'super', (int(w/2),int(h/2)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 3)
                m5 = threading.Thread(target=super)
                m5.start()
                
                
            
                
                    
            

            
                

    
    cv2.imshow("Image", img)
    
    if cv2.waitKey(10) & 0xFF==ord('q'):
        break  
        
cap.release()
cv2.destroyAllWindows()