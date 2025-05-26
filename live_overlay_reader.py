import cv2
from utils import load_rois, is_on

def draw_text(img, txt, pos, color=(0, 255, 0), scale=0.7):
    cv2.putText(img, txt, pos, cv2.FONT_HERSHEY_SIMPLEX, scale, color, 2)

def detect_and_display(frame, rois):
    switch_states = []
    for i, (x, y, w, h) in rois.items():
        roi = frame[y:y+h, x:x+w]
        state = is_on(roi)
        switch_states.append(state)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        draw_text(frame, f"{i}", (x, y - 5))

    binary = ''.join(['1' if s else '0' for s in switch_states])
    draw_text(frame, f"BINARY: {binary}", (10, 50), (255, 255, 0), 1)
    return frame

def main():
    cap = cv2.VideoCapture(1)
    if not cap.isOpened():
        print("❌ Camera not found.")
        return

    rois = load_rois()
    print("📡 Live detection started. Press 'q' to quit, 's' to save snapshot.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        display = detect_and_display(frame.copy(), rois)
        cv2.imshow("Live DIP View", display)

        key = cv2.waitKey(1)
        if key == ord('q'):
            break
        elif key == ord('s'):
            cv2.imwrite("photos/live_snapshots/live_snapshot.jpg", display)
            print("📸 Snapshot saved.")

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
