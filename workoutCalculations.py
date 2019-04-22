from datetime import datetime, timedelta
from decimal import Decimal
from math import trunc


def prNks(userRunningData, distance, yearOf):  # section more out, like getting x amount of time's PR pace for X distance.

    thisYearsRunsMaxPacesByMonth = {}

    for workout in userRunningData:
        workout['start'] = datetime.strptime(workout['start'][:10], '%Y-%m-%d')

    # get last year's max pace for runs over distanceKm
    lastYearsRuns = list(filter(lambda x: 'pace' in x and x['start'].year == yearOf - 1, userRunningData))
    maxPaceFromLastYear = max([run['pace'] for run in lastYearsRuns if run['distance'] >= distance], default=0)

    # get this year's runs that were over distanceKm
    thisYearsRuns = list(filter(lambda x: 'pace' in x and x['start'].year == yearOf, userRunningData))
    thisYearsRunsFinal = [run for run in thisYearsRuns if run['distance'] >= distance]

    # get the max pace per month
    for i in range(12):
        thisYearsRunsMaxPacesByMonth[i+1] = max([run['pace'] for run in thisYearsRunsFinal if run['start'].month == i + 1], default=0)

    # loop through and count the times they PR'd by pace
    fastest = maxPaceFromLastYear
    thisYearsPRs = 0
    for currentMonthMaxPace in thisYearsRunsMaxPacesByMonth:
        if currentMonthMaxPace > fastest:
            fastest = currentMonthMaxPace
            thisYearsPRs = thisYearsPRs + 1

    return thisYearsPRs


def greaterThanNkmStreaks(userRunningData, requiredDistance, requiredStreakLengthDays):
    numDaysInCurrentStreak = 1
    streaksLengths = []

    for workout in userRunningData:
        workout['start'] = datetime.strptime(workout['start'][:10], '%Y-%m-%d')
    NkmRuns = list(filter(lambda x: 'distance' in x and x['distance'] >= requiredDistance, userRunningData))
    datesOfNkRuns = sorted({run['start'] for run in NkmRuns})  # had to do this in 2 steps to avoid key error

    # compare each with the next item
    for i in range(len(datesOfNkRuns)-1):
        if datesOfNkRuns[i] + timedelta(1) == datesOfNkRuns[i+1]:  # if the next element falls consecutively after the current,
            numDaysInCurrentStreak = numDaysInCurrentStreak + 1
        else:
            streaksLengths.append(numDaysInCurrentStreak)
            numDaysInCurrentStreak = 1

    return sum([trunc(streakLen/requiredStreakLengthDays) for streakLen in streaksLengths])


def ranMoreThanNkm(userRunningData, distance):

    numOfWeeksRanMoreThan10km = 0

    # convert to date/time and overwrite the date with the start of the week.
    for workout in userRunningData:
        convertedToDate = datetime.strptime(workout['start'][:10], '%Y-%m-%d')
        workout['start'] = convertedToDate - timedelta(convertedToDate.weekday())

    # get all of the workout week starting dates.
    weeksStarting = {x['start'] for x in userRunningData}

    # total distance for each week. If it's greater than or equal to 10, add to tally
    for weekStart in weeksStarting:
        workoutsThisWeek = list(filter(lambda x: x['start'] == weekStart, userRunningData))
        sumOfDistanceInWeek = sum([thisWorkout['distance'] for thisWorkout in workoutsThisWeek if 'distance' in thisWorkout])
        if sumOfDistanceInWeek >= distance:
            numOfWeeksRanMoreThan10km = numOfWeeksRanMoreThan10km + 1

    return numOfWeeksRanMoreThan10km


if __name__ == '__main__':
    print('yay!')


# Units: line55
    # distance: kilometers
    # speed: km / h
    # pace: minute / km
    # ascent / descent: meters
