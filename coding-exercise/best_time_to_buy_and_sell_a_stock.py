from typing import List
""" 
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104
"""

def maximum_profit(prices:List[int]) -> int:
    # Get size of price list.
    price_list_size = len(prices)

    # There is no data to compare.
    if price_list_size < 2:
        return 0

    # Variables to hold min and max prices range index.
    min_buy_price = prices[0]
    max_selling_price = 0
    new_min_buy_price = min_buy_price
    new_max_selling_price = max_selling_price
    
    # Loop to find max profit buy and sell day.
    for index in range(price_list_size):
        selling_price = prices[index] 
        
        if selling_price < new_min_buy_price:
            new_min_buy_price = selling_price
            new_max_selling_price = 0
            
        if index < price_list_size-1 and prices[index+1] > new_max_selling_price: 
            new_max_selling_price = prices[index+1]
        
        if  new_max_selling_price - new_min_buy_price > (max_selling_price - min_buy_price):
            max_selling_price = new_max_selling_price
            min_buy_price = new_min_buy_price
            
    if max_selling_price > min_buy_price:        
        return max_selling_price - min_buy_price
    return 0


def main():
    test_cases = {
        0:{"Prices":[2,4,1], "Expected":2},
        1:{"Prices":[7,6,4,3,1], "Expected":0},
        2:{"Prices":[7,1,5,3,6,4], "Expected":5},
        3:{"Prices":[1,2], "Expected":1},
        4:{"Prices":[3,2,6,5,0,3], "Expected":4},
        5:{"Prices":[1,2,4], "Expected":3},
        6:{"Prices":[2,1,2,1,0,1,2], "Expected":2},
        7:{"Prices":[3,3,5,0,0,3,1,4], "Expected":4},
    }
    
    for test_case in test_cases:
        result = maximum_profit(test_cases[test_case]["Prices"])
        pass_status = result == test_cases[test_case]["Expected"]
        # if not pass_status:
        print(test_case, "input" , test_cases[test_case]["Prices"] , " Expected = ", test_cases[test_case]["Expected"], " Output = ",result,"Result", result == test_cases[test_case]["Expected"])
    
if __name__ == "__main__":
    main()