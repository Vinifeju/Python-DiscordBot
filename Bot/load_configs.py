import json

def load():
	dict = {}
	path = '../Config/config.json'

	with open(path, 'r') as config_file:
		data = json.loads(config_file.read())
		dict = data

	return dict