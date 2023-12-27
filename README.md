# API Test Server
This is a simple Python server that support the Vizitest user guide.

## Installation
Clone the repository to your machine. Make sure Python and PIP are installed and running. 

- ```python3 --version```
- ```pip --version```


We suggest running the following to update pip and install the flask package.

- ```pip install --upgrade pip ```  
- ```python3 -m pip install flask``` 

## Starting the server.

- ```python3 api_test_server_starter.py```

## Changing Port
The port can be changed from server/constants.py.

## Check up and running

- ```http://localhost:33291/api``` should return API information and show it's up and running.

## Namespaces and endpoints
Our play server comes with a simple namespacing ability. This allows you to simulate development, staging, production environments.

Please refer to the Vizitest User Guide where you will find examples of test configurations using the play server.

Endpoints can be seen in ```http://localhost:33291/api``` but the user guide explain them in practical scenarios.

