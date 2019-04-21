from datetime import datetime, timedelta
from decimal import Decimal
from math import trunc


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


def prNks(userRunningData, distance):  # section more out, like getting x amount of time's PR pace for X distance.
    # get last year's max pace for runs over distanceKm
    # get this year's runs that were over distanceKm
    # group everything by month
    # get the max for each month
    # sort by date
    # loop through and count the times they PR'd by pace
    return ''


if __name__ == '__main__':
    response = [{'user_id': 'd77908482ed2505ebbf17ef72be2f080', 'distance': Decimal('4.478512443021909'),
                 'ascent': Decimal('81.33643397688866'), 'descent': Decimal('80.4417839050293'),
                 'calories': Decimal('60.935'), 'pace': Decimal('13.360429553618925'), 'steps': Decimal('6388'),
                 'end': '2017-12-02T20:01:09.756000Z', 'speed': Decimal('4.490873572530299'),
                 'start': '2017-12-02T18:58:13Z', 'activity_id': '254369755c4e59b48f72717075dc3456', 'type': 'run'},
                {'user_id': 'd77908482ed2505ebbf17ef72be2f080', 'distance': Decimal('1.334750197192503'),
                 'descent': Decimal('6.8222527503967285'), 'calories': Decimal('107.624'),
                 'pace': Decimal('11.704499737998676'), 'steps': Decimal('1807'), 'end': '2018-01-16T00:41:37.261000Z',
                 'speed': Decimal('5.12623361468495'), 'start': '2018-01-16T00:25:57Z',
                 'activity_id': '869942d3c43e5f66afec49526fb2d5a6', 'type': 'run'},
                {'user_id': 'd77908482ed2505ebbf17ef72be2f080', 'distance': Decimal('5.5344684198995795'),
                 'ascent': Decimal('9.61392728984356'), 'descent': Decimal('8.326112833991644'),
                 'calories': Decimal('446.039'), 'pace': Decimal('12.599824959268377'), 'steps': Decimal('7882'),
                 'end': '2018-01-28T19:48:46.610000Z', 'speed': Decimal('4.761970915783577'),
                 'start': '2018-01-28T18:38:59Z', 'activity_id': 'c456c887e36f5352b19ba37f85a1f183', 'type': 'run'},
                {'user_id': 'd77908482ed2505ebbf17ef72be2f080', 'distance': Decimal('4.295745239046658'),
                 'ascent': Decimal('10.98809027671814'), 'descent': Decimal('23.580438494682312'),
                 'calories': Decimal('344.588'), 'pace': Decimal('12.745169220544955'), 'steps': Decimal('6259'),
                 'end': '2018-01-30T04:00:09.215000Z', 'speed': Decimal('4.707666015393598'),
                 'start': '2018-01-30T03:05:21Z', 'activity_id': 'cf95db0decc751d1b0d8bc62bacf346f', 'type': 'run'},
                {'user_id': 'd77908482ed2505ebbf17ef72be2f080', 'distance': Decimal('6.107463362456542'),
                 'ascent': Decimal('12.875235080718994'), 'descent': Decimal('5.715232342481613'),
                 'calories': Decimal('400.779'), 'pace': Decimal('12.018359991486992'), 'steps': Decimal('7089'),
                 'end': '2018-02-04T20:07:59.943000Z', 'speed': Decimal('4.99236169015573'),
                 'start': '2018-02-04T19:06:33Z', 'activity_id': 'eecc01012a6653979761045704249464', 'type': 'run'},
                {'user_id': 'd77908482ed2505ebbf17ef72be2f080', 'distance': Decimal('0.5228733835008679'),
                 'ascent': Decimal('1.1092855632305145'), 'descent': Decimal('10.84444808959961'),
                 'calories': Decimal('42.686'), 'pace': Decimal('14.981319723879828'), 'steps': Decimal('846'),
                 'end': '2018-02-24T23:29:41.033000Z', 'speed': Decimal('4.004987618304519'),
                 'start': '2018-02-24T22:45:10Z', 'activity_id': 'fd66e96c1dbd5a20b97937acd1f5f80d', 'type': 'run'},
                {'user_id': 'd77908482ed2505ebbf17ef72be2f080', 'distance': Decimal('2.443870362459134'),
                 'ascent': Decimal('4.28290230631827'), 'descent': Decimal('6.290907746553408'),
                 'calories': Decimal('193.358'), 'pace': Decimal('12.439285023862777'), 'steps': Decimal('3543'),
                 'end': '2018-03-23T01:56:41.207000Z', 'speed': Decimal('4.823428346958816'),
                 'start': '2018-03-23T01:26:12Z', 'activity_id': '4f831a24d1d65155a6748b33ad0118d1', 'type': 'run'}]
    print(ranMoreThanNkm(response))


# Units: line55
    # distance: kilometers
    # speed: km / h
    # pace: minute / km
    # ascent / descent: meters
