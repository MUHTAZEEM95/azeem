import cv2

print("🎯 Calibration mode: Draw boxes around EACH DIP switch.")
print("➡ Press ENTER/SPACE to confirm. Press 'c' to cancel.")
print("➡ You need to draw exactly 8 ROIs. Output: dip_rois.txt")

img_path = "photos/IMG001.jpg"
frame = cv2.imread(img_path)
if frame is None:
    print(f"❌ Failed to load image at {img_path}")
    exit()

regions = []
count = 0
while count < 8:
    print(f"🟦 Select switch #{count + 1}")
    roi = cv2.selectROI("Draw ROI", frame, showCrosshair=True)
    if roi == (0, 0, 0, 0):
        print("❌ Invalid/empty selection. Try again.")
        continue
    regions.append(roi)
    count += 1

cv2.destroyAllWindows()

with open("dip_rois.txt", "w") as f:
    for i, (x, y, w, h) in enumerate(regions, start=1):
        f.write(f"{i},{x},{y},{w},{h}\n")

print("✅ Saved 8 switch positions to dip_rois.txt")

