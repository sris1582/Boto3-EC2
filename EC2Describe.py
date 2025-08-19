import boto3
client = boto3.client('ec2')
response = client.describe_instances()

for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        print("Running Instance Image ID: {} Running instance Instance Type: {} Running Instance Keyname {}"
              .format(instance['InstanceId'],instance['InstanceType'],instance['KeyName']))
