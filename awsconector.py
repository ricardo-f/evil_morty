#Open a session with aws
import boto3

def get_session(region):
# the profile_name need to match your aws cli profile
    return boto3.session.Session(region_name=region, profile_name='dev')
