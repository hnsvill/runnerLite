## RunnerLite:
This api has been written to use Flask with DynamoDB and the intention to deploy on an EC2 instance.

### To Run:
Clone this repo. In the project's directory, run the following commands:
- `pip3 install boto3`
- `pip3 install Flask`

#### To run using the API:
Run the following command:
- `python3 app.py`

The server will spin up on port 5000. The index has links to the endpoints for each calculation for
each user and important links.

#### To run from the command line:
Run the following commands:
- `python3 runnerLiteCLI.py --help` lists all of the options for the kpi you would like to calculate
- `python3 runnerLiteCLI.py <kpiName> <userID> <optional: --datasource>`

*A note on the datasource: The DynamoDB API key has not been included in this project's repo.
The datasource defaults to a local json file included in this repo.


### More Information:
Additional information about this project can be found in the "submissionExplanation.pdf" file. It 
is located at [static/submissionExplanation.pdf](https://github.com/hnsvill/runnerLite/blob/master/static/submissionExplanation.pdf), 
also linked on the index page of the app.