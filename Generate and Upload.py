import random
import re
import boto3

id_log = open("id-log.txt","a+")
id_log.seek(0)
inputFile = open("payment-template.json","r")

lines = []
global id_match
id_match = 1

def generate_id():
    global id_match
    while id_match != 0:
        id_match = 0
        old_ids = re.findall("[0-9]{4}",id_log.read())
        id_log.seek(0)
        global new_id
        new_id = str(random.randint(1000,9999))
        for old_id in old_ids:
            if old_id == new_id:
                id_match += 1
                new_id = str(random.randint(1000,9999))
                break
    return new_id            

def generate_amt():
    return str('{0:.2f}'.format(round((random.random() * 100), 2)))

for x in inputFile:
    lines.append(x)

new_id = generate_id()
outputFileName = "Payment-"+new_id
outputFile = open(outputFileName,"a")


for line in lines:
    match = re.search("<<.*>>",line)
    if match != None:
        if match.group() == "<<id>>":
            new_id = generate_id()
            outputLine = line.replace(match.group(),new_id)
            log_output = new_id+"\n"
            id_log.write(log_output)
        elif match.group() == "<<amt>>":
            outputLine = line.replace(match.group(),generate_amt())
        else:
            outputLine = line
    else:
        outputLine = line
    outputFile.write(outputLine)

inputFile.close()
outputFile.close()
id_log.close()

s3 = boto3.resource('s3')
bucket = s3.Bucket("alexwbucket1")
obj = bucket.Object(outputFileName)
obj.upload_file(outputFileName)

