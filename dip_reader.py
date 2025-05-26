import cv2
from utils import load_regions, detect_switch_state

cap = cv2.VideoCapture(2)
regions = load_regions()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    bits = []
    for region in regions:
        state = detect_switch_state(frame, region)
        bits.append(state)
        x, y, w, h = region
        color = (0, 255, 0) if state else (0, 0, 255)
        cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)

    # Display value
    if len(bits) == 8:
        binary_str = ''.join(map(str, bits))
        decimal_value = int(binary_str, 2)
        cv2.putText(frame, f"Value: {decimal_value}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    cv2.imshow("DIP Reader", frame)
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()