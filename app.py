from flask import Flask, send_from_directory
from dataAccess import *
import workoutCalculations

import os

app = Flask(__name__, static_url_path='/static')


@app.route('/')
def testlinks():
    return app.send_static_file('homepage.html')


@app.route('/allUserData/<userID>')
def allUserData(userID):
    return str(getUserWorkouts(userID))


@app.route('/allUserRuns/<userID>')
def allUserRuns(userID):
    return str(getUserWorkouts(userID, 'run'))


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
    data = getUserWorkouts(userID, 'run')
    timesPRThisYear = workoutCalculations.prNks(data, 5, 2018)
    return '{user_id: ' + userID + ', ran_more_than_10km: ' + str(timesPRThisYear) + '}'


if __name__ == '__main__':
    app.run()
