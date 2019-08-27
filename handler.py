import boto3
import uuid
import csv
import redis
import base64
import os
     
s3_client = boto3.client('s3')
redis_host = os.environ['redisHost']
redis_port = os.environ['redisPort']

registro = redis.Redis(host=redis_host, port=redis_port, db=0)

def read_csv(file_path, resized_path):
    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                recordList(row[0])
                line_count += 1
        print('Processado {} linha.'.format(line_count))

def delet_object_s3(bucket, key):
    response = s3_client.delete_object(
        Bucket=bucket,
        Key=key
    )

def recordList(cpf):
    c = str(cpf)
    encoded = base64.b64encode(str(c).encode())
    registro.set(encoded, encoded)

def tap(event, context):
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key'] 
        download_path = '/tmp/{}{}'.format(uuid.uuid4(), key)
        upload_path = '/tmp/resized-{}'.format(key)
        
        s3_client.download_file(bucket, key, download_path)
        read_csv(download_path, upload_path)
    
    delet_object_s3(bucket, key)

    return { 
        'message' : 'ok'
    }
