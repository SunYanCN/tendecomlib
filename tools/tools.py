
from functools import reduce

def  float2front(order,index):
    pop_data = order.pop(index)
    order.insert(0, pop_data)
    return order

if __name__ == '__main__':
    print(float2front([0, 1, 2, 3, 4], 2))