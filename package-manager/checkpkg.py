#!/usr/bin/env python3

import os
import sys
import subprocess


def is_root():
    return os.getuid() == 0


def is_installed(pkg: str) -> bool:
    result = subprocess.run(
        ["pacman", "-Qi", pkg], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
    )
    return result.returncode == 0


if len(sys.argv) < 2:
    print("please enter atleast 1 package")
    sys.exit(1)

if sys.argv[1] == "--help":
    print(f"sudo {sys.argv[0]} then type packages name")
    print(f"example: sudo {sys.argv[0]} git vim etc..")
    sys.exit(0)


packages = sys.argv[1:]

installed = []
not_installed = [pkg for pkg in packages if not is_installed(pkg)]


if not not_installed:
    print("All packages are installed")
    sys.exit(0)

print("Not installed")
print(" " + " ".join(not_installed))

while True:
    try:
        choice = (
            input("Do you want to install not installed packages y/n: ").strip().lower()
        )

        if choice in ["y", "yes"]:
            cmd = ["pacman", "-S"] + not_installed
            if not is_root():
                print("sudo required. Asking for permission...")
                cmd = ["sudo"] + cmd
            try:
                res = subprocess.run(cmd)
                if res.returncode == 0:
                    print("Sucsesfully installed" + " " + " ".join(not_installed))
            except KeyboardInterrupt:
                print("\n installaion cancelled by user")
            break
        elif choice in ["n", "no"]:
            print("Installation canceld")
            break
        else:
            print("please type y or n")
    except KeyboardInterrupt:
        print("\n cancelled by user")
        break
