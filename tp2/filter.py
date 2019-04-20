import numpy as np

def qrs2ecg(qrs,ecg):
    det=np.zeros(ecg.size)
    j=0
    for i in range(ecg.size):
        if qrs[j]==i :
            det[i]=5000
            j+=1
            if j>=qrs.size:
                break
    return det
