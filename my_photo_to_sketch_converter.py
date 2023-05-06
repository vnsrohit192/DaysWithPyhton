
import cv2
def img2sketch(photo, k_size):

    img=cv2.imread(photo)
    
    grey_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    invert_img=cv2.bitwise_not(grey_img)

    blur_img=cv2.GaussianBlur(invert_img, (k_size,k_size),100)


    invblur_img=cv2.bitwise_not(blur_img)

    sketch_img=cv2.divide(grey_img,invblur_img, scale=256.0)

    cv2.imwrite('sketch.png', sketch_img)

    cv2.imshow('sketch image',sketch_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
img2sketch(photo=r'C:\Users\VIRENDRA\Documents\rohit kumar\rohit2.jpg',k_size=7)