import os
import subprocess
import sys
import shutil

def check_ffmpeg():
    if shutil.which("ffmpeg") is None:
        print("ffmpeg not found. Trying to install 'ffmpeg' via pip...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "ffmpeg"])
            print("Installed ffmpeg-python!")
        except subprocess.CalledProcessError:
            print("Installation failed. Please install ffmpeg manually using your system's package manager.")
            sys.exit(1)
    else:
        print("ffmpeg is installed.")

def convert_to_png(directory):
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            name, ext = os.path.splitext(filename)
            ext = ext.lower()
            if ext in [".mp4", ".mov", ".avi", ".mkv", ".jpg", ".jpeg", ".bmp", ".gif", ".tiff"]:
                output_pattern = os.path.join(directory,"Converted PNGs", f"{name}.png")
                try:
                    print(f"Converting {filename}...")
                    subprocess.run(
                        ["ffmpeg", "-i", filepath, output_pattern],
                        check=True,
                        stdout=subprocess.DEVNULL,
                        stderr=subprocess.DEVNULL
                    )
                    print(f"{filename} converted successfully.")
                except subprocess.CalledProcessError as e:
                    print(f"Error converting {filename}: {e}")

if __name__ == "__main__":
    target_directory = input("What directory should be converted? ")
    check_ffmpeg()
    convert_to_png(target_directory)
