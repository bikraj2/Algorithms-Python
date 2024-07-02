from cProfile import label
import matplotlib.pyplot as plt
import time
from n_queen import NQueens
import numpy as np


def graph_time():
    fig,ax = plt.subplots()
    input_size =[]
    time_taken=[]
    for i in range(4,14):
        start_time = time.time()
        prob = NQueens(i)
        prob.backTrack(1)
        time_taken.append(time.time() -start_time)
        input_size.append(i)
    ax.plot(input_size, time_taken, color='green',linewidth=2.0,label="Insertion Sort")
    plt.xlabel("Size of N-Queen")
    plt.ylabel("Time")
    plt.title("NQueen BackTracking")
    plt.legend()
    plt.savefig("NQueen BackTracking" + ".png", dpi=300, bbox_inches='tight')
    plt.cla()

        
        
        
if __name__ =="__main__" :
    graph_time()
