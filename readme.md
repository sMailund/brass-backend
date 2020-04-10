# project brass backend
Simple ctf-like platform for irl treasure hunt. (don't let my friend know I'm planning his surprise birthday party)

## about
### purpose
Small project made for a friends surpise birthday party.
Project was limited in scope and 
only meant to be used a single day by a single user, 
so few resources were invested in 
architecture, robustness and security.
### solution
The following is a simple backend that serves as a thin layer between gcp data and the frontend (WIP) 
running on gcp app engine.

The API allows for basic read and modify operation on the task entity, 
which represents a task the birthdayboi<sup>tm</sup> has to complete.
On each of the IRL checkpoints, the birthdayboi<sup>tm</sup> has to complete a task, 
and is awarded with a solution string that is inputet via the frontend.
When the correct solution string is provided, 
the task is marked as solved and the birthdayboi<sup>tm</sup> can move on to the next task.

## usage
### run for local development
#### export gcp credentials
```
export GOOGLE_APPLICATION_CREDENTIALS="[path to credentials file]"
```
#### install dependencies
```
pip install -r requirements.txt
```
#### run project on local machine:
```
python main.py
```
### deploy to google cloud platform
```
gcloud app deploy
```

## API documentation
### get a specified task.
```
GET /task/<task_number>
```
### update specified task.
```
patch /task/<task_number>
```
This endpoint takes in form data.
If the form data contains a the field `reset` (with any value), 
the task is reset to unsolved without checking the answer string.

If not, the field `answer` is compared with the solution.
Returns `200` on correct answer string and `400` on incorrect answer string.
### list all tasks
```
GET /task/
```
Returns a list of all tasks, sorted by natural order.
### reset all tasks
```
PATCH /task/
```
Resets all tasks to unsolved
