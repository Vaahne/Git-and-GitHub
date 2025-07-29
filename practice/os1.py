#!/usr/bin/env python3
import os
import sys

def check_reboot():
        """Reboot True if the computer has a pending reboot."""
        return os.path.exists("/run/reboot-required")
def main():
    if check_reboot():
        print ("Pending Reboot!!")
        sys.exit(1)
    # if disk_ful():
    #     print("Disk full")
    #     sys.exit(1)
    print ("Everything ok!!")
    sys.exit(0)
    # pass    # pass means do something later, do nothing now 

main()