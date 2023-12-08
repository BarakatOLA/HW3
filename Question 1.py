from collections import deque
def processingqueue(inputfile):
    queue = deque()

    with open(inputfile, 'r') as file:
        for line in file:
            action, name = line.strip().split()
            if action == 'JUMP':
                queue.appendleft(name) 
            elif action == 'JOIN':
                queue.append(name)

    return list(queue)
# File path for the input file
input_file_path = 'hw3_q1.txt'

# Get the final order of people in the queue
final_order = processingqueue(input_file_path)

# Print the final order of people in the queue
print("Final order in the queue:", final_order)


