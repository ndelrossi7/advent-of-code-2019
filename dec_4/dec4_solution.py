# Part 1

start_range = 240920
end_range = 789857

def passwords(start, end):
    counter = 0
    for i in range(start, end+1):
        asc = True
        consec = False
        prev = ''
        for char in str(i):
            if char < prev:
                asc = False
                break
            if char == prev: 
                consec = True
            prev = char
        if asc == True and consec == True:
            counter += 1
    return counter

num_pass = passwords(start_range, end_range)


# Part 2