# AI Quality Control in Manufacturing
# Python 3.9.6 compatible

parts = [
    {"PartID": "P001", "Length": 10.1, "Width": 5.2, "Height": 2.1},
    {"PartID": "P002", "Length": 9.9,  "Width": 5.0, "Height": 2.0},
    {"PartID": "P003", "Length": 10.5, "Width": 4.9, "Height": 1.8},
    {"PartID": "P004", "Length": 10.0, "Width": 5.1, "Height": 2.2},
    {"PartID": "P005", "Length": 9.7,  "Width": 5.3, "Height": 2.3}
]

TOLERANCES = {
    "Length": (9.8, 10.2),
    "Width":  (5.0, 5.2),
    "Height": (2.0, 2.2)
}

def is_within_tolerance(value, limits):
    return limits[0] <= value <= limits[1]

def check_quality(part):
    issues = []
    for dim, (min_val, max_val) in TOLERANCES.items():
        val = part[dim]
        if not is_within_tolerance(val, (min_val, max_val)):
            issues.append(f"{dim}={val}")
    return issues

def run_quality_control():
    print("AI Quality Control Report\n" + "-"*30)
    for part in parts:
        part_id = part["PartID"]
        issues = check_quality(part)
        if issues:
            print(f"[DEFECTIVE] {part_id}: {'; '.join(issues)}")
        else:
            print(f"[PASS] {part_id} passed all checks.")

if __name__ == "__main__":
    run_quality_control()
