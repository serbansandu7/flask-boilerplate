import os

# Database config
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

# Server config
SERVER_HOST = os.getenv('LICENSING_HOST')
SERVER_PORT = int(os.getenv('LICENSING_PORT'))
