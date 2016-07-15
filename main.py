#!usr/bin/python
from threading import Timer
import winsound
import logging

logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] (%(threadName)-10s) %(message)s')
work_time = 0.1
short_break = 0.05
long_break = 0.2
unit_size = 4


class PomodoroTimer:

    def __init__(self, work_time, short_break, long_break, unit_size):
        self.unit_size = unit_size
        self.step = 'start'
        self.units_counter = 0
        self.timers = {'work' : Timer(work_time * 60, program_control, args=['work']),
                       'short_break' : Timer(short_break * 60, program_control, args=['short_break']),
                       'long_break' : Timer(long_break * 60, program_control, args=['long_break'])}
    def start(self):
        pass

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
            self.timers['work'].start()
        elif self.step == 'work' and self.check_timer():
            winsound.Beep(300, 1200)
            self.units_counter += 1
            self.set_step('short_break')
            logging.debug("Small unit finished. Step = " + self.step + ", units = " + self.print_counter())
            self.timers['short_break'].start()
        elif self.step == 'short_break' and not self.check_timer():
            winsound.Beep(300, 1200)
            self.set_step('long_break')
            logging.debug("Big unit finished. Step = " + self.step + ", units = " + self.print_counter())
            self.timers['long_break'].start()
        elif self.step == 'short_break' and self.check_timer():
            winsound.Beep(300, 1200)
            self.unit
            logging.debug("Short break finished. Step = " + self.step + ", units = " + self.print_counter())
            run_timer('work')
        elif self.step == 'long_break':
            winsound.Beep(300, 1200)
            logging.info("Pomodoro big unit finished!")
            user_interface()
        else:
            raise ValueError("Undefined step value!")

def run_timer(length_type):
    if length_type == 'work':
        elapsed_time = Timer(work_time * 60, program_control, args=['work']).
    elif length_type == 'short_break':
        elapsed_time = Timer(short_break * 60, program_control, args=['short_break'])
    elif length_type == 'long_break':
        elapsed_time = Timer(long_break * 60, program_control, args=['long_break'])
    else:
        raise ValueError("Allowed types of timers are in range [0;2]!")
    elapsed_time.start()

def program_control(step):
    global pomodoro_units_counter
    if step == 'start':
        pomodoro_units_counter = 0
        logging.debug("Starting sequence. Step = " + step + ", units = " + str(pomodoro_units_counter))
        run_timer('work')
    elif step == 'work' and pomodoro_units_counter < unit_size:
        winsound.Beep(300, 1200)
        pomodoro_units_counter +=1
        logging.debug("Small unit finished. Step = " + step + ", units = " + str(pomodoro_units_counter))
        run_timer('short_break')
    elif step == 'work' and pomodoro_units_counter >= unit_size:
        winsound.Beep(300, 1200)
        pomodoro_units_counter = 0
        logging.debug("Big unit finished. Step = " + step + ", units = " + str(pomodoro_units_counter))
        run_timer('long_break')
    elif step == 'short_break':
        winsound.Beep(300, 1200)
        logging.debug("Short break finished. Step = " + step + ", units = " + str(pomodoro_units_counter))
        run_timer('work')
    elif step == 'long_break':
        winsound.Beep(300, 1200)
        logging.info("Pomodoro big unit finished!")
        user_interface()
    else:
        raise ValueError("Undefined step value!")

def user_interface():
    logging.info("Action:")
    logging.info("1 - Start working")
    logging.info("2 - Cancel timers and exit program")
    logging.info("What's your decision: ")
    chosen_option = input()

    if str(chosen_option) == "1":
        logging.debug("starting timer")
        program_control('start')
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