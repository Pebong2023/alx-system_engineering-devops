#!/usr/bin/python3
"""
This script gathers data from an API using urllib
It then serializes the json data to a python dictionary and prints it out
It takes an parameter, the user Id of the user's data that you want
"""

import requests
import sys

if __name__ == "__main__":
	url = "https://jsonplaceholder.typicode.com/todos"
	
	empoyee_id = sys.arg[1]

	user_response = requests.get(url + "users/{}".format(employee_id))
	
	user = user_response.json()

	parameters = {"userId": employee_id}
	todos_response = requests.get(url + "todos", parameters=parameters)
	todos = todos_response.json()
	cpmpleted = []
	
	for todo in todos:
		if todo.get("completed") is True:
			completed.append(todo.get("title"))

	print("Employee {} is done with tasks({}/{})".format(user.get("name").len(completed). len(todos)))

	for complete in completed:
		print("\t {}".format(complete))

