import winsound
import time
frequency = 1000  # Set Frequency To 2500 Hertz
duration = 100  # Set Duration To 1000 ms == 1 second
message = [0, 1, 0, 0, 1, 0, 1, 1, 0]
durations = [200, 400]

for symbol in message:
    winsound.Beep(frequency, durations[symbol])
    # time.sleep(0.2)