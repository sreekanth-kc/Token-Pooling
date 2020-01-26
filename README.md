#Token Pooling
Simple Microservice for serving tokens.

## Installation

Setup virtual environment
```bash
sudo apt-get install -y python3-pip

sudo apt install python3-venv -y  && python3 -m venv venv && . venv/bin/activate

```

Install requirments

```
sudo pip3 install -r requirements.txt
```

Setup Cache
```
sudo apt-get install memcached

memcached -u root &

```
Run application

```
python main.py

```

API details

```
/post_token

Description:
    Create a token in Database.
params:
    token_name
--------------------------------
/get_token

Description:
    Get a token from the Microservice.
params:
    None
--------------------------------
/get_token_status

Description:
    Get usage status of all tokens.
params:
    None

```