def calculate_hash(filepath):
    sha256 = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(4096):
            sha256.update(chunk)
    return sha256.hexdigest()

def create_baseline():
    baseline = {}
    for root, dirs, files in os.walk(MONITOR_DIR):
        for file in files:
            path = os.path.join(root, file)
            baseline[path] = calculate_hash(path)

    with open(BASELINE_FILE, "w") as f:
        json.dump(baseline, f, indent=4)

    print("Baseline created.")

def monitor_files():
    with open(BASELINE_FILE, "r") as f:
        baseline = json.load(f)

    while True:
        for path in baseline:
            if os.path.exists(path):
                current_hash = calculate_hash(path)
                if baseline[path] != current_hash:
                    print(f"[ALERT] File changed: {path}")
            else:
                print(f"[ALERT] File deleted: {path}")

        time.sleep(10)

if __name__ == "__main__":
    if not os.path.exists(BASELINE_FILE):
        create_baseline()
    else:
        monitor_files()
