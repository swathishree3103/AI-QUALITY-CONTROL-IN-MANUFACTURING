import cv2
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import zipfile
import os
import pandas as pd

# Set paths
zip_path = r"C:\Users\Jayalakshmi murugan\Downloads\archive (5).zip"
extract_path = r"C:\Users\Jayalakshmi murugan\Downloads\archive (5)"

# Extract ZIP
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_path)

# Auto-find CSV file in extracted contents
def find_csv(zip_path):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        for file in zip_ref.namelist():
            if file.endswith('.csv'):
                return file  # Return the first CSV file name
    return None

zip_path = r'C:\Users\Jayalakshmi murugan\Downloads\archive (5).zip'
csv_file = find_csv(zip_path)
print("CSV file found:", csv_file)
# Measurement check
def check_measurement(data, min_val=10, max_val=20):
    return [(x, min_val <= x <= max_val) for x in data]

# Analyze CSV and plot
def analyze_csv(csv_file):
    df = pd.read_csv(r"C:\Users\Jayalakshmi murugan\Downloads\archive (5).zip")
    for col in df.select_dtypes(include=[np.number]).columns:
        print(f"\nColumn: {col}")
        results = check_measurement(df[col])
        for val, ok in results:
            print(f"Value: {val} -> {'PASS' if ok else 'FAIL'}")

        # Plot using matplotlib
        plt.figure(figsize=(10, 4))
        plt.plot(df[col], label=col)
        plt.axhline(10, color='red', linestyle='--', label='Min Threshold')
        plt.axhline(20, color='green', linestyle='--', label='Max Threshold')
        plt.title(f"Measurements in '{col}'")
        plt.xlabel("Index")
        plt.ylabel("Value")
        plt.legend()
        plt.tight_layout()
        plt.show()

# Analyze Image
def analyze_image(image_path):
    img = cv2.imread(image_path, 0)
    if img is None:
        print("Image not found or invalid format.")
        return
    _, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    defect_pixels = np.sum(thresh == 0)
    total_pixels = thresh.size
    defect_ratio = defect_pixels / total_pixels
    print(f"Defect Ratio: {defect_ratio:.2%}")
    print("PASS" if defect_ratio < 0.05 else "FAIL")
    plt.imshow(img, cmap='gray')
    plt.title("Analyzed Image")
    plt.axis('off')
    plt.show()

# Manual Input Check
def manual_input_check():
    vals = list(map(float, input("Enter values separated by space: ").split()))
    results = check_measurement(vals)
    for val, ok in results:
        print(f"Value: {val} -> {'PASS' if ok else 'FAIL'}")
    plt.plot(vals, marker='o')
    plt.axhline(10, color='red', linestyle='--')
    plt.axhline(20, color='green', linestyle='--')
    plt.title("Manual Input Values")
    plt.show()

# Main Menu
def main():
    mode = input("Choose mode (csv/image/manual): ").strip().lower()
    if mode == "csv":
        csv_file = find_csv(r"C:\Users\Jayalakshmi murugan\Downloads\archive (5).zip")
        if csv_file:
            analyze_csv(csv_file)
        print("no csv file found.")
    elif mode == "image":
        image_path = input("enter image path" ).strip()
        analyze_image(image_path)
    elif mode == "manual":
        manual_input_check()
    else:
        print("Invalid mode.")

if __name__ == "__main__":
    main()


