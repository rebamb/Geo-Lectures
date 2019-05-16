# Lecture 5: Snuffler exercise functions 
# 
# author: Eva Eibl eva.eibl@uni-potsdam.de
# SS 2019: Module MGPW02
# 16.5.2019
# -----------------------------
import Lec5_geyserEx_functions as h
import matplotlib.pyplot as plt
import numpy as np

# -- import the snuffler marker file, time in julian days --
julianday, eventclass = h.read_snuffler_marker("Markers.txt", length=0)
julianday = np.sort(julianday)
#plt.plot(julianday)
#plt.show()

# -- calculate the waiting time after eruption/ duration of bursts in minutes --  
waittime = []

for i in range(1, len(julianday)):
    waittime.append((julianday[i] - julianday[i-1])*24*60)

waittime=np.diff(julianday)*24*60

plt.plot(waittime)
plt.show()


# -- calculate mean time --



# -- plot waiting time after eruptions/ duration of bursts vs. time --
plot


# -- plot histogram of the intereruption times (1 h bins) -- 
hist













