import time


def sleep_time(pause_time_in_sec):
    for i in range(1, 100):
        if i % 2 == 0:
            print('Tick')
            time.sleep(pause_time_in_sec)
        else:
            print('Tock')
            time.sleep(pause_time_in_sec)


sleep_time(pause_time_in_sec=2)
