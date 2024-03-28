#!/usr/bin/python3
import random
import sys
from time import sleep
import datetime

for i in range(40):
    sleep(random.random())
    sys.stdout.write("{:d}.{:d}.{:d}.{:d} - [{}] \"GET /projects/260 HTTP/1.1\" {} {}\n".format(
        random.randint(1, 255), random.randint(1, 255), random.randint(1, 255), random.randint(1, 255),
        datetime.datetime.now(),
        random.choice([200, 301, 400, 401, 403, 404, 405, 500]),
        random.randint(1, 1024)
    ))
    # print(texto)
    # parts = texto.split()
    # if parts[7].isdigit and parts[8].isdigit:
    #     print (parts[7])
    #     print (parts[8])

    sys.stdout.flush()

