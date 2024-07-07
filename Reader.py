

import pytesseract as ptess
import cv2
import PIL
import datetime

#import os

path_to_tesseract = "A:\\Data_Science\\Projects\\Whiteout_Survival\\WoS Bot\\Tesseract\\tesseract.exe"
#March_img = "A:\\Data_Science\\Projects\\Whiteout_Survival\\WoS Bot\\images\\images_Testing\\March_time_Example.JPG"

test_image_directory = "A:\\Data_Science\\Projects\\Whiteout_Survival\\WoS Bot\\images\\images_Testing"
#test_images = [test_image_directory + "\\" + i for i in os.listdir(test_image_directory)]

ptess.pytesseract.tesseract_cmd = path_to_tesseract

#note success with pytesseract. 
#simple image processing using PIL 
#enables reading of training wait time button

#more complex image processing using cv2 yields
#better recognition of march times

#easyocr does not work well for the purpose of this
#program

def text_reader_PIL(path, grey):
    """Use this function to read promotion times"""
    if grey == True:

        img = PIL.Image.open(path).convert('L')

    else:

        img = PIL.Image.open(path)

    text = ptess.image_to_string(img)

    return(text)

def text_reader_cv2(path, arg):
    """Use this function to read march times.
    note to future me: read more about image processing
    with cv2"""

    img = cv2.imread(path)

    if arg == 1:
        """"""

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | 
                                    cv2.THRESH_BINARY_INV)

        rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))

        dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)

        contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,
                                            cv2.CHAIN_APPROX_NONE)

        im2 = img.copy()

        text_list = []

        my_text = ""

        for cnt in contours:
            x, y, w, h = cv2.boundingRect(cnt)

            rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)

            cropped = im2[y:y + h, x:x + w]

            text = ptess.image_to_string(cropped)

            print(text)

            my_text = my_text + text

    elif arg == 2:
        """lighthouse stamina cans"""
        img_h, img_w = img.shape[:2]
        
        img_stretched = cv2.resize(img, (img_w * 10, img_h * 10),
                                   interpolation= cv2.INTER_CUBIC)
        
        img_stretched_B, img_stretched_G, img_stretched_R = cv2.split(img_stretched) 
        
        my_text = ptess.image_to_string(img_stretched_B)

        rem_index = my_text.find(">")

        my_text = my_text[rem_index:].strip()

    return(my_text)





def time_reader(text):
    """returns the timer in seconds
    times are presented with leading 00 at the hour mark
    days are marked with d, if there are any."""
    text_no_ascii = "".join([ele for ele in text if ele.isascii()])

    index_list = []

    #find first appearance of a numeric character. 
    #either catches the day or hour mark
    for num in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        index_list.append(text_no_ascii.find(num))

    index_list = [i for i in index_list if i != -1]

    text_start = min(index_list)

    trimmed_text = text_no_ascii[text_start:]

    #seconds in each time frame

    time_dict = {'d' : 86400, 'h' : 3600, 'm' : 60}

    if trimmed_text.find("d") != -1:

        time_text = trimmed_text.replace("d", "")

        time_text = time_text.replace(" ", ":")

        d, h, m, s = time_text.split(":")

        final_seconds = (int(d) * time_dict["d"] 
                         + int(h) * time_dict["h"] 
                         + int(m) * time_dict["m"] + int(s))

    else:

        time_text = trimmed_text

        h, m, s = time_text.split(":")

        final_seconds = (int(h) * time_dict["h"] 
                         + int(m) * time_dict["m"] + int(s))
        
    return(final_seconds)