# project brass backend
Simple ctf-like platform for irl treasure hunt. (don't let my friend know I'm planning his surprise birthday party)

## about
Small project made for a friends surpise birthday party.
Project was limited in scope and 
only meant to be used a single day by a single user, 
so few resources were invested in 
architecture, robustness and security.

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


