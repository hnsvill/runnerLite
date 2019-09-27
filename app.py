from flask import Flask
import workoutCalculations
from dataAccess import *

app = Flask(__name__, static_url_path='/static')

localOrRemoteData = 'local'


@app.route('/')
def testlinks():
    return app.send_static_file('homepage.html')


@app.route('/allUserData/<userID>')
def allUserData(userID):
    return str(getUserWorkouts(userID))


@app.route('/allUserRuns/<userID>')
def allUserRuns(userID):
    return str(getUserWorkouts(userID, 'run'))


@app.route('/addWorkout/<workoutData>')  # TODO: add a workout, recalculate KPI's, update table
def add_workout_to_db(workoutData):
    return 'Added ' + workoutData + ' to DB'


@app.route('/fullDashboard/<userID>')  # TODO: make a table, place current KPIs there, handle for new users
def full_dashboard(userID):
    return '{user_id: ' + userID + '}'


@app.route('/greaterThan3kmStreaks/<userID>/<requiredDistance>')
def greater_than_3km_streaks(userID, requiredDistance):
    data = getUserWorkouts(userID, 'run', localOrRemoteData)
    numStreaks = workoutCalculations.greaterThanNkmStreaks(data, int(requiredDistance), 3)
    return '{user_id: ' + userID + ', greater_than_3km_streaks: ' + str(numStreaks) + '}'

# @app.route('/greaterThan1kmStreaks/<userID>')
# def greater_than_1km_streaks(userID):
#     data = getUserWorkouts(userID, 'run', localOrRemoteData)
#     numStreaks = workoutCalculations.greaterThanNkmStreaks(data, 1, 3)
#     return '{user_id: ' + userID + ', greater_than_3km_streaks: ' + str(numStreaks) + '}'


@app.route('/ranMoreThan10km/<userID>')
def ran_more_than_10km(userID):
    data = getUserWorkouts(userID, 'run', localOrRemoteData)
    timesMoreThan10kmInWeek = workoutCalculations.ranMoreThanNkm(data, 10)
    return '{user_id: ' + userID + ', ran_more_than_10km: ' + str(timesMoreThan10kmInWeek) + '}'


@app.route('/pr5ks/<userID>')
def pr_5ks(userID):
    data = getUserWorkouts(userID, 'run', localOrRemoteData)
    timesPRThisYear = workoutCalculations.prNks(data, 5, 2018)
    return '{user_id: ' + userID + ', pace_5k_pr: ' + str(timesPRThisYear) + '}'


if __name__ == '__main__':
    app.run()
