from flask import Flask
from dataAccess import *
import workoutCalculations

app = Flask(__name__)


@app.route('/allUserData/<userID>')
def allUserData(userID):
    return str(getUserWorkouts(userID))


@app.route('/addWorkout/<workoutData>')  # TODO: add a workout, recalculate, update table
def add_workout_to_db(workoutData):
    return 'Added ' + workoutData + ' to DB'


@app.route('/fullDashboard/<userID>')  # TODO: make a table, place current KPIs there, handle for new users
def full_dashboard(userID):
    return '{user_id: ' + userID + '}'


@app.route('/greaterThan3kmStreaks/<userID>')
def greater_than_3km_streaks(userID):
    data = getUserWorkouts(userID, 'run')
    numStreaks = workoutCalculations.greaterThanNkmStreaks(data, 1, 3)
    return '{user_id: ' + userID + ', greater_than_3km_streaks: ' + str(numStreaks) + '}'


@app.route('/ranMoreThan10km/<userID>')
def ran_more_than_10km(userID):
    data = getUserWorkouts(userID, 'run')
    timesMoreThan10kmInWeek = workoutCalculations.ranMoreThanNkm(data, 10)
    return '{user_id: ' + userID + ', ran_more_than_10km: ' + str(timesMoreThan10kmInWeek) + '}'


@app.route('/pr5ks/<userID>')  # TODO: Calculation
def pr_5ks(userID):
    return '{user_id: ' + userID + ', ran_more_than_10km: ' + str('') + '}'


if __name__ == '__main__':
    app.run()
