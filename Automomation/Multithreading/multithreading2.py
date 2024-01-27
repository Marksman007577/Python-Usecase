import threading, time
print('Start of program.')


def take_a_nap():
    time.sleep(5)
    print('Wake up!')


threading_obj = threading.Thread(target=take_a_nap)
threading_obj.start()
print('End of program.')
