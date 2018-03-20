import numpy as np
import cv2


cap = cv2.VideoCapture(0)
x=0
y=0
h=0
w=0

refPt = []
def function(name) :




    def click_and_crop(event, x, y, flags, param):
        # grab references to the global variables
        global refPt
        if event == cv2.EVENT_LBUTTONDOWN:
            refPt = [(x, y)]

        # check to see if the left mouse button was released
        elif event == cv2.EVENT_LBUTTONUP:
            refPt.append((x, y))


    # Face and Eyes detection through Haar Cascade XML files loading


    # Loop for each frame of webcame
    x_user=0
    y_user=0
    z_user=0


    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()
        print("in loop")
        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.namedWindow('image', cv2.WINDOW_NORMAL)
        cv2.setMouseCallback("image", click_and_crop)
        l_img = frame
        if len(refPt)>1 :
            x1=refPt[0][0]
            y1=refPt[0][1]
            x2=refPt[1][0]
            y2=refPt[1][1]
            #print(x1,x2,y1,y2)
            flag = 1
            s_img = cv2.imread(name)

            x_onset = 3.2 * 150 / s_img.shape[0] + z_user
            y_onset = 2.5 * 150 / s_img.shape[1]+ z_user
            # x_offset = int(x - x_onset*200)+x_user
            # y_offset = int(y + h + 15)+y_user
            x_offset = x1- int(s_img.shape[0]/2)
            y_offset = y1
            if x_offset <= 0:
                xcut = abs(x_offset)
                x_offset = 0
            else:
                xcut = 0
            s_img = cv2.resize(s_img, (0, 0), fx=x_onset, fy=y_onset)
            crop = s_img[0:l_img.shape[0] - y_offset, xcut:l_img.shape[1] - x_offset]
            # l_img[y_offset:y_offset+crop.shape[0], x_offset:x_offset+crop.shape[1]] = crop
            for c in range(0, 3):
                l_img[y_offset:y_offset + crop.shape[0], x_offset:x_offset + crop.shape[1], c] = crop[:, :, c] * (
                crop[:, :, 2] / 255.0) + l_img[y_offset:y_offset + crop.shape[0], x_offset:x_offset + crop.shape[1], c] * (
                1.0 - crop[:, :, 2] / 255.0)
            # cv2.putText(l_img,"a - Move left",(10,10),FONT_HERSHEY_SIMPLEX,2,(255,255,255),2,cv2.LINE_AA)
        cv2.imshow('image', l_img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()