import time
import dateutil.parser
from datetime import datetime

def getDateTimeFromISO8601String(s):
    d = dateutil.parser.parse(s)
    return d
def mergesort(array, left=0, right=None):
    global count
    if right is None:
        right = len(array)
    if right - left <= 1:
        return
    mid = left + (right - left) // 2
    count = count + 1
    mergesort(array, left, mid)
    count = count + 1
    mergesort(array, mid, right)
    merge(array, left, mid, right)

def merge(array, left, mid, right):
    buffer = array[left:mid]
    read_left = 0
    read_right = mid
    write = left

    while read_left < len(buffer) and read_right < right:
        if datetime.timestamp(getDateTimeFromISO8601String(array[read_right].split(' ')[0])) < datetime.timestamp(getDateTimeFromISO8601String(buffer[read_left].split(' ')[0])):
            array[write] = array[read_right]
            read_right += 1
        else:
            array[write] = buffer[read_left]
            read_left += 1
        write += 1

    while read_left < len(buffer):
        array[write] = buffer[read_left]
        read_left += 1
        write += 1


count=0
f_names = ['syslog1Mc_10k.log']
for file in f_names:
     print(file)

     start_time = time.time()
     f=open('syslog1Mc_10k.log','rb')
     file_content = f.read()
     file_content = str(file_content,'utf-8')
     file_content = file_content.splitlines()
     print("Time to read")
     print("runtime: %s seconds" % (time.time()-start_time))
     print("Merge Sort")
     start_time = time.time()
     mergesort(file_content)
     print("Run Time %s seconds" % (time.time()-start_time))
     print("count: ", count)

