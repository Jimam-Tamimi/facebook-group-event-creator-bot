from threading import Thread
from time import sleep



pro = [ ]
for i in range(5):
    def run():
        for j in range(5):
            sleep(1)
        return "jimam"
    t = Thread(target=run)
    t.start()
    pro.append(t)

for t in pro:
    t.join()
    print(t.get_result())
    print(t)
    