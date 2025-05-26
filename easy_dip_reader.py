import cv2
import glob

# Helper to decide ON/OFF in a region
def detect_switch_state(frame, region):
    x,y,w,h = region
    roi = frame[y:y+h, x:x+w]
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    # threshold for ON/OFF (tweak 100 if needed)
    return 1 if gray.mean() < 100 else 0

# --------- EDIT THESE ROIS TO MATCH YOUR PHOTO LAYOUT ---------
# Example for an 800×400‑pixel photo with 8 equal boxes.
# You must adjust these numbers once based on your real photo size!
dip_rois = [
    (0, 50, 100, 100), (100, 50, 100, 100),
    (200, 50, 100, 100), (300, 50, 100, 100),
    (0,200,100,100), (100,200,100,100),
    (200,200,100,100), (300,200,100,100)
]
# --------------------------------------------------------------

# Process every JPG/PNG in the photos folder
for path in glob.glob("photos/*.jpg") + glob.glob("photos/*.png"):
    frame = cv2.imread(path)
    if frame is None:
        print("Cannot read", path)
        continue

    bits = [detect_switch_state(frame, r) for r in dip_rois]
    binary = "".join(str(b) for b in bits)
    channel = int(binary, 2) if binary else None

    print(f"{path} → binary={binary}  decimal={channel}")
