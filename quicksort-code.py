import time
import dateutil.parser
from datetime import datetime
count=0
def getDateTimeFromISO8601String(s):
    d = dateutil.parser.parse(s)
    return d

def partition(arr, low, high):
    i = (low - 1)  # index of smaller element
    mid=int(low+(high-low)/2);
    pivot = datetime.timestamp(getDateTimeFromISO8601String(arr[mid] .split(' ')[0]))  # pivot

    for j in range(low, high):

        # If current element is smaller than the pivot
        if datetime.timestamp(getDateTimeFromISO8601String(arr[j].split(' ')[0])) < pivot:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)



def quickSort(arr, low, high):
    global count
    if low < high:

        pi = partition(arr, low, high)
        count= count+1
        quickSort(arr, low, pi - 1)
        count =count+1
        quickSort(arr, pi + 1, high)

f_names = ['syslog2500.log']
for file in f_names:
     print(file)
     start_time = time.time()
     f=open('syslog2500.log','rb')
     file_content = f.read()
     file_content = str(file_content,'utf-8')
     file_content = file_content.splitlines()
     print("Time to read")
     print("runtime: %s seconds" % (time.time()-start_time))
     print("Quick Sort")
     start_time = time.time()
     n=len(file_content)
     quickSort(file_content,0,n-1)
     print("Run Time %s seconds" % (time.time()-start_time))
     print("count:" ,count)