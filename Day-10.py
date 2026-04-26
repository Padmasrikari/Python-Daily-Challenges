import random
import copy
import math
import numpy as np
import pandas as pd
roll_number = 24110011615 % 100
def generate_data():
    data = []
    n = random.randint(10, 15)
    for i in range(n):
        data.append({
            "id": i + 1,
            "marks": random.randint(40, 100),
            "attendance": random.randint(60, 100),
            "scores": [random.randint(10, 25), random.randint(10, 25)]
        })
    return data
def mutate_data(data):
    mod = roll_number % 3
    if mod == 0:
        mod = 1
    for i in range(len(data)):
        if i % mod == 0:
            data[i]["marks"] = data[i]["marks"] + math.sqrt(data[i]["marks"])
            data[i]["attendance"] -= 5
            data[i]["scores"][0] += 2
            data[i]["scores"][1] += 3
    return data
def manual_mean(data):
    total = 0
    for d in data:
        total += d["marks"]
    return total / len(data)
def analyze_data(original, modified):
    orig_marks = np.array([d["marks"] for d in original])
    mod_marks = np.array([d["marks"] for d in modified])
    mean = np.mean(mod_marks)
    median = np.median(mod_marks)
    std_dev = np.std(mod_marks)
    orig_mean = manual_mean(original)
    drift = abs(orig_mean - mean)
    normalized = (mod_marks - np.min(mod_marks)) / (np.max(mod_marks) - np.min(mod_marks))
    return float(mean), float(median), float(std_dev), float(drift), normalized
def detect_copy_failure(original_backup, current):
    for i in range(len(original_backup)):
        if original_backup[i] != current[i]:
            return True
    return False
def classify(drift, threshold, copy_failed):
    if copy_failed:
        return "Copy Failure Detected"
    elif drift < threshold:
        return "Stable Data"
    elif drift < threshold * 2:
        return "Minor Drift"
    else:
        return "Critical Drift"
data = generate_data()
original_backup = copy.deepcopy(data)
shallow_copy = data.copy()
deep_copy = copy.deepcopy(data)
mutate_data(shallow_copy)
mutate_data(deep_copy)
df_original = pd.DataFrame(data)
df_shallow = pd.DataFrame(shallow_copy)
df_deep = pd.DataFrame(deep_copy)
mean, median, std_dev, drift, normalized = analyze_data(original_backup, deep_copy)
threshold = 5
copy_failed = detect_copy_failure(original_backup, data)
result = classify(drift, threshold, copy_failed)
print("Original DataFrame:")
print(df_original)
print("\nShallow Copy DataFrame:")
print(df_shallow)
print("\nDeep Copy DataFrame:")
print(df_deep)
print("\nDrift Value:", drift)
print("Tuple:", (mean, drift, std_dev))
print("Classification:", result)