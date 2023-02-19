import os
import time

total_time = (10 * 1000) / 60 # modify (1000) to the amount of times you need to open
total_hours = total_time // 60
hours_min = total_time % 60

print("This will open Garry's Mod 1k times so you can get the achievement [Startup Millenium]")

if total_hours > 1:
    print(f"This will take {total_time} minutes or {total_hours} hours and {hours_min} minutes.")
elif total_hours == 1:
    print(f"This will take {total_time} minutes or {total_hours} hour and {hours_min} minutes.")
else:
    print(f"This will take {total_time} minutes.")

for i in range(1000): # modify (1000) to the amount of times you need to open
    os.startfile(r"D:\Steam\steamapps\common\GarrysMod\hl2.exe")
    time.sleep(5)
    os.system("taskkill /im hl2.exe /f")
    time.sleep(5)
