from pathlib import Path
import sys

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR))

from Array.OrderedRecordArray import *
from Queue import * 

def que_lab_iden(x): 
    return x[0]

def line_reader(line_str, que_lab):
    cus_counter = 1
    for i in line_str:
        if i.isalpha():
            if i.islower():
                i = i.upper()
                insert(i, que_lab, cus_counter)
                cus_counter += 1
            else:
                remove(i, que_lab, cus_counter)
                cus_counter += 1
        else: 
            print_current(que_lab)

def insert(item, que_lab, cus_counter):
    queue_name = que_lab.get(que_lab.find(item))
    c_string = "C" + str(cus_counter)
    queue_name[1].insert(c_string)

def remove(item, que_lab, cus_customer): 
    queue_name = que_lab.get(que_lab.find(item))
    queue_name[1].remove()
          
def print_current(que_lab): 
    for i in ("A", "B", "C", "D"):
        queue_name = que_lab.get(que_lab.find(i)) 
        print(f"\nCurrent state of queue_{i}", queue_name[1])

def main(): 
    que_lab = OrderedRecordArray(initialize=4, key=que_lab_iden)
    queue_A = Queue(10)
    queue_B = Queue(10)
    queue_C = Queue(10)
    queue_D = Queue(10)
    for i in (["A", queue_A],
            ["B", queue_B],
            ["C", queue_C],
            ["D", queue_D]): 
        que_lab.insert(i)

    line_reader('aaaAAAaabbB', que_lab)
    print_current(que_lab)

if __name__ == "__main__": 
    main() 



