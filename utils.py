import cv2
import numpy as np

def load_rois(filename="dip_rois.txt"):
    rois = {}
    with open(filename, "r") as f:
        for line in f:
            parts = line.strip().split(",")
            if len(parts) == 5:
                i, x, y, w, h = map(int, parts)
                rois[i] = (x, y, w, h)
    return rois

def is_on(roi_image, threshold=127):
    gray = cv2.cvtColor(roi_image, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)
    white_pixels = cv2.countNonZero(binary)
    total_pixels = roi_image.shape[0] * roi_image.shape[1]
    white_ratio = white_pixels / total_pixels
    return white_ratio < 0.5
