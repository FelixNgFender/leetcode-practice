def carFleet(target, position, speed):
    # We observe that each fleet would have a leader.
    # A leader will not have cars in its fleet finish before it.
    # Number of leaders = number of fleets
    # We sort cars by their initial position in desc. order
    # To see if a car belongs to a fleet, its finish time must be
    # less than or equal to the current leader's finish time.
    # If not, it must be the leader of a SLOWER fleet.
    fleets = 1
    cars = [(position[i], speed[i]) for i in range(len(position))]
    cars.sort(reverse=True)
    leaderFinishTime = (target - cars[0][0]) / cars[0][1]
    for i in range(1, len(cars)):
        currentFinishTime = (target - cars[i][0]) / cars[i][1]
        if currentFinishTime > leaderFinishTime:
            fleets += 1
            leaderFinishTime = currentFinishTime
    return fleets


target = 12
position = [10, 8, 0, 5, 3]
speed = [2, 4, 1, 1, 3]
print(carFleet(target, position, speed))

target = 10
position = [3]
speed = [3]
print(carFleet(target, position, speed))

target = 100
position = [0, 2, 4]
speed = [4, 2, 1]
print(carFleet(target, position, speed))
