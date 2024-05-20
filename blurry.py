import cv2

image = cv2.imread('./output_image.jpg')

if image is None:
    print("Error: Could not load image")
    exit()

start_point = (564, 329)   # left-top corner
end_point = (827, 361)  # right-bottom corner

roi = image[start_point[1]:end_point[1], start_point[0]:end_point[0]]
# cv2.imshow('Cut', roi)

blurred_roi = cv2.blur(roi, (3, 3))

image[start_point[1]:end_point[1], start_point[0]:end_point[0]] = blurred_roi

cv2.imwrite('blurred_area_image.jpg', image)

# cv2.imshow('Blurred Area Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
