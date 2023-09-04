from machine import Pin
import time

class FourSixMethod:
    STATUSES = { "powder": 0, "taste": 1, "strength": 2, "drip": 3  }
    POWDERS = [10, 20, 30, 40]
    TASTES = ['sweet', 'normal', 'bitter']
    STRENGTHS = ['light', 'normal', 'strong']

    led = Pin("LED", Pin.OUT)
    next_btn = Pin("SWITCH", Pin.IN, Pin.PULL_UP)
    decide_btn = Pin("BUTTON", Pin.IN, Pin.PULL_UP)
    reset_btn = Pin("SWITCH", Pin.IN, Pin.PULL_UP)


    def execute(self):
        self.status = 0

        while True:
            if self.status == self.STATUSES["powder"]:
                self.status = self.__select_powder()
            elif self.status == self.STATUSES["taste"]:
                self.status = self.__select_taste()
            elif self.status == self.STATUSES["strength"]:
                self.status = self.__select_strength()
            else:
                self.status = self.__drip()


    def __select_powder(self):
        selection = 0
        while True:
            if self.decide_btn.value() == 1:
                return self.STATUSES["taste"]
            elif self.reset_btn.value() == 1:
                return self.STATUSES["powder"]
            elif self.next_btn.value() == 1:
                selection +=1
                if selection > (len(self.POWDERS) - 1):
                    selection = 0


    def __select_taste(self):
        selection = 0
        while True:
            if self.decide_btn.value() == 1:
                return self.STATUSES["strength"]
            elif self.reset_btn.value() == 1:
                return self.STATUSES["powder"]
            elif self.next_btn.value() == 1:
                selection +=1
                if selection > (len(self.TASTES) - 1):
                    selection = 0


    def __select_strength(self):
        while True:
            if self.decide_btn.value() == 1:
                return self.STATUSES["drip"]
            elif self.reset_btn.value() == 1:
                return self.STATUSES["taste"]
            elif self.next_btn.value() == 1:
                selection +=1
                if selection > (len(self.STRENGTHS) - 1):
                    selection = 0


    def __drip(self):
        if self.reset_btn.value() == 1:
            return self.STATUSES["powder"]


FourSixMethod().execute()
