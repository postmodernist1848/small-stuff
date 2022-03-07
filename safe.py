class Event(object):
    def __init__(self):
        self.__eventhandlers = []

    def __iadd__(self, handler):
        self.__eventhandlers.append(handler)
        return self
    
    def __isub__(self, handler):
        self.__eventhandlers.remove(handler)
        return self
    
    def __call__(self, *args, **keywargs):
        for eventhandler in self.__eventhandlers:
            eventhandler(*args, **keywargs)

class Police(object):
    def __init__(self, policeTelephoneNo):
        self.telephone=policeTelephoneNo

    def CallPolice(self):
        print("Дзинь-дзинь")

class Vladelec(object):
    def __init__(self, ownerMobile):
        self._mobile=ownerMobile

    def Message(self):
        print("Отправлено SMS хозяину")

class Alarm(object):
    def StartAlarm(self):
        print("Виу-виу-виу-виу")

class Doors:
    def BlockDoors(self):
        print("Двери заблокированы")

class Windows:
    def CloseWindows(self):
        print("Окна заблокированы")

class Signalizacia(object):
    def __init__(self):
        self.OnLockBroken=Event()

    def Vzlom(self):
        self.OnLockBroken()

    def Dobavit_Signal(self, objMethod):
        self.OnLockBroken += objMethod

    def Udalit_Signal(self, objMethod):
        self.OnLockBroken -= objMethod

Real_obj_01 = Signalizacia()
localPoliceObj= Police("02")
ownerObj= Vladelec("9-916-255-54-55")
mainDoorAlarmObj= Alarm()
DoorsBlockObj = Doors()
WindowObj = Windows()

Real_obj_01.Dobavit_Signal(DoorsBlockObj.BlockDoors)
Real_obj_01.Dobavit_Signal(WindowObj.CloseWindows)
Real_obj_01.Dobavit_Signal(localPoliceObj.CallPolice)
Real_obj_01.Dobavit_Signal(ownerObj.Message)
Real_obj_01.Dobavit_Signal(mainDoorAlarmObj.StartAlarm)
Real_obj_01.Vzlom() 