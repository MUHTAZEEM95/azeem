import cv2
from utils import load_rois, is_on

bit_weights = {
    1: 1, 2: 2, 3: 4, 4: 8,
    5: 16, 6: 32, 7: 64, 8: 128
}

img_paths = [
    "photos/switch_1.jpg",
    "photos/switch_2.jpg",
    "photos/switch_3.jpg",
    "photos/switch_4.jpg",
    "photos/switch_5.jpg",
    "photos/switch_6.jpg",
    "photos/switch_7.jpg",
    "photos/switch_8.jpg"
]

rois = load_rois()

for i, path in enumerate(img_paths, start=1):
    print(f"\n🧪 Testing switch #{i} → {path}")
    frame = cv2.imread(path)
    if frame is None:
        print("❌ Image not found.")
        continue

    channel = 0
    for sw in range(1, 9):
        x, y, w, h = rois[sw]
        roi = frame[y:y+h, x:x+w]
        state = is_on(roi)
        channel += state * bit_weights[sw]

    print(f"📡 Channel value (binary): {channel:08b} → decimal: {channel}")
