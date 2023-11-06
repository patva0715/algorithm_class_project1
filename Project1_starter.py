def find_schedule(busy,avail,min):
    if avail == []:                                                               #O(1)
        return []                                                                 #O(1)
    if min <= 0:                                                                  #O(1)
        return []                                                                 #O(1)
    # For every array in busy, check if it needs to be modified/formatted
    busy_scheds = []                                                              #O(1)
    for i in range(len(busy)):                                                    #O(m), m == length of busy
        busy_scheds.append(modify(busy[i],avail[i]))                              #O(1) + O(k) -> O(k)

    # For every busy sched, calculate it's gap intervals (their available time intervals)
    all_gaps = []                                                                 #O(1)
    for sched in busy_scheds:                                                     #O(n)
        all_gaps.append(find_gaps(sched))                                         #O(n)

    # For every array in all_gaps, find its intersect with the student's login logout interval
    all_intersects = []                                                           #O(1)
    for i in range(len(avail)):                                                   #O(a), a == length of avail
        all_intersects.append(find_intersect(all_gaps[i],[avail[i]]))             #O(1 + n) -> O(n)


    # Find intersects of all array in all_intersects (this gives us the time intervals every member can meet)
    result = all_intersects[0]                                                    #O(1)
    for x in all_intersects[1::]:                                                 #O(n - 1) -> n
        result=find_intersect(result,x)                                           #O(n)

    # Filter result 
    result = filter(result,min)                                                   #O(n)

    # Format result. Decimal -> HH:MM
    return format_result(result)                                                  #O(n)
                                                                                  #Total Time Complexity == O(n^2)

def modify(array,interval):
    # This function adds [x,inf] or [-inf,x] to the array if needed. This is necessary so we can find all gaps
    formatted=[]                                                                  #O(1)
    # If end point of interval (x) greater than endpoint of array then append [x,inf] to array
    if array[-1][1] < interval[1]:                                                #O(1)
        array.append([interval[1],float('inf')])                                  #O(1)
    # If start point of interval (x) greater than startpoint of array then append [-inf,x] to beginning of array
    if array[0][0] > interval[0]:                                                 #O(1)
        formatted.append([float('-inf'),interval[0]])                             #O(1)
        formatted.extend(array)                                                   #O(k), k == number of vals added to the list
    else:
        formatted=array                                                           #O(1)
    return formatted                                                              #O(1)
                                                                                  #Total == O(6(1) + k) = O(k)

def find_gaps(intervals):
    if not intervals:                                                             #O(1)
        return []                                                                 #O(1)

    gaps = []                                                                     #O(1)
    prev_end = intervals[0][1]                                                    #O(1)

    for interval in intervals[1:]:                                                #O(n - 1) -> n
        start, end = interval                                                     #O(1)
        if start > prev_end:                                                      #O(1)
            gaps.append([prev_end, start])                                        #O(1)
        prev_end = max(prev_end, end)                                             #O(n)

    return gaps                                                                   #O(1)
                                                                                  #Total == O((n - 1) * (3(1) + n)) = O(n^2)

def find_intersect(arr1, arr2):
    if not arr1 or not arr2:                                                      #O(1)
        return []                                                                 #O(1)

    result = []                                                                   #O(1)
    i, j = 0, 0                                                                   #O(1)
    while i < len(arr1) and j < len(arr2):                                        #O(k + m) -> n
        start1, end1 = arr1[i]                                                    #O(1)
        start2, end2 = arr2[j]                                                    #O(1)

        # Calculate the intersection of the two intervals
        start = max(start1, start2)                                               #O(n)
        end = min(end1, end2)                                                     #O(n)
        if start <= end:                                                          #O(1)
            result.append([start, end])                                           #O(1)

        # Move the pointer for the interval that ends earlier
        if end1 < end2:                                                           #O(1)
            i += 1                                                                #O(1)
        else:
            j += 1                                                                #O(1)
    return result                                                                 #O(1)
                                                                                  #Total == O(n^2)

def filter(array,min):
    result=[]                                                                     #O(1)
    for x in array:                                                               #O(n)
        if x[1]-x[0]>=min:                                                        #O(1)
            result.append(x)                                                      #O(1)
    return result                                                                 #O(1)
                                                                                  #Total == O(4(1) + n) -> O(n)

def format_result(array):
    for x in array:                                                               #O(n) n == length of the array
        x[0]=convert_dec_to_time(x[0])                                            #O(1)
        x[1]=convert_dec_to_time(x[1])                                            #O(1)
    return array                                                                  #O(1)
                                                                                  #Total == O(3(1) + n) -> O(n)

def convert_dec_to_time(dec):
    # Extract the integer part (hours) and the fractional part (minutes)
    hours = int(dec)                                                              #O(1)
    minutes = int((dec - hours) * 60)                                             #O(1)
    # Format the result as HH:MM
    time_formatted = f"{hours:02d}:{minutes:02d}"                                 #O(1)
    return time_formatted                                                         #O(1)

if __name__ == "__main__":
    with open("output.txt", "w") as Outfile:                                      #O(1)                             
        with open('input.txt') as file:                                           #O(1)
            
            # 10 different inputs
            for j in range(10):                                                   #O(N) -> n == 10, number of trials
                busy = []                                                         #O(1)
                shift = []                                                        #O(1)
                # Reads the number of input users
                numOfInputs = int(file.readline().strip())                        #O(1)
                meeting_time = (int(file.readline().strip())) / 60                        #O(1)                                
                for _ in range(numOfInputs):                                      #O(n) -> n == number of employees
                    # Reads string from input -> list
                    temp = file.readline().strip()[1:-1].split("],[")             #O(1) + 2O(l) l == length of line = O(l)
                    busy_times = []                                               #O(1)

                    # Busy Schedule
                    for i in temp:                                                #O(k) -> k == number of busy intervals
                        start, end = i.split(",")                                 #O(6(1)) split schedule times -> O(1)
                        start_hr, start_min = map(int, start.split(':'))          #O(s) s == length of val of start time -> O(5(1)) -> O(1)
                        end_hr, end_min = map(int, end.split(':'))                #O(t) t == length of val of end time -> O(5(1)) -> O(1)
                        start_decimal_time = start_hr + (start_min / 60)          #O(1)
                        end_decimal_time = end_hr + (end_min / 60)                #O(1)
                        busy_times.append([start_decimal_time, end_decimal_time]) #O(1)
                    busy.append(busy_times)                                       #O(1)

                    # Shift Times
                    shift_time = file.readline().strip()[1:-1].split(",")         #O(1) + 2O(l) l == length of line = O(l)
            

                    shift_start_hr, shift_start_min = map(int, shift_time[0].split(":")) #O(s) s == length of val in [0] of shift time -> O(5(1)) -> O(1)
                    shift_end_hr, shift_end_min = map(int, shift_time[1].split(":")) #O(t) t == length of val in [1] of shift time -> O(5(1)) -> O(1)
                    start_dec = shift_start_hr + (shift_start_min / 60)           #O(1)
                    end_dec = shift_end_hr + (shift_end_min / 60)                 #O(1)
                    shift.append([start_dec, end_dec])                            #O(1)
                catch_val = find_schedule(busy,shift,meeting_time)                #O(n^2)
                Outfile.write(f"Output {j+1}: {catch_val}\n")                     #O(1)
            print("Done. Output saved in output.txt")                             #O(1)
                                                                                  #Total == O(N * (n^2))