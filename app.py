import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
import time 
import random

cap=cv2.VideoCapture(0)


cap.set(cv2.CAP_PROP_FRAME_WIDTH,640)  #width
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480)  #height

detector=HandDetector(maxHands=1)

timer=0
# Ean teliosi i xronometrisi tote to stateResult ginetai True
stateResult= False
start= False
scores= [0,0] #[Player, AI]

message=''
playerMove=''   # H epilogi tou paikti
choice=''       # H epilogi tou ipologisti


while True:
    bgImage= cv2.imread("Resources/bg.png")

    success, img= cap.read()

    imgScaled = cv2.resize(img, None, fx=0.308, fy=0.444)


    # Detect Hand
    # hands, img = detector.findHands(img, draw=True, flipType=True)
    hands, img = detector.findHands(imgScaled)

    cv2.putText(bgImage, 'Press', (265,243), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 1)
    cv2.putText(bgImage, 'S to play', (255,263), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 1)
    cv2.putText(bgImage, 'Rock-Paper-Scissors', (205,65), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 1)


    cv2.putText(bgImage, 'Press', (265,295), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 1)
    cv2.putText(bgImage, 'Q to close', (245,315), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 1)



    if start:


        if stateResult is False:

            timer= time.time()- initialTime
            cv2.putText(bgImage, str(int(timer)), (275,210), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 4)

            if timer>3:
                stateResult=True
                timer=0


                # Dialegei o ipologistis
                choices=['paper','rock','scissors']
                choice= choices[random.randint(0, 2)]
                print('Computer choice', choice)



                if hands:
                    # fingers einai enas pinakas me 5 stoixia. to proto afora ton antixira. to deutero ton dikti ... to teleutaio to mikro daktilo. H antistoixi timi einai
                    # 1 an fainetai to daktilo

                    hand=hands[0]
                    fingers= detector.fingersUp(hand)


                    print('fingers ',fingers)

                    if fingers == [0,0,0,0,0] or fingers==[1,0,0,0,0]:    # sixna stin mpounia anagnorizei ton antixira gia auto elegxoyme kai to [1,0,0,0,0]
                        playerMove="rock"
                    elif fingers== [1,1,1,1,1]:
                        playerMove='paper'
                    elif fingers== [0,1,1,0,0]:
                        playerMove='scissors'
                    else:
                        playerMove='Move not recognised'
                        message='Move not recognised'
                        # print('1 ', message)

                    if(playerMove=='rock' and choice=='scissors' ):
                        scores[0] +=1
                        message='You win'
                    
                    elif(playerMove=='rock' and choice=='paper' ):
                        scores[1] +=1
                        message='You lose'

                    elif(playerMove=='rock' and choice=='rock' ):
                        message='Draw'
                    


                    elif(playerMove=='paper' and choice=='rock' ):
                        scores[0] +=1
                        message='You win'

                    elif(playerMove=='paper' and choice=='scissors' ):
                        scores[1] +=1
                        message='You lose'

                    elif(playerMove=='paper' and choice=='paper' ):
                        message='Draw'
                        


                    elif(playerMove=='scissors' and choice=='paper' ):
                        scores[0] +=1
                        message='You win'

                    elif(playerMove=='scissors' and choice=='rock' ):
                        scores[1] +=1
                        message='You lose'

                    elif(playerMove=='scissors' and choice=='scissors' ):
                        message='Draw'
                    
                    print('playerMove ',playerMove)



                else:
                    # den anagnoristike xeri

                    message='Move not recognised'
                    playerMove= 'Move not recognised'
                    # print('2 ',message)


                # topothetisi ikonas ipologisti
                AIimg= cv2.imread(f"Resources/{choice}.png", cv2.IMREAD_UNCHANGED)

                new_width = 180  
                new_height = 150  
                AIimg_resized = cv2.resize(AIimg, (new_width, new_height), interpolation=cv2.INTER_AREA)
                AIimg_rgb = AIimg_resized[:, :, :3]  # First 3 channels (RGB)

                bgImage[137:287, 360:540]= AIimg_rgb         # height x width

       

    bgImage[107:320, 33:230]= imgScaled         # height x width

    # diatirisi ikonas ipologisti
    if stateResult: 
        bgImage[137:287, 360:540]= AIimg_rgb         # height x width


    if playerMove!='' and timer==0:    

        if(playerMove=="Move not recognised"):

            cv2.putText(bgImage, 'Move not', (255,123), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 1)
            cv2.putText(bgImage, 'recognised', (250,143), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 1)
        
        else:
            cv2.putText(bgImage, playerMove+' vs ', (253,123), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 1)
            cv2.putText(bgImage, choice, (253,143), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 1)
            cv2.putText(bgImage, message, (253,163), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 1)


    cv2.putText(bgImage, ':'+str(scores[0]), (105,100), cv2.FONT_HERSHEY_PLAIN, 2, (255,255,255), 2)
    cv2.putText(bgImage, ':'+str(scores[1]), (377,98), cv2.FONT_HERSHEY_PLAIN, 2, (255,255,255), 2)


    cv2.imshow("Rock Paper Scissors",bgImage)
    key= cv2.waitKey(1)

    if key == ord('s'):
        start= True
        initialTime=time.time()

        stateResult= False

    if key == ord('q'):
        break