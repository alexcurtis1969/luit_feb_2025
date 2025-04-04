import boto3
import uuid
import os
import subprocess
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configuration
REGION = 'us-east-2'  # Change to your preferred AWS region
BUCKET_NAME = f"static-website-bucket-{uuid.uuid4()}"  # Unique bucket name
PIPELINE_NAME = f"static-website-pipeline-{uuid.uuid4()}"  # Unique pipeline name
HTML_FILE = "index.html"  # Name of your HTML file (assuming it's in the same directory)
BRANCH_NAME = "main"  # Main branch name
GITHUB_REPO_URL = os.getenv("GITHUB_REPO_URL") #Get the github repo url from the .env file.
GITHUB_OAUTH_TOKEN = os.getenv("GITHUB_OAUTH_TOKEN") #Get the oauth token from the .env file.
AWS_ACCOUNT_ID = os.getenv("AWS_ACCOUNT_ID") #Get the account id from the .env file.

# Create Boto3 clients
s3_client = boto3.client('s3', region_name=REGION)
codepipeline_client = boto3.client('codepipeline', region_name=REGION)

def create_s3_bucket(bucket_name):
    """Creates an S3 bucket for static website hosting."""
    try:
        s3_client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint': REGION})
        s3_client.put_bucket_website(Bucket=bucket_name, WebsiteConfiguration={'IndexDocument': {'Suffix': 'index.html'}})
        print(f"S3 bucket {bucket_name} created.")
        return f"http://{bucket_name}.s3-website.{REGION}.amazonaws.com"
    except Exception as e:
        print(f"Error creating S3 bucket: {e}")
        return None

def create_codepipeline(pipeline_name, bucket_name, branch_name):
    """Creates a CodePipeline for CI/CD using GitHub."""
    try:
        response = codepipeline_client.create_pipeline(
            pipeline={
                'name': pipeline_name,
                'roleArn': f'arn:aws:iam::{AWS_ACCOUNT_ID}:role/AWSCodePipelineServiceRole-us-east-1-codepipeline',  # Use account ID from .env
                'artifactStore': {
                    'type': 'S3',
                    'location': bucket_name,  # use the same bucket for both deployment and artifacts.
                },
                'stages': [
                    {
                        'name': 'Source',
                        'actions': [
                            {
                                'name': 'SourceAction',
                                'actionTypeId': {
                                    'category': 'Source',
                                    'owner': 'ThirdParty',
                                    'provider': 'GitHub',
                                    'version': '1'
                                },
                                'configuration': {
                                    'Owner': GITHUB_REPO_URL.split('/')[-2],  # Extract GitHub username
                                    'Repo': GITHUB_REPO_URL.split('/')[-1].replace(".git",""), #Extract repo name
                                    'Branch': branch_name,
                                    'OAuthToken': GITHUB_OAUTH_TOKEN
                                },
                                'outputArtifacts': [{'name': 'SourceOutput'}]
                            }
                        ]
                    },
                    {
                        'name': 'Deploy',
                        'actions': [
                            {
                                'name': 'DeployAction',
                                'actionTypeId': {
                                    'category': 'Deploy',
                                    'owner': 'AWS',
                                    'provider': 'S3',
                                    'version': '1'
                                },
                                'configuration': {
                                    'BucketName': bucket_name,
                                    'Extract': 'true'
                                },
                                'inputArtifacts': [{'name': 'SourceOutput'}]
                            }
                        ]
                    }
                ]
            }
        )
        print(f"CodePipeline {pipeline_name} created.")
    except Exception as e:
        print(f"Error creating CodePipeline: {e}")

def update_html_and_trigger_pipeline(html_file, branch_name, pipeline_name):
    """Updates the HTML file and triggers the CodePipeline."""
    try:
        with open(html_file, 'r') as f:
            content = f.read()

        updated_content = content.replace("Welcome", "Welcome to the Updated Page")  # example update.

        with open(html_file, 'wb') as f:
            f.write(updated_content.encode('utf-8'))

        subprocess.run(["git", "add", html_file], check=True)
        subprocess.run(["git", "commit", "-m", "Updated HTML file"], check=True)
        subprocess.run(["git", "push", "origin", branch_name], check=True)

        print(f"Updated {html_file} and triggered CodePipeline.")
    except Exception as e:
        print(f"Error updating HTML and triggering pipeline: {e}")

# Main execution

if not GITHUB_REPO_URL or not GITHUB_OAUTH_TOKEN or not AWS_ACCOUNT_ID:
    print("Error: GITHUB_REPO_URL, GITHUB_OAUTH_TOKEN, or AWS_ACCOUNT_ID environment variables are not set in .env file.")
else:
    website_url = create_s3_bucket(BUCKET_NAME)
    if website_url:
        create_codepipeline(PIPELINE_NAME, BUCKET_NAME, BRANCH_NAME)
        print(f"Website URL: {website_url}")
        print("Waiting for Pipeline to finish initial deploy.")
        input("Press Enter to continue and update the website")  # wait for user input to give the pipeline time.
        update_html_and_trigger_pipeline(HTML_FILE, BRANCH_NAME, PIPELINE_NAME)

print("Deployment process complete.")