import cv2
import numpy as np
from utils import load_regions, detect_switch_state
import glob

# 1) load the ROI coordinates you calibrated earlier
regions = load_regions("dip_regions.txt")

# 2) get a list of all images in the photos folder
image_files = glob.glob("photos/*.jpg") + glob.glob("photos/*.png")

for img_path in image_files:
    # 3) read the photo
    frame = cv2.imread(img_path)
    if frame is None:
        print("Could not read", img_path)
        continue

    # 4) for each ROI, decide ON/OFF
    bits = []
    for r in regions:
        bits.append(detect_switch_state(frame, r))

    # 5) compute decimal value
    binary_str = "".join(str(b) for b in bits)
    channel = int(binary_str, 2)

    # 6) show result
    print(f"{img_path} → binary={binary_str}  decimal={channel}")
