from dataAccess import *
from workoutCalculations import *

# TODO: Refactor to use Argparse. Add local data as an option.
#   The finished command should look like:
#       `runnerLite --pr5ks --40d7ae29e393582abdbcb8c726249e22`


def runCalcs():
    desiredCalc = input('Which calculation would you like to perform? Type your selection and press' +
                        'enter.\n3-day, 1km streaks\nran more than 10km\n5k PRs\n\n').lower()
    userID = input('What user would you like the calculation for? Type the user ID and press enter.\n\n')
    data = getUserWorkouts(userID, 'run', 'local')

    calcOptions = ['ran more than 10km', '3-day, 1km streaks', '5k prs']

    if desiredCalc not in calcOptions:
        print('Calculation choice is not one of the listed options. Please try again.')
    elif data is None:
        print('Error loading user data.')
    else:
        if desiredCalc == 'ran more than 10km':
            kpi = ranMoreThanNkm(data, 10)
            header = 'ran_more_than_10km'
        elif desiredCalc == '3-day, 1km streaks':
            kpi = greaterThanNkmStreaks(data, 1, 3)
            header = 'greater_than_3km_streaks'
        elif desiredCalc == '5k prs':
            kpi = prNks(data, 5, 2018)
            header = 'pace_5k_pr'

        print('{user_id: ' + str(userID) + ', ' + header + ': ' + str(kpi) + '}')


if __name__ == '__main__':
    runCalcs()
