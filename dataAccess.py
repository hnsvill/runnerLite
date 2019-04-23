import boto3
from boto3.dynamodb.conditions import Key
from decimal import Decimal
import json

dynamodb = boto3.resource('dynamodb')
workoutsTbl = dynamodb.Table('workouts')
kpis = dynamodb.Table('metrics')


# DynamoDB data access
def getUserWorkouts(userID, activityType = 'allTypes', localOrRemote = 'local'):
    if localOrRemote == 'remote':
        response = workoutsTbl.query(
            KeyConditionExpression=Key('user_id').eq(userID)
        )
        workoutData = response['Items']

    else:
        workoutData = json.load(open('localDataManagement/allLocalData.json', 'r'))

    if activityType != 'allTypes':
        return list(filter(lambda x: x['type'] == activityType and x['user_id'] == userID, workoutData))

    return workoutData


if __name__ == '__main__':
    print(getUserWorkouts('72eff89c74cc57178e02f103187ad579'), 'local')
