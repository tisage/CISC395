"""
Lab 07: Trip Notes — Project Setup
===================================
Run this script ONCE from your CISC395 workspace folder to create the
trip_notes/ project and download all required files.

Usage:
    python setup.py
"""

import os
import urllib.request

BASE_URL = "https://raw.githubusercontent.com/tisage/CISC395/refs/heads/main/Lab07/"

# Files to download: (remote path, local path inside trip_notes/)
DOWNLOADS = [
    ("tests/test_flow.py",          "tests/test_flow.py"),
    ("prompts/ex2_models.md",       "prompts/ex2_models.md"),
    ("prompts/ex3_storage.md",      "prompts/ex3_storage.md"),
    ("prompts/ex4_main.md",         "prompts/ex4_main.md"),
    ("prompts/part2_template_a.md", "prompts/part2_template_a.md"),
    ("prompts/part2_template_b.md", "prompts/part2_template_b.md"),
    ("prompts/part2_template_c.md", "prompts/part2_template_c.md"),
]

# Empty source files to create
EMPTY_SRC = [
    "src/main.py",
    "src/models.py",
    "src/storage.py",
]


def setup():
    root = "trip_notes"

    # Check: don't overwrite an existing project
    if os.path.exists(root):
        print(f"'{root}/' already exists. Delete it first if you want a fresh setup.")
        return

    print("Creating trip_notes/ project structure...")

    # Create directories
    for d in ["src", "data", "tests", "prompts"]:
        os.makedirs(os.path.join(root, d), exist_ok=True)

    # Create empty source files
    for f in EMPTY_SRC:
        open(os.path.join(root, f), "w").close()

    # Create requirements.txt and README.md
    open(os.path.join(root, "requirements.txt"), "w").close()
    with open(os.path.join(root, "README.md"), "w") as f:
        f.write("# Trip Notes\n")

    print("Downloading lab files...")

    # Download tests and prompts
    for remote, local in DOWNLOADS:
        dest = os.path.join(root, local)
        url = BASE_URL + remote
        try:
            urllib.request.urlretrieve(url, dest)
            print(f"  ✓  {local}")
        except Exception as e:
            print(f"  ✗  {local}  ({e})")
            print(f"     Retry manually: curl -o {dest} {url}")

    print()
    print("Setup complete! Your project is ready at: trip_notes/")
    print()
    print("Next steps:")
    print("  1. cd trip_notes")
    print("  2. Open VS Code with two terminals (see Lab 07 instructions)")
    print("  3. Terminal 1: start your AI agent")
    print("  4. Terminal 2: run tests and git commands")
    print("  5. Start Exercise 2: give your AI  @prompts/ex2_models.md")


if __name__ == "__main__":
    setup()
