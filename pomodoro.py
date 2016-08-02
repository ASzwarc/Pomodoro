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

    def stop(self):
        self.cancel_timers()
        self.step = 'start'
        self.units_counter = 0
        logging.debug("Timers killed, members reset to initial state")

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

    def take_user_input(self):
        logging.info(self.step + " phase finished. 1 - Continue, 2 - Stop")
        return 1

    def cancel_timers(self):
        for key in self.timers.keys():
            self.timers[key].cancel()

    def control_function(self):
        if self.step == 'start':
            self.reset_counter()
            self.set_step('work')
            logging.debug("Starting sequence. Step = " + self.step + ", units = " + self.print_counter())
            self.timers['work'].run()
        elif self.step == 'work' and self.check_timer():
            self.units_counter += 1

            logging.debug("Small unit finished. Step = " + self.step + ", units = " + self.print_counter())

            if self.take_user_input() == 1:
                self.set_step('short_break')
                self.timers['short_break'].run()
            else:
                return
        elif self.step == 'work' and not self.check_timer():

            logging.debug("Big unit finished. Step = " + self.step + ", units = " + self.print_counter())
            if self.take_user_input() == 1:
                self.set_step('long_break')
                self.timers['long_break'].run()
            else:
                return
        elif self.step == 'short_break':

            logging.debug("Short break finished. Step = " + self.step + ", units = " + self.print_counter())
            if self.take_user_input() == 1:
                self.set_step('work')
                self.timers['work'].run()
            else:
                return
        elif self.step == 'long_break':
            logging.info("Pomodoro big unit finished!")
        else:
            raise ValueError("Undefined step value!")