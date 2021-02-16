import os
import awsconector
import json
import random

session = awsconector.get_session('us-east-1')
client = session.client('ec2')

def describe_and_count():
    k8s_ec2 = client.describe_instances(Filters=[{'Name': 'tag:k8s.io/cluster-autoscaler/ekslab01', 'Values': ['owned']}])
    instance_count = len(k8s_ec2['Reservations']) - 1
    gen_random_index = random.randrange(0, instance_count)
    target = k8s_ec2['Reservations'][gen_random_index]['Instances'][0]['InstanceId']
    return target

str_id = describe_and_count()
id = describe_and_count().split()

def terminate():
    result = client.terminate_instances(InstanceIds=id)
    x = result['TerminatingInstances'][0]['CurrentState']
    return x

print(terminate())
