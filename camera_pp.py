import cv2

cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

count =0

if vc.isOpened():
    rval , frame = vc.read()
else: rval =False

while rval:
    cv2.imshow("preview", frame)
    rval, frame = vc.read()
    key = cv2.waitKey(20)
    if key == 27:
        break
    elif key== 32:
        img_name = "opencv_frame_{}.png".format(count)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        count += 1

vc.release()
cv2.destroyAllWindows()
