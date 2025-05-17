# app.py
import random

def load_images():
    """
    Simulate loading images from manufacturing line
    Returns a list of image IDs (just dummy data here)
    """
    images = [f"image_{i}" for i in range(1, 11)]  # 10 dummy images
    print(f"Loaded images: {images}")
    return images

def detect_defect(image_id):
    """
    Dummy AI defect detection
    Randomly decides if an image has defect or not.
    In real case, this would use an ML model.
    """
    # Simulate defect detection with random chance
    defect_prob = random.random()
    if defect_prob > 0.7:  # 30% chance of defect
        return True
    return False

def quality_control(images):
    """
    Run defect detection on a list of images
    Returns a report dictionary with image IDs and detection results
    """
    report = {}
    for img in images:
        has_defect = detect_defect(img)
        report[img] = "Defect" if has_defect else "OK"
    return report

def print_report(report):
    """
    Print the defect detection report
    """
    print("\nQuality Control Report:")
    for img, status in report.items():
        print(f"{img}: {status}")

def main():
    images = load_images()
    report = quality_control(images)
    print_report(report)

if __name__ == "__main__":
    main()
