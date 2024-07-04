import pytesseract as ptess
import cv2
import easyocr
import PIL
import os

path_to_tesseract = "A:\\Data_Science\\Projects\\Whiteout_Survival\\WoS Bot\\Tesseract\\tesseract.exe"
#March_img = "A:\\Data_Science\\Projects\\Whiteout_Survival\\WoS Bot\\images\\images_Testing\\March_time_Example.JPG"

test_image_directory = "A:\\Data_Science\\Projects\\Whiteout_Survival\\WoS Bot\\images\\images_Testing"
test_images = [test_image_directory + "\\" + i for i in os.listdir(test_image_directory)]

ptess.pytesseract.tesseract_cmd = path_to_tesseract

def general_image_text_Reader(path):
    img = PIL.Image.open(path).convert('L')

    text = ptess.image_to_string(img)

    return(text)

def general_image_text_reader_2(path):
    reader = easyocr.Reader(['en'])
    
    return(reader.readtext(path))

def general_image_text_reader_3(path):
    img = cv2.imread(path)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | 
                                 cv2.THRESH_BINARY_INV)

    rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))

    dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)

    contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,
                                           cv2.CHAIN_APPROX_NONE)

    im2 = img.copy()

    text_list = []

    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)

        rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cropped = im2[y:y + h, x:x + w]

        text = ptess.image_to_string(cropped)

        print(text)

        #list.append(text)
    
    #return(text_list)

general_image_text_reader_3(test_images[3])

    




def Get_March_Time(text):
    """March time is returned as © followed by time"""





