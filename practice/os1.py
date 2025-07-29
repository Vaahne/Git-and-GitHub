#!/usr/bin/env python3
import os
def check_reboot():
        """Reboot True if the computer has a pending reboot."""
        return os.path.exists("/run/reboot-required")
def main():
    pass    # pass means do something later, do nothing now 

main()