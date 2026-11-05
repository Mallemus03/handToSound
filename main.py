import cv2 as cv
import mediapipe as mp
import pygame as pg

cap= cv.VideoCapture(0)

mp_hands = mp.solutions.hands
hands= mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.5)

while True:
    ret,frame= cap.read()
    if not ret:
        break
    frame =cv.flip(frame, 1)

    RGBframe =cv.cvtColor(frame, cv.COLOR_BGR2RGB)

    results= hands.process(RGBframe)
    if results.multi_hand_landmarks is not None:
        print("hand found")#todo: dræb

        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing = mp.solutions.drawing_utils
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    else:
       print( "hand not found") #todo: dræb


    cv.imshow('Our live sketch', frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()