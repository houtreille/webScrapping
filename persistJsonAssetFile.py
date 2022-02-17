import json

import mysql.connector


config = {
            "user": "testuser",
            "password": "test623",
            "host": "localhost",
            "port": 3306,
            "database": "cryptomonitoring"
        }

connection = mysql.connector.connect(**config)
cur=connection.cursor()


def persist(jsonFile):

    x=json.loads(jsonFile)

    for asset in x:
        price=x[asset]['price']
        date=x[asset]['date']
        query= f'insert into assethp (ASSET,DATE,CLOSE,TYPE) VALUES ("{asset}",STR_TO_DATE("{date}","%Y-%m-%d"),{price},"SINGLE")'
        cur.execute(query)

    connection.commit()



