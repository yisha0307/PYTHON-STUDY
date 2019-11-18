# from urllib.request import urlopen
# for line in urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl'):
#     line = line.decode('utf-8')
#     if 'EST' in line or 'EDT' in line:
#         print(line)

from timeit import Timer
Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()