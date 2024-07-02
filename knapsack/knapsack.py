import time
class Item:
    def __init__(self,profit,weight,id):
        self.profit = profit
        self.weight = weight
        self.id = id
        self.p_by_w = profit/weight

def brute_0_1(items,m):
    def knapsack_recursive(i, m):
            if i == len(items) or m == 0:
                return 0, []
            elif items[i].weight > m:
                return knapsack_recursive(i + 1, m)
            else:

                include_value, include_items = knapsack_recursive(i + 1, m - items[i].weight)
                include_value += items[i].profit
                include_items = include_items + [i]
                exclude_value, exclude_items = knapsack_recursive(i + 1, m)

                if include_value > exclude_value:
                    return include_value, include_items
                else:
                    return exclude_value, exclude_items
    max_value, items_included = knapsack_recursive(0, m)
    combination =[0] * len(items)

    for i in range(len(combination)):
        if i in items_included:
            combination[i]=1
    return max_value, items_included,combination
def dynamic_0_1(items,m):
    dictionary ={}
    def knapsack_recursive(i, m):
            if i == len(items) or m == 0:
                return 0, []
            elif str(i) + "and"+ str(m) in dictionary:
                return dictionary[str(i)+ "and"+str(m)]
            elif items[i].weight > m:
                return knapsack_recursive(i + 1, m)
            else:
                include_value, include_items = knapsack_recursive(i + 1, m - items[i].weight)
                include_value += items[i].profit
                include_items = include_items + [i]
                exclude_value, exclude_items = knapsack_recursive(i + 1, m)

                if include_value > exclude_value:
                    dictionary[str(i)+ "and"+str(m)] = (include_value ,include_items)

                    return include_value, include_items
                else:
                    dictionary[str(i)+ "and"+str(m)] = (exclude_value ,exclude_items)
                    return exclude_value, exclude_items
    max_value, items_included = knapsack_recursive(0, m)
    combination =[0] * len(items)

    for i in range(len(combination)):
        if i in items_included:
            combination[i]=1
    return max_value, items_included,combination
def greedy_fractional(items:list[Item],m):
    temp_items = items.copy()
    temp_items.sort(key=lambda x:x.p_by_w,reverse=True)
    items = temp_items.copy()
    profit =0
    i = 0
    items_sel =[]
    combination =[0] * len(items)
    while i < len(items) and m > 0:
        if items[i].weight > m :
            profit += m/items[i].weight * items[i].profit
            
            items_sel.append(items[i].id)
            combination[items[i].id -1] = m/items[i].weight
            m = 0
        else :
            m -= items[i].weight
            profit += items[i].profit
            items_sel.append(items[i].id)
            combination[items[i].id -1] =1
        i +=1
    return profit,items_sel,combination
def brute_force_frational(items,m):
    n = len(items)
    comibnation = generate_combinations(n)
    max_profit =0
    best_combination =[]
    weights= [i.weight for i in items]
    profits= [i.profit for i in items]
    for comb in comibnation:
        object_added =[0]*n
        current_profit =0
        current_weight =0
        for i in range(n):
            if comb[i] ==1:
                if current_weight + weights[i]< m:
                    current_profit += profits[i]
                    current_weight +=weights[i]
                    object_added[i] = 1.0
        if current_weight < m:
            for i in range(n):
                if comb[i] == 0: 
                        fraction = (m - current_weight) / weights[i]
                        if fraction > 1:
                            fraction = 1
                        current_weight += weights[i] * fraction
                        current_profit += profits[i] * fraction
                        object_added[i] = fraction
                        if current_weight >= m:
                            break
        if current_profit > max_profit:
            max_profit =current_profit
            best_combination = object_added[:]
    itesm_included = []
    for i in range(len(best_combination)):
        if best_combination[i]>0:
            itesm_included.append(i)
    return max_profit,itesm_included,best_combination
def generate_combinations(n):
    combinations = []
    for i in range(2**n):
        bin_str = bin(i)[2:].zfill(n)
        combinations.append([int(bit) for bit in bin_str])
    return combinations


def print_items(items:list[Item]):
    for i in items:
        print(f"id:{i.id}, profit:{i.profit},weignht:{i.weight} and profit_by_w:{i.p_by_w}")
if __name__ == "__main__":
    items = [
        Item(profit=60, weight=10, id=1),
        Item(profit=100, weight=20, id=2),
        Item(profit=120, weight=30, id=3),
        Item(profit=80, weight=40, id=4),
        Item(profit=90, weight=50, id=5),
        Item(profit=70, weight=60, id=6),
        Item(profit=30, weight=10, id=7),
        Item(profit=50, weight=20, id=8),
        Item(profit=40, weight=30, id=9),
        Item(profit=100, weight=10, id=10)
    ]
    start_time = time.time()
    knap_sack = dynamic_0_1(items, 185)
    print("Time taken for dynamic is :",time.time()-start_time)
    print(knap_sack)
    start_time = time.time()
    knap_sack = brute_0_1(items, 185)
    print("Time taken for brute is :",time.time()-start_time)
    print(knap_sack)
    start_time = time.time()
    knap_sack = greedy_fractional(items, 185)
    print("Time taken for greedy_fractional is :",time.time()-start_time)
    print(knap_sack)
    start_time = time.time()
    knap_sack = brute_force_frational(items, 185)
    print("Time taken for brute_fractional is :",time.time()-start_time)
    val,it_sel,comb = knap_sack
    print(knap_sack)
    weight = 0
    for i in it_sel:

        weight +=items[i -1 ].weight
    print(weight)