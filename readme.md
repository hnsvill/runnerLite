## RunnerLite:
This api has been written to use Flask with DynamoDB and the intention to deploy on an EC2 instance.

### To Run:
Make sure you have python3 and git lfs installed.
- `brew install python3`
- `brew install git-lfs`

Clone this repo and run
- `git lfs install`

Git should allow you to finish cloning. The lfs installation is for the submissionExplanation.pdf file.
See [the docs](https://git-lfs.github.com) for more information about git lfs.

In the project's directory, run the following commands:
- `pip3 install boto3`
- `pip3 install Flask`

#### Starting the runnerLite API:
Run the following command:
- `python3 app.py`

The server will spin up on port 5000. The index has links to the endpoints for each calculation for
each user and important links.

#### Using the runnerLite CLI:
Run the following commands:
- `python3 runnerLiteCLI.py --help` lists all of the options for the kpi you would like to calculate
- `python3 runnerLiteCLI.py <kpiName> <userID> <optional: --datasource>`

*A note on the datasource: The DynamoDB API key has not been included in this project's repo.
The datasource defaults to a local json file included in this repo.


### More Information:
Additional information about this project can be found in the "submissionExplanation.pdf" file. It 
is located at [static/submissionExplanation.pdf](https://github.com/hnsvill/runnerLite/blob/master/static/submissionExplanation.pdf), 
also linked on the index page of the app.