import cv2


def dodgeNaive(image, mask):
    width, height = image.shape[:2]
    blend = np.zeros((width, height), np.uint8)

    for col in range(width):
        for row in range(height):
            if mask[col, row] == 255:
                blend[col, row] = 255
            else:
                tmp = (image[col, row] << 8) / (255 - mask)
                if tmp.any() > 255:
                    tmp = 255
                    blend[col, row] = tmp

    return blend


def dodgeV2(image, mask):
    return cv2.divide(image, 255 - mask, scale=256)


def burnV2(image, mask):
    return 255 - cv2.divide(255 - image, 255 - mask, scale=256)


def rgb_to_sketch(img_rgb):
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

    img_gray_inv = 255 - img_gray
    img_blur = cv2.GaussianBlur(img_gray_inv, ksize=(21, 21),
                                sigmaX=0, sigmaY=0)
    img_blend = dodgeV2(img_gray, img_blur)
    return img_blend


cap = cv2.VideoCapture('raw.mp4')

while(cap.isOpened()):
    ret, frame = cap.read()

    cv2.imshow('frame', rgb_to_sketch(frame))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
