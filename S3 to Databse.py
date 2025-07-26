import boto3
import psycopg2
import json


db_host = "database-1.cleekikcy2cj.eu-north-1.rds.amazonaws.com"
db_name = "glue_db"
db_user = "postgres"
db_pass = "ueybfrvyersib234rfoub34q" 
connection = psycopg2.connect(host = db_host, database = db_name, user = db_user, password = db_pass)
cursor = connection.cursor()
print("Connection Successful")


data = []

s3 = boto3.resource('s3')
bucket = s3.Bucket("alexwbucket1")


insert = """INSERT INTO payment_info VALUES("""+((str(data).replace("[","")).replace("]",""))+""")"""

for obj in bucket.objects.all():
    data = []
    key = obj.key
    body = obj.get()["Body"].read()
    bodyDict = json.loads(body)
    for x in bodyDict:
        if x == "cardHolderDetails":
            detail_json = str(bodyDict.get(x))
            detail_json = detail_json.replace("'",'"')
            details = json.loads(detail_json)
            for i in details:
                data.append(details[i])
        else:
            data.append(bodyDict[x])
    print((str(data).replace("[","")).replace("]",""))
    final_data = (str(data).replace("[","")).replace("]","")
    insert = ("INSERT INTO payment_info\nVALUES("+final_data+")")
    cursor.execute(insert)
    connection.commit()

connection.close()
cursor.close()
