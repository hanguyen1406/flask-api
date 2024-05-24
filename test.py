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
    position = (704,392)
    color = (0, 0, 0)  
    draw.text(position, text, font=font, fill=color)

    font_path = "./SVN-Arial Regular.ttf"  

    text = data[1]
    font_size = 30
    font = ImageFont.truetype(font_path, font_size)
    position = (603,478)
    draw.text(position, text, font=font, fill=color)

    text = data[2]
    font_size = 25
    font = ImageFont.truetype(font_path, font_size)
    position = (865,522)
    draw.text(position, text, font=font, fill=color)

    text = data[3]
    font_size = 25
    font = ImageFont.truetype(font_path, font_size)
    position = (771,564)
    draw.text(position, text, font=font, fill=color)

    text = "Việt Nam"
    font_size = 25
    font = ImageFont.truetype(font_path, font_size)
    position = (1120,564)
    draw.text(position, text, font=font, fill=color)


    text = data[5]
    font_size = 25
    font = ImageFont.truetype(font_path, font_size)
    position = (605, 640)
    draw.text(position, text, font=font, fill=color)


    text = data[6]
    font_size = 25
    font = ImageFont.truetype(font_path, font_size)
    # print(text)

    if len(text.split(",")) > 3:
        parts = text.split(',')
        first = parts[0].strip()
        position = (995, 676)
        draw.text(position, first, font=font, fill=color)

        text = ','.join(parts[1:]).strip()



    position = (605, 710)
    draw.text(position, text, font=font, fill=color)

    font_size = 20
    text = data[4]
    font = ImageFont.truetype(font_path, font_size)
    position = (465, 703)
    color = (0, 0, 0)  
    draw.text(position, text, font=font, fill=color)
    # print(data)

    cv_image_with_text = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)

    blurred_image = cv2.GaussianBlur(cv_image_with_text, (3, 3), 0)
    cv2.imwrite('output_mat_truoc.jpg', blurred_image)
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
    position = (275,460)
    color = (0, 0, 0)  
    draw.text(position, text, font=font, fill=color)


    cv_image_with_text = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)
    blurred_image = cv2.GaussianBlur(cv_image_with_text, (3, 3), 0)
    cv2.imwrite('output_mat_sau.jpg', blurred_image)
    # print("Tạo mặt sau thành công")

    # cv2.destroyAllWindows()

createCCcd(
    'mat_truoc.jpg',
    'mat_sau.jpg',
    ['095094015612', 'HOÀNG MINH KIÊN', '30/01/1994', 'Nam', '30/01/2034', 'Phong Thạnh Tây B, Phước Long, Bạc Liêu', 'Ấp 12, Phong Thạnh Tây B, Phước Long, Bạc Liêu', 'IDVNM0940156001095094015600<<3\n9401301M3401309VNM<<<<<<<<<<<6\nHOANG<<MINH<GIAP<<<<<<<<<<<<<<\n']
    )