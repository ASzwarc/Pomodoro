#!usr/bin/python
from threading import Timer
import winsound
import logging

logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] (%(threadName)-10s) %(message)s')

class PomodoroTimer:

    def __init__(self, work_time, short_break, long_break, unit_size):
        self.unit_size = unit_size
        self.step = 'start'
        self.units_counter = 0
        self.timers = {}
        self.create_timers(work_time, short_break, long_break)

    def create_timers(self, work_time, short_break, long_break):
        self.timers['work'] = Timer(work_time * 60, self.timer_callback)
        self.timers['short_break'] = Timer(short_break * 60, self.timer_callback)
        self.timers['long_break'] = Timer(long_break * 60, self.timer_callback)

    def start(self):
        self.control_function()

    def timer_callback(self):
        winsound.Beep(300, 1200)
        self.control_function()

    def reset_counter(self):
        self.units_counter = 0

    def print_counter(self):
        return str(self.units_counter)

    def set_step(self, step):
        self.step = step

    def check_timer(self):
        return self.units_counter < self.unit_size

    def control_function(self):
        if self.step == 'start':
            self.reset_counter()
            self.set_step('work')
            logging.debug("Starting sequence. Step = " + self.step + ", units = " + self.print_counter())
            self.timers['work'].run()
        elif self.step == 'work' and self.check_timer():
            self.units_counter += 1
            self.set_step('short_break')
            logging.debug("Small unit finished. Step = " + self.step + ", units = " + self.print_counter())
            self.timers['short_break'].run()
        elif self.step == 'work' and not self.check_timer():
            self.set_step('long_break')
            logging.debug("Big unit finished. Step = " + self.step + ", units = " + self.print_counter())
            self.timers['long_break'].run()
        elif self.step == 'short_break':
            self.set_step('work')
            logging.debug("Short break finished. Step = " + self.step + ", units = " + self.print_counter())
            self.timers['work'].run()
        elif self.step == 'long_break':
            logging.info("Pomodoro big unit finished!")
        else:
            raise ValueError("Undefined step value!")

def user_interface():
    timer = PomodoroTimer(0.2, 0.05, 0.3, 4)
    logging.info("Action:")
    logging.info("1 - Start working")
    logging.info("2 - Cancel timers and exit program")
    logging.info("What's your decision: ")
    chosen_option= input()

    if str(chosen_option) == "1":
        logging.debug("starting timer")
        timer.start()
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