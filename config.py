import os

DB_DETAILS = {
    'dev': {
        'SOURCE_DB': {
            'DB_TYPE': 'mysql',
            'DB_HOST': '139.99.209.131',
            'DB_NAME': os.environ.get('DB_NAME'),
            'DB_USER': os.environ.get('DB_USER'),
            'DB_PASS': os.environ.get('DB_PASS'),
        },
        'TARGET_DB': {
            'DB_TYPE': 'postgres',
            'DB_HOST': '139.99.209.131',
            'DB_NAME': os.environ.get('DB_NAME'),
            'DB_USER': os.environ.get('DB_USER'),
            'DB_PASS': os.environ.get('DB_PASS'),
        }
    }
}