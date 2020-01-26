import json


class ClientSecrets:
	__secrets = None
	
	@staticmethod
	def get(key):
		if ClientSecrets.__secrets == None:
			ClientSecrets.read()
		return ClientSecrets.__secrets[key]
	
	@staticmethod
	def read():
		print('Reading secrets')
		with open('credentials/client_secrets.json', 'r') as f:
			ClientSecrets.__secrets = json.loads(f.read())
