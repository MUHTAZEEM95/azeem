import cv2
import glob

# Load utils if you have detect_switch_state; or inline it:
def detect_switch_state(frame, region, thresh=100):
    x,y,w,h = region
    roi = frame[y:y+h, x:x+w]
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    return 1 if gray.mean() < thresh else 0

# 1) Define ROIs in the order of switches [1,2,3,4,8,7,6,5]
#    but we will only use bits for switches 1–7.
#    These numbers are from your 1571×1042 measurement example:
dip_rois = {
    1: (0,    0,   392, 521),
    2: (392,  0,   392, 521),
    3: (784,  0,   392, 521),
    4: (1176, 0,   395, 521),
    8: (0,    521, 392, 521),
    7: (392,  521, 392, 521),
    6: (784,  521, 392, 521),
    5: (1176, 521, 395, 521),
}

# 2) Define the bit weights for switches 1–7
bit_weights = {
    1: 64,  # switch 1 → bit6
    2: 32,  # switch 2 → bit5
    3: 16,  # switch 3 → bit4
    4: 8,   # switch 4 → bit3
    5: 1,   # switch 5 → bit0
    6: 2,   # switch 6 → bit1
    7: 4,   # switch 7 → bit2
    # switch 8 is ignored or weight 0
}

# 3) Process each photo
for path in glob.glob("photos/*.jpg") + glob.glob("photos/*.png"):
    frame = cv2.imread(path)
    if frame is None:
        print("Cannot read", path)
        continue

    # 4) Read each switch 1–7
    channel_value = 0
    bits = {}
    for sw in range(1,8):            # only 1 through 7
        region = dip_rois[sw]
        state = detect_switch_state(frame, region)
        bits[sw] = state
        channel_value += state * bit_weights[sw]

    # 5) Shift from 0–127 to 1–128
    channel = channel_value + 1

    # 6) Show result
    print(f"{path} → switches {bits} → channel {channel}")
