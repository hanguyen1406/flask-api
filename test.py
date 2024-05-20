import cv2
from PIL import Image, ImageDraw, ImageFont
import numpy as np

def testData(matTruoc, matSau, data):
    print(matTruoc)
    print(matTruoc)
    print(data)

def createCCcd(matTruoc, matSau, data):
    image = cv2.imread(matTruoc)

    if image is None:
        print("Error: Could not load image")
        exit()

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    pil_image = Image.fromarray(image)

    draw = ImageDraw.Draw(pil_image)

    text = data[0]
    font_path = "./SVN-Arial Bold.ttf"  
    font_size = 39
    font = ImageFont.truetype(font_path, font_size)
    position = (564,313)
    color = (0, 0, 0)  
    draw.text(position, text, font=font, fill=color)

    font_path = "./SVN-Arial Regular.ttf"  

    text = data[1]
    font_size = 30
    font = ImageFont.truetype(font_path, font_size)
    position = (478,386)
    color = (0, 0, 0)  
    draw.text(position, text, font=font, fill=color)

    text = data[2]
    font_size = 25
    font = ImageFont.truetype(font_path, font_size)
    position = (705,419)
    color = (0, 0, 0)  
    draw.text(position, text, font=font, fill=color)

    text = data[3]
    font_size = 25
    font = ImageFont.truetype(font_path, font_size)
    position = (621,451)
    color = (0, 0, 0)  
    draw.text(position, text, font=font, fill=color)

    text = "Việt Nam"
    font_size = 25
    font = ImageFont.truetype(font_path, font_size)
    position = (897,449)
    color = (0, 0, 0)  
    draw.text(position, text, font=font, fill=color)


    text = data[5]
    font_size = 25
    font = ImageFont.truetype(font_path, font_size)
    position = (478, 512)
    color = (0, 0, 0)  
    draw.text(position, text, font=font, fill=color)


    text = data[6]
    font_size = 25
    font = ImageFont.truetype(font_path, font_size)
    position = (478, 570)
    color = (0, 0, 0)  
    draw.text(position, text, font=font, fill=color)


    text = data[4]
    font_size = 20
    font = ImageFont.truetype(font_path, font_size)
    position = (365, 563)
    color = (0, 0, 0)  
    draw.text(position, text, font=font, fill=color)
    print(data)

    cv_image_with_text = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)

    cv2.imwrite('output_mat_truoc.jpg', cv_image_with_text)
    # print("Tạo mặt trước thành công")
    # mat sau
    image = cv2.imread(matSau)

    if image is None:
        print("Error: Could not load image")
        exit()

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    pil_image = Image.fromarray(image)

    draw = ImageDraw.Draw(pil_image)

    text = f"""{data[7]}"""
    font_path = "./OCRB Regular.ttf"  
    font_size = 40
    font = ImageFont.truetype(font_path, font_size)
    position = (270,460)
    color = (0, 0, 0)  
    draw.text(position, text, font=font, fill=color)


    cv_image_with_text = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)
    cv2.imwrite('output_mat_sau.jpg', cv_image_with_text)

    # cv2.destroyAllWindows()
