from apscheduler.schedulers.blocking import BlockingScheduler
import random

i = -1
acceleration = []
def get_start_time():
    global i
    i = i + 1
    acceleration.append(round(random.uniform(-3.924, 3.924), 3))
    # acceleration[i] =
    print(i)
    print(acceleration[i])
    return i

sched = BlockingScheduler()
sched.add_job(get_start_time, 'interval', seconds=1)
sched.start()