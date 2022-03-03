# 2) Best Time to Meet

# Billy is trying to figure out if there is a time that he and his team can meet to work on the project. His three teammates each give him a list of times they are available ('HH:MM' 24-hour). Create a function that will take in the list of all the teammates and return a list of times where everyone can meet.

billy_times = ['09:00', '10:30', '11:30', '12:00', '13:00', '14:30']
teammate_1 = ['09:30', '10:00', '10:30', '12:00', '14:30', '16:00']
teammate_2 = ['09:00', '09:30', '11:00', '11:30', '12:00', '13:30', '14:30', '15:00']
teammate_3 = ['11:00', '11:30', '12:00', '14:00', '14:30', '16:30', '17:00']
# Available Times: '12:00' and '14:30'

def find_times(*times):
    # time = [set(time) for time in times]
    # best_time = set.intersection(*time) # * is necessary
    # return best_time
    best_time = set.intersection(*[set(time) for time in times])
    return best_time


print(find_times(billy_times, teammate_1, teammate_2, teammate_3))