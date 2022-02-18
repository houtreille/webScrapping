import mysql.connector

conn = mysql.connector.connect(
        host="localhost",
        user="testuser",
        password="test623",
        database="cryptomonitoring"
        )


def retrieveCryptoFromDB(crypto='%',date=None):


    query= f'Select  asset, CLOSE, date_format(DATE, "%Y%m%d")  from assethp where asset like "{crypto}"'
    if date:
        query+=f' and date=STR_TO_DATE("{date}","%Y%m%d")'

    mycursor = conn.cursor()
    mycursor.execute(query)

    cryptoValue={}
    records=mycursor.fetchall()
    for record in records:
        if not record[2] in cryptoValue:
            cryptoValue[record[2]]={}
        cryptoValue[record[2]][record[0]]=float(record[1])

    return cryptoValue

