#!/usr/bin/env python3

import os
import shutil
import time
import subprocess


def is_root():
    return os.getuid() == 0


class Storage:
    def __init__(self, path):
        self.path = path
        self.usage = shutil.disk_usage(path)
        self.total = round(self.usage.total / (1024**3), 2)
        self.used = round(self.usage.used / (1024**3), 2)
        self.free = round(self.usage.free / (1024**3), 2)

        self.free_percentage = round(self.free / self.total * 100, 2)

    def check_and_clean(self, clean_cmd, threshold=10):
        print(f"Checking {self.path}...")
        time.sleep(0.5)
        print(f"Free space: {self.free}({self.free_percentage}%)")

        if self.free_percentage >= threshold:
            print("\033[0;32m Sufficient space available. \033[0m")
            return

        print("\033[0;31m Warning: Low disk space! \033[0m ")
        while True:
            try:
                choice = input("Do you want to run cleanup? (y/n): ").strip().lower()
                if choice in ["y", "yes"]:
                    if not is_root():
                        print("\033[0;31m Sudo required for cleanup. \033[0m ")
                        clean_cmd = ["sudo"] + clean_cmd
                    print("Running cleanup...")
                    result = subprocess.run(clean_cmd)
                    if result.returncode == 0:
                        print("\033[0;32m Cleanup successful! \033[0m")
                        break
                    print("\033[0;31m Operation cancelled. \033[0m")
                    break
                elif choice in ["n", "no"]:
                    print("\033[0;31m Skipping cleanup \033[0m ")
                    break
                else:
                    print("\033[0;31m Please select y or n \033[0m ")
                    print(" Press ctrl + c for skipping cleanup")
            except KeyboardInterrupt:
                print("\n\033[0;33m Skipped by user \033[0m")
                break


if __name__ == "__main__":
    root = Storage("/")
    root.check_and_clean(["pacman", "-Sc"])

    home = Storage("/home")
    home.check_and_clean(["yay", "-Sc"])
