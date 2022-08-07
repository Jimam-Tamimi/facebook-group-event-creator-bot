from threading import Thread
from time import sleep




for i in range(10):
    def run():
        for j in range(5):
            print({i, j})
        sleep(1)
    Thread(target=run).start()
    sleep(1)