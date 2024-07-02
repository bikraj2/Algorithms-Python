class Activity:
    def __init__(self,id,start,finish):
        self.start = start
        self.finish = finish
        self.id = id
def sort_finish_time(acitivities:list[Activity]):
    return sorted(acitivities,key= lambda x:x.finish)
    

def acitivity_sel_recursive(activites,k,n):
    m = k + 1
    while m <= n and activites[m].start < activities[k].finish:
        m=m+1
    if m<=n:
        return {activities[m]} | acitivity_sel_recursive(activites,m,n)
    else :
        return  set()
def activity_iterative(activities):
    ans = {activities[1]}
    k = 1
    for m in range(k,len(activities)):
        if activities[m].start >=activities[k].finish:
            ans = ans | {activities[m]}
            k = m
    return ans
if __name__=="__main__":
    activities = [
    Activity(0, 0, 0),
    Activity(1, 1, 4),
    Activity(2, 3, 5),
    Activity(3, 0, 6),
    Activity(4, 5, 7),
    Activity(5, 3, 8),
    Activity(6, 5, 9),
    Activity(7, 6, 10),
    Activity(8, 8, 11),
    Activity(9, 8, 12),
    Activity(10, 2, 13),
    Activity(11, 12, 14)
    ]
    # activities = sort_finish_time(activities)
    ans =activity_iterative(activities)
    for i in ans:
        print(i.start,i.finish)



