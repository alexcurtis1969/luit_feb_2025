# Pull Request Template: Static Website CI/CD Pipeline with AWS CodePipeline

## Description

This pull request introduces a CI/CD pipeline for deploying a static website hosted on Amazon S3, using AWS CodePipeline and GitHub. It automates the process of updating the website whenever changes are pushed to the main branch of the specified GitHub repository.

This includes:

* Creation of an S3 bucket configured for static website hosting.
* Setup of an AWS CodePipeline to pull source code from GitHub and deploy it to S3.
* Use of environment variables for sensitive information (GitHub OAuth token, AWS Account ID).
* A basic `index.html` file for testing the deployment.

Fixes: N/A (New Feature)

## Type of change

- [x] New feature (non-breaking change which adds functionality)

## How Has This Been Tested?

- [x] Manual tests: Verified that the S3 bucket is created correctly, the CodePipeline is set up and working, and that changes pushed to the GitHub repository are reflected on the deployed website.
- [x] Manual tests: Verified that the environment variables are correctly loaded and used by the script.

## Checklist:

- [x] My code follows the style guidelines of this project (PEP 8 where applicable).
- [x] I have performed a self-review of my own code.
- [x] I have commented my code, particularly in hard-to-understand areas.
- [x] I have added a `README.md` file explaining the setup and usage of the code.
- [x] My changes generate no new warnings.
- [x] New and existing unit tests pass locally with my changes (N/A - manual testing was used).
- [x] Any dependent changes have been merged and published in downstream modules (N/A).

## Additional Notes

* Ensure that the `.env` file is created and contains the correct environment variables.
* The IAM role used for CodePipeline needs appropriate permissions to access S3 and GitHub.
* The `index.html` file is a basic example; you can replace it with your actual website content.
* For production environments, consider more robust error handling and security measures (e.g., AWS Secrets Manager for environment variables).
* The S3 Bucket permissions should be reviewed and tightened.