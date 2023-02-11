class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        cur_gas = 0
        start = -1
        sum_gas = 0
        sum_cost = 0
        for i in range(len(gas)): 
            sum_gas += gas[i]
            sum_cost += cost[i]
            temp = gas[i] - cost[i]
            cur_gas += temp
            if cur_gas >= 0:
                if start == -1:
                    start = i
            else:
                start = -1
                cur_gas = 0
        if sum_gas < sum_cost:
            return -1
        return start