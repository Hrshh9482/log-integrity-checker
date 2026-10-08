import hashlib
import os


def hash_file(path):
    sha = hashlib.sha256()

    with open(path, "rb") as f:
        while True:
            chunk = f.read(4096)

            if not chunk:
                break

            sha.update(chunk)

    return sha.hexdigest()


def collect_files(path):
    if not os.path.exists(path):
        raise SystemExit("Error: path not found: " + path)

    if os.path.isfile(path):
        return [path]

    files = []

    for root, dirs, names in os.walk(path):
        for name in names:
            files.append(os.path.join(root, name))

    return files


for f in collect_files("testlogs"):
    print(f, hash_file(f))