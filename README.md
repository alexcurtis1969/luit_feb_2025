# Static Website CI/CD Pipeline with AWS CodePipeline

This project automates the deployment of a static website hosted on Amazon S3 using AWS CodePipeline and GitHub.

## Prerequisites

* AWS Account with appropriate permissions.
* GitHub Account with a repository containing your static website files (e.g., `index.html`).
* Python 3.6+
* Boto3 library (`pip install boto3`)
* python-dotenv library (`pip install python-dotenv`)

## Setup

1.  **Clone the Repository:**
    ```bash
    git clone <YOUR_GITHUB_REPO_URL>
    cd <PROJECT_DIRECTORY>
    ```

2.  **Create `.env` File:**
    * Create a `.env` file in the project's root directory.
    * Add the following environment variables:

        ```
        GITHUB_REPO_URL=<YOUR_GITHUB_REPO_URL>
        GITHUB_OAUTH_TOKEN=<YOUR_GITHUB_OAUTH_TOKEN>
        AWS_ACCOUNT_ID=<YOUR_AWS_ACCOUNT_ID>
        ```

    * Replace the placeholders with your actual values.
    * **Important:** Do not commit the `.env` file to your repository.

3.  **Create an IAM Role for CodePipeline:**
    * Go to the AWS IAM console.
    * Create a new role.
    * Select "AWS service" and "CodePipeline" as the service.
    * Attach the necessary policies:
        * Your custom codepipeline policy (if created)
        * `AWSCodePipelineServiceRole`
        * S3 permissions (e.g., `AmazonS3FullAccess` or a more restrictive policy)
        * Any other required AWS service permissions.
    * Note the Role ARN.

4.  **Update `CDA06.py`:**
    * Replace the placeholder `roleArn` in the `create_pipeline` function with the IAM Role ARN you created.
    * Verify the `REGION` variable.

5.  **Run the Script:**
    ```bash
    python CDA06.py
    ```

## Code Explanation

* **`CDA06.py`:**
    * Uses Boto3 to create an S3 bucket configured for static website hosting.
    * Creates an AWS CodePipeline that retrieves source code from GitHub and deploys it to the S3 bucket.
    * Uses environment variables for sensitive information.
* **`.env`:**
    * Stores sensitive information like GitHub OAuth token and AWS account ID.
* **`index.html`:**
    * A sample HTML file for the static website.

## Important Notes

* Ensure that the IAM role has the necessary permissions to access S3 and GitHub.
* Replace the placeholders in the `.env` file and `CDA06.py` with your actual values.
* The `index.html` file should be in the same directory as the `CDA06.py` script, or update the `HTML_FILE` variable accordingly.
* For production environments, consider using a more secure method for managing environment variables (e.g., AWS Secrets Manager).
* For S3 permissions, it is best to use a more restrictive policy than `AmazonS3FullAccess`.

## To Update the Website

1.  Make changes to your website files (e.g., `index.html`).
2.  Commit and push the changes to your GitHub repository.
3.  CodePipeline will automatically deploy the updated files to your S3 bucket.