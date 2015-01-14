import pyttsx
engine = pyttsx.init()
import random

import datetime

sth = range(100, 1000)

for i in range(100):
    random.shuffle(sth)
    print(sth[:2], "ss")
    engine.say("{}".format(sth[:2]))
    early_date = datetime.datetime.now()
    a = raw_input()
    print(sum(sth[:2]))
    time_elapsed = (datetime.datetime.now() - early_date).seconds
    engine.say("{}".format(sum(sth[:2])))
    engine.say("{}".format(
        time_elapsed
    ))
    b = raw_input()
