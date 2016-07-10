#!usr/bin/python
from threading import Timer
import winsound

work_time = 0.2
short_break = 0.1
long_break = 0.3
pomodoro_units_counter = 0

def run_timer(length_type):
    if length_type == 0:
        elapsed_time = Timer(work_time * 60, on_timeout)
    elif length_type == 1:
        elapsed_time = Timer(short_break * 60, on_timeout)
    elif length_type == 2:
        elapsed_time = Timer(long_break * 60, on_timeout)
    else:
        raise ValueError("Allowed types of timers are in range [0;2]!")
    elapsed_time.start()

def on_timeout():
    print("Timer stopped")
    winsound.Beep(300, 1200)

def main():
    while True:
        print("Action:")
        print("1 - Start working")
        print("2 - Cancel timers and exit program")
        chosen_option = input("What's your decision: ")

        if chosen_option == "1":
            run_timer(0)
        elif chosen_option == "2":
            #Threads have to be saved in some structure to enable its canceling
            break
        else:
            break
    print("Goodbye")

if __name__ == '__main__':
    main()