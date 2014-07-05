#!/usr/bin/python2.7
import sys
import os
import time

time_units = {
    's':1,
    'm':60,
    'h':60*60,
    'd':24*60*60,
}

if len(sys.argv) <= 1 or sys.argv[1] in ("-h", "-help", "--help"):
    print "HELP: ", sys.argv[0], "NUMBER[s,m,h,d] [NUMBER[s,m,h,d] [...]"
    exit(1)

time_to_sleep = 0

for arg in sys.argv:
    if arg == sys.argv[0]:
        continue

    if arg[-1] in time_units.keys():
        time_to_sleep += int(arg[:-1])*time_units[arg[-1]]
    else:
        time_to_sleep += int(arg)

try:
    for x in xrange(time_to_sleep, 0, -1):
        days    = x/60/60/24
        hours   = (x/(60*60))%24
        minutes = (x/60)%60
        seconds = x%60

        sys.stdout.write(
            "\rETA {0:02d}:{1:02d}:{2:02d}:{3:02d}".\
            format(days, hours, minutes, seconds)
        )
        sys.stdout.flush()

        time.sleep(1)
    sys.stdout.write("\nTime out!\n")
    sys.stdout.flush()
except KeyboardInterrupt:
    sys.stdout.write('\nAborted by Keyboard Interrupt!\n')

sys.exit()
