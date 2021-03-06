import boto3
import click

session = boto3.Session(profile_name='default')
s3 = session.resource('s3')

@click.group()
def cli():
    "Webtron deploys websites to AWS"
    pass

@cli.command('list-buckets')
def list_buckets():
    "List all s3 buckets"
    for bucket in s3.buckets.all():
        print(bucket)

@cli.command('list-bucket-objects')
@click.argument('bucket')
def list_bucket_objects:
    "List objects in s3 bucket"
    for obj in s3.Bucket(bucket).objecys.all():
        print(obj)

if __name__ == '__main__':
    cli()
