#!usr/bin/python
from threading import Timer
import winsound
import logging

logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] (%(threadName)-10s) %(message)s')
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
    logging.info("Timer stopped")
    winsound.Beep(300, 1200)
    user_interface()

def user_interface():
    logging.info("Action:")
    logging.info("1 - Start working")
    logging.info("2 - Cancel timers and exit program")
    logging.info("What's your decision: ")
    chosen_option = input()

    if str(chosen_option) == "1":
        logging.debug("starting timer")
        run_timer(0)
    elif str(chosen_option) == "2":
        logging.debug("option 2")
        # Threads have to be saved in some structure to enable its canceling
        logging.info("Goodbye")
    else:
        logging.debug("option 3")
        logging.info("Goodbye")

def main():
    user_interface()

if __name__ == '__main__':
    main()