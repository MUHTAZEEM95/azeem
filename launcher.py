import tkinter as tk
import subprocess

scripts = [
    "check_camera.py",
    "verify_dip.py",
    "dip_calibrator.py",
    "draw_rois.py",
    "easy_reader.py",
    "easy_dip_reader.py",
    "dip_reader.py",
    "dip_regions.py",
    "batch_reader.py",
    "preprocess_image.py",
    "live_feed.py",
    "utils.py"
]

def run_script(script_name):
    subprocess.Popen(["python", script_name])

root = tk.Tk()
root.title("DIP Switch Detection Launcher")
root.geometry("400x600")

for script in scripts:
    btn = tk.Button(root, text=script, command=lambda s=script: run_script(s))
    btn.pack(pady=5, fill='x', padx=10)

root.mainloop()

