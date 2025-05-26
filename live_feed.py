import cv2

# Open camera 0 (change to another number if needed)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Camera not accessible.")
    exit()

print("Press 's' to save a frame. Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame.")
        break

    cv2.imshow("Live Camera Feed - DIP Switch", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('s'):
        # Save the current frame
        cv2.imwrite("dip_snapshot.jpg", frame)
        print("Frame saved as dip_snapshot.jpg")
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
