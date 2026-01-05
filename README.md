# arch-linux-scripts-python

A collection of Python automation scripts designed for Arch Linux system administration. These tools help with package management, disk monitoring, and system maintenance using standard Python libraries and Arch-specific commands (`pacman`, `yay`).

## 📂 Included Tools

### 1. Package Manager Helper
A script to check for installed packages and batch-install missing ones.
- **Path:** `package_manager/checkpkg.py`
- **Features:** Checks installation status, bulk installs via `pacman`, handles permissions.

### 2. Disk Space Monitor & Cleaner
A monitoring tool that checks disk usage and prompts for cleanup if space is low.
- **Path:** `disk_monitor/cleaner.py`
- **Features:** Monitors Root (`/`) and Home (`/home`) partitions, alerts on low space (<10%), and automates cache cleaning (`pacman -Sc`, `yay -Sc`).

## 🚀 Getting Started

### Prerequisites
- **OS:** Arch Linux (or Arch-based distros like Manjaro, EndeavourOS)
- **Language:** Python 3.x
- **Tools:** `pacman` (required), `yay` (optional, for AUR cleaning)

### Installation
```bash
git clone https://github.com/YOUR_USERNAME/arch-linux-scripts-python.git
cd arch-linux-scripts-python
