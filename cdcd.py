import hashlib
import os

def calculate_md5(file_path):
    """Calculates the MD5 hash of the specified file."""
    hasher = hashlib.md5()
    with open(file_path, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()

def create_file_with_same_md5(target_md5, output_file):
    """Creates a file with the same MD5 hash as the target hash."""
    # Generate a file with random content
    with open(output_file, 'wb') as f:
        f.write(os.urandom(1024))  # Write 1 KB of random data

    # Modify the file until the MD5 hash matches
    while calculate_md5(output_file) != target_md5:

        with open(output_file, 'ab') as f:
            f.write(os.urandom(1))  # Append random data byte by byte

if __name__ == "__main__":
    target_md5 = "6a046a57ca3dd222d8bf1410b8172f81"
    output_file_path = "output_file.exe"
    create_file_with_same_md5(target_md5, output_file_path)
    print(f"Created file with same MD5: {output_file_path}")
