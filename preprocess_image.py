import cv2

# 1. Load the saved snapshot
img = cv2.imread("dip_snapshot.jpg")
if img is None:
    print("Error: could not read dip_snapshot.jpg")
    exit()

# 2. Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 3. Apply binary thresholding (invert so switches appear white)
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

# 4. Save and display
cv2.imwrite("dip_preprocessed.jpg", thresh)
cv2.imshow("Preprocessed", thresh)
print("Saved preprocessed image as dip_preprocessed.jpg")
cv2.waitKey(0)
cv2.destroyAllWindows()
