import boto3
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb')
workoutsTbl = dynamodb.Table('runnerTry')
kpis = dynamodb.Table('runnerTry')


def getUserWorkouts(userID, activityType = 'allTypes'):
    response = workoutsTbl.query(
        KeyConditionExpression=Key('user_id').eq(userID)
    )

    workoutData = response['Items']

    if activityType != 'allTypes':
        return list(filter(lambda x: x['type'] == activityType,  workoutData))

    return workoutData
