import time
import csv
class Item:
    def __init__(self,profit,weight,id):
        self.profit = profit
        self.weight = weight
        self.id = id
        self.p_by_w = profit/weight
class KnapSack:
    def __init__(self,p_w_dict:list[Item] ,capacity:int,) :
        self.items = p_w_dict
        self.fractional =True 
        self.capacity = capacity
        self.length = len(self.items) 
    def brute_force_zero_one(self):
        def knapsack_recursive(index, remaining_capacity):
            if index == self.length or remaining_capacity == 0:
                return 0, []
            elif self.items[index].weight > remaining_capacity:
                return knapsack_recursive(index + 1, remaining_capacity)
            else:

                include_value, include_items = knapsack_recursive(index + 1, remaining_capacity - self.items[index].weight)
                include_value += self.items[index].profit
                include_items = include_items + [index]
                exclude_value, exclude_items = knapsack_recursive(index + 1, remaining_capacity)

                if include_value > exclude_value:
                    return include_value, include_items
                else:
                    return exclude_value, exclude_items
        max_value, items_included = knapsack_recursive(0, self.capacity)
        combination =[0] * self.length

        for i in range(len(combination)):
            if i in items_included:
                combination[i]=1
        return max_value, items_included,combination

    def brute_force_frational(self):
        n=self.length
        capacity = self.capacity
        items =self.items
        def generate_combinations(n):
            combinations = []
            for i in range(2 ** n):
                bin_str = bin(i)[2:].zfill(n)
                combinations.append([int(bit) for bit in bin_str])
            return combinations
        weights = [item.weight for item in items]
        profits = [item.profit for item in items]
        combinations = generate_combinations(n)
        max_profit = 0
        best_combination = []
        for x in combinations:
            objects_added = [0.0] * n
            current_weight = 0
            current_profit = 0
            
            for i in range(n):
                if x[i] == 1:
                    if current_weight + weights[i] <= capacity:
                        current_weight += weights[i]
                        objects_added[i] = 1.0
                        current_profit += profits[i]
            
            if current_weight < capacity:  
                for i in range(n):
                    if x[i] == 0: 
                        fraction = (capacity - current_weight) / weights[i]
                        if fraction > 1:
                            fraction = 1
                        current_weight += weights[i] * fraction
                        current_profit += profits[i] * fraction
                        objects_added[i] = fraction
                        if current_weight >= capacity:
                            break
            if current_profit > max_profit:
                max_profit = current_profit
                best_combination = objects_added[:]
        solutions = []
        for i in range(len(best_combination)):
            if best_combination[i] >=0:
                solutions.append(i)
        return max_profit,solutions,best_combination

    def greedy_fractional(self):
        if self.items == []:
            return 0,[],[]
        temp_items =self.items.copy()
        temp_items.sort(key=lambda i:i.p_by_w,reverse=True)
        total_profit = 0
        capacity = self.capacity
        i = 0
        solution = []
        combination =[0]*self.length
        while i >=0 and capacity > 0:
            weight = temp_items[i].weight 
            profit =  temp_items[i].profit 
            if (capacity - weight) <0:
                total_profit += profit * (capacity)/weight
                
                solution.append(temp_items[i].id-1)
                combination[temp_items[i].id -1] = capacity/weight
                capacity = 0
                break
            else:
                capacity-=weight
                total_profit +=profit
                solution.append(temp_items[i].id-1)
                combination[temp_items[i].id -1] = 1
            i+=1
        return total_profit,solution,combination
    def dynamic(self):
        dictionary = {}
        def knapsack_recursive(index, remaining_capacity):
            if index == self.length or remaining_capacity == 0:
                return 0, []
            elif str(index) + str(remaining_capacity) in dictionary:
                return dictionary[str(index) + str(remaining_capacity)]
            elif self.items[index].weight > remaining_capacity:
                return knapsack_recursive(index + 1, remaining_capacity)
            else:

                include_value, include_items = knapsack_recursive(index + 1, remaining_capacity - self.items[index].weight)
                include_value += self.items[index].profit
                include_items = include_items + [index]
                exclude_value, exclude_items = knapsack_recursive(index + 1, remaining_capacity)

                if include_value > exclude_value:
                    dictionary[str(index) + str(remaining_capacity)] = (include_value,include_items)
                    return dictionary[str(index) + str(remaining_capacity)]
                else:
                    dictionary[str(index) + str(remaining_capacity)] = (exclude_value,include_items)
                    return dictionary[str(index) + str(remaining_capacity)]
        max_value, items_included = knapsack_recursive(0, self.capacity)
        combination =[0] * self.length
        for i in range(len(combination)):
            if i in items_included:
                combination[i]=1
        return max_value, items_included,combination

        

def time_knapsack_methods():
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
    knap_sack = KnapSack(items, 185)
    
    times = {}

    start = time.time()
    print(knap_sack.brute_force_zero_one())
    end = time.time()
    times['brute_force_zero_one'] = end - start

    start = time.time()
    print(knap_sack.brute_force_frational())
    end = time.time()
    times['brute_force_fractional'] = end - start

    start = time.time()
    print(knap_sack.greedy_fractional())
    end = time.time()
    times['greedy_fractional'] = end - start

    start = time.time()
    print(knap_sack.dynamic())
    end = time.time()
    times['dynamic'] = end - start

    # with open('knapsack_time.csv', 'w', newline='') as file:
    #     writer = csv.writer(file)
    #     writer.writerow(["Method", "Time"])
    #     for method, duration in times.items():
    #         writer.writerow([method, duration])
    
    # print("Timing results saved to knapsack_time.csv")

if __name__ == "__main__":
    time_knapsack_methods()