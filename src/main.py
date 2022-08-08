import cv2
import numpy as np
import glob

def main():
    scale = 4
    image_list = sorted(glob.glob("./images/LR/*.png"))
    
    for image_path in image_list:
        image = cv2.imread(image_path)
        height, width = image.shape[:2]
        image_bicubic = cv2.resize(image, (width*scale, height*scale), interpolation=cv2.INTER_CUBIC)
        
        print("./images/bicubic-SR/" + image_path.split("/")[-1])
        cv2.imwrite("./images/bicubic-SR/" + image_path.split("/")[-1], image_bicubic)
        
    
if __name__ == '__main__':
    main()