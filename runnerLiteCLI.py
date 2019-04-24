import argparse
from workoutCalculations import *
from dataAccess import *


def cliInterface():
    parser = argparse.ArgumentParser()

    parser.add_argument('kpiName',
                        help='Please specify which metric you would like to evaluate. The availible calculations are: \n' +
                             'greaterThanNkmStreaks\nranMoreThanNkm\nprNks')
    parser.add_argument('userID', help='Please specify the user. The availible IDs are:\n' +
                                       '6bd5f3c04e6b5279aca633c2a245dd9c\n' + '4e7aaa167b9b5ff7b9b3a22dee8c2085\n' +
                                       'c7e962db02da55209f02fe3d8a86c99d\nd77908482ed2505ebbf17ef72be2f080\n' +
                                       '72eff89c74cc57178e02f103187ad579\n40d7ae29e393582abdbcb8c726249e22')
    parser.add_argument('--dataSource', help='specify local or remote datasource. Default is local.', default='local',
                        required=False)

    args = parser.parse_args()

    switcher = {
        'greaterThanNkmStreaks': '{user_id: ' + args.userID + ', greater_than_3km_streaks: ' + str(
            greaterThanNkmStreaks(getUserWorkouts(args.userID, 'run', args.dataSource), 1, 3)) + '}',
        'ranMoreThanNkm': '{user_id: ' + args.userID + ', ran_more_than_10km: ' + str(
            ranMoreThanNkm(getUserWorkouts(args.userID, 'run', args.dataSource), 10)) + '}',
        'prNks': '{user_id: ' + args.userID + ', pace_5k_pr: ' + str(
            prNks(getUserWorkouts(args.userID, 'run', args.dataSource), 5, 2018)) + '}'
    }

    print(switcher[args.kpiName])


if __name__ == '__main__':
    cliInterface()
