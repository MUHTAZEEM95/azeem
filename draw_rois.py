import cv2
from utils import load_rois

img_path = "photos/IMG001.jpg"
image = cv2.imread(img_path)
if image is None:
    print("❌ Could not load image.")
    exit()

rois = load_rois()
for i, (x, y, w, h) in rois.items():
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.putText(image, str(i), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

cv2.imshow("ROIs", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

