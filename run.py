import os
import awsconector
import json
import random
from discord_webhook import DiscordWebhook

session = awsconector.get_session('us-east-1')
client = session.client('ec2')

#webhook = DiscordWebhook(url=os.environ['DISCORDX9'], content='Evil Morty Starting, let us see your resilience :) https://media.giphy.com/media/U7K7nYUedeKm3q9Qru/giphy.gif')
#response = webhook.execute()

def describe_and_count():
    k8s_ec2 = client.describe_instances(Filters=[{'Name': 'tag:Name', 'Values': ['CE-POC']}])
    instance_count = len(k8s_ec2['Reservations']) - 1
    gen_random_index = random.randrange(0, instance_count)
    target = k8s_ec2['Reservations'][gen_random_index]['Instances'][0]['InstanceId']
    return target

str_id = describe_and_count()
id = describe_and_count().split()

def shutdown():
    result = client.stop_instances(InstanceIds=id)
    x = result['StoppingInstances'][0]['CurrentState']
    return x

print(shutdown())

#webhook = DiscordWebhook(url=os.environ['DISCORDX9'], content='Evil Morty Finished ' + str_id + ' finalizada! https://media.giphy.com/media/Spo8GBTweRoTHwrG7X/giphy.gif')
#response = webhook.execute()
