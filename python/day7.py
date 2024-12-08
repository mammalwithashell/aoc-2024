from functools import lru_cache

with open('input/day7.txt') as f:
    lines = f.readlines()


def evaluate_expression(numbers, operators):
    """
    Evaluates an expression left-to-right given a list of numbers and operators
    """
    result = numbers[0]
    for i in range(len(operators)):
        if operators[i] == '+':
            result += numbers[i + 1]
        elif operators[i] == '*':  # '*'
            result *= numbers[i + 1]
        else: # '||'
            result = int(f"{result}{numbers[i + 1]}")
    return result

def solve_equation(target, numbers, current_operators=None, position=0):
    """
    Recursively tries to find valid operator combinations that equal the target value.
    
    Args:
        target: The target value to achieve
        numbers: List of numbers in the equation
        current_operators: Current list of operators being built
        position: Current position in the operator list being filled
    
    Returns:
        List of lists containing valid operator combinations
    """
    if current_operators is None:
        current_operators = []
    
    # Base case: we've placed operators between all numbers
    if position == len(numbers) - 1:
        if evaluate_expression(numbers, current_operators) == target:
            return [current_operators[:]]  # Return a copy of the valid solution
        return []  # No valid solution found
    
    solutions = []
    # Try both operators (+ and *) at the current position
    for operator in ['+', '*', '||']:
        current_operators.append(operator)
        solutions.extend(solve_equation(target, numbers, current_operators, position + 1))
        current_operators.pop()  # Backtrack
        
    return solutions

def parse_equation(line):
    """
    Parses an input line into target value and numbers
    """
    parts = line.split(':')
    target = int(parts[0])
    numbers = [int(x) for x in parts[1].strip().split()]
    return target, numbers

def format_solution(numbers, operators):
    """
    Formats a solution into a readable string
    """
    result = str(numbers[0])
    for i in range(len(operators)):
        result += f' {operators[i]} {numbers[i+1]}'
    return result

# Part 1
target_sum = 0
for expression in lines:
    target, numbers = parse_equation(expression)
    solutions = solve_equation(target, numbers)
    if solutions:
        target_sum += target
print(target_sum)