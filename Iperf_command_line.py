import re
import sys
from math import ceil

# defaults:
port = 8000
v = 200
czas = '30'

# example invoke:  python prisma_ip.py --czas 20 -v 50 --port 9000

out = ''
iperfs = ''
with open('Prisma_IP.txt', 'r') as f:
    out += r"#!/bin/sh" + '\n'
    params = sys.argv[1:]
    for param in params[::2]:
        if re.search(r"(--czas|--time|-t|-c)", param):
            czas = params[params.index(param) + 1]
        if re.search(r"(-v|--downlink|--dl|-d)", param):
            v = params[params.index(param) + 1]
            try:
                v = int(v)
            except ValueError:
                raise ValueError("Error - v must be a pure number")
        if re.search(r"(-p|--port)", param):
            port = params[params.index(param) + 1]

    for line in f:
        if re.match(r".*PDN address assigned:.*?user \d\d\d.*", line):
            user = int(re.search(r"user \d\d\d", line)[0][-3:])
            ip = re.search(r"\d+\.\d+\.\d+\.\d+", line)[0]
            out += 'ue{}="{}"\n'.format(user, ip)

    out += '\n'
    vPerUE = str(ceil(int(v) / user)) + 'M'
    for i in range(user):
        out += "iperf -u -i 1 -t "+czas+" -p " + str(int(port) + i) + " -l 1300 -b " + vPerUE + " -c $ue" + str(
            i + 1) + " >> iperf" + str(i + 1) + ".txt &\n"

print(out)
with open("prisma_output.txt", 'w') as f:
    f.write(out)
