from flask import Flask
from dataAccess import *
import workoutCalculations

app = Flask(__name__)


@app.route('/addWorkout/<workoutData>')
def add_workout_to_db(workoutData):
    return 'Added ' + workoutData + ' to DB'


@app.route('/fullDashboard/<userID>')
def full_dashboard(userID):
    return '{user_id: ' + userID + '}'


@app.route('/greaterThan3kmStreaks/<userID>')
def greater_than_3km_streaks(userID):
    return '{user_id: ' + userID + ', greater_than_3km_streaks: ' + str('') + '}'


@app.route('/ranMoreThan10km/<userID>')
def ran_more_than_10km(userID):
    data = getUserWorkouts(userID, 'run')
    timesMoreThan10kmInWeek = workoutCalculations.ranMoreThan10km(data)
    return '{user_id: ' + userID + ', ran_more_than_10km: ' + str(timesMoreThan10kmInWeek) + '}'


@app.route('/pr5ks/<userID>')
def pr_5ks(userID):
    return '{user_id: ' + userID + ', ran_more_than_10km: ' + str('') + '}'


if __name__ == '__main__':
    app.run()
