import hashlib
import pathlib


if __name__ == "__main__":
    start = 15210407809
    N = 10000
    filename = pathlib.Path.home() / "Downloads" / f"sha256_records_{N}.txt"

    with open(filename, "wt") as f:
        for i in range(N):
            cur = start + i
            hex = hashlib.sha256(str(cur).encode()).hexdigest()
            f.write(f"{hex}\n")
