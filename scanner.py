import os
import hashlib


def scan_directory(directory):
    """Scan a directory and process each file."""
    print(f"Scanning directory: {directory}")
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                file_hash = calculate_hash(file_path)
                print(f"File: {file_path} | Hash: {file_hash}")
            except Exception as e:
                print(f"Error processing {file_path}: {e}")


def calculate_hash(file_path):
    """Calculate SHA256 hash of a file."""
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        while chunk := f.read(8192):
            sha256.update(chunk)
    return sha256.hexdigest()


if __name__ == "__main__":
    directory = "./test/" if os.name != "nt" else "C:\\"
    scan_directory(directory)
