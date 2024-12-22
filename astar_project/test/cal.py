from astar import astar
import time

ls = list(range(100000))


tr = []
def time_cal(name):
    def cal_time(func):
        def wrapper(*args,**kwargs):
            global tr
            start = time.time()
            rs = func(*args,**kwargs)
            stop = time.time()
            tr.append((name,stop-start))
            return rs
        return wrapper
    return cal_time


@time_cal(name="Loop Sum in Python")
def cal_sum_builtIn():
    s = 0
    for x in ls:
        s+=x
    return s

@time_cal(name="Loop Sum in C extension")
def cal_sum_custom():
    return astar.sum_integers(ls)




cal_sum_custom()
cal_sum_builtIn()

tr.sort(key=lambda x:x[1])

print("="*60)
print(f"{'Function Name':<30}|{'Result':<15}|{'Time (s)'}")
print("="*60) 

for name, time_taken in tr:
    print(f"{name:<30}|{'Success':<15}|{time_taken:<10.6f}")
print("="*60)
print(f"{'Multiplier':<30}|{'':<15}|{tr[1][1]//tr[0][1]:<15}")
print("="*60)