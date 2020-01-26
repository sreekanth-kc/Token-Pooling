import os
from app.utils.client_secrets import ClientSecrets


class ConnectSqlClient(object):
    @staticmethod
    def connection_string():

        user = ClientSecrets.get('sql')['username']
        database_name = ClientSecrets.get('sql')['database_name']
        password = ClientSecrets.get('sql')['password']

        print("User :", user)
        print("Password:", password)
        print("database_name:", database_name)

        template = 'mysql://%s:%s@127.0.0.1/%s'
        return template % (user, password, database_name)