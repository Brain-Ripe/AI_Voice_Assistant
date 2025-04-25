import os
import time

print("Muting volume...")
os.system("nircmd.exe mutesysvolume 1")
time.sleep(2)

print("Unmuting volume...")
os.system("nircmd.exe mutesysvolume 0")
