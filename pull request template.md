# Pull Request Template

## Description

Please include a summary of the changes and the related issue. Please also include relevant motivation and context. List any dependencies that are required for this change.

Fixes # (issue)

## Type of Change

Please delete options that are not relevant.

- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Documentation update

## Checklist

- [ ] My code follows the style guidelines of this project
- [ ] I have performed a self-review of my own code
- [ ] I have commented my code, particularly in hard-to-understand areas
- [ ] I have made corresponding changes to the documentation
- [ ] My changes generate no new warnings
- [ ] I have added tests that prove my fix is effective or that my feature works
- [ ] New and existing unit tests pass locally with my changes
- [ ] Any dependent changes have been merged and published in downstream modules

## How to Test

Please describe the tests that you ran to verify your changes. Provide instructions so that the reviewer can reproduce them. Please also list any relevant details for your test configuration.

- [ ] Test A

import unittest
from unittest.mock import patch, MagicMock

class TestSSMParameterRetrieval(unittest.TestCase):

    @patch('boto3.client')
    def test_retrieve_parameters(self, mock_boto_client):
        ssm_mock = MagicMock()
        mock_boto_client.return_value = ssm_mock
        ssm_mock.get_parameter.return_value = {'Parameter': {'Value': 'fake_value'}}
        
        access_key_id_aws = ssm_mock.get_parameter(Name='access_key_id_aws')['Parameter']['Value']
        secret_access_key_aws = ssm_mock.get_parameter(Name='secret_access_key_aws')['Parameter']['Value']

        self.assertEqual(access_key_id_aws, 'fake_value')
        self.assertEqual(secret_access_key_aws, 'fake_value')

if __name__ == '__main__':
    unittest.main()

- [ ] Test B

import unittest
from unittest.mock import patch, MagicMock

class TestCloud9EnvironmentCreation(unittest.TestCase):

    @patch('boto3.client')
    def test_create_environment(self, mock_boto_client):
        cloud9_mock = MagicMock()
        mock_boto_client.return_value = cloud9_mock
        cloud9_mock.create_environment_ec2.return_value = {'environmentId': 'fake_env_id'}

        response = cloud9_mock.create_environment_ec2(
            name='test_env',
            instanceType='t2.micro',
            imageId='amazonlinux-2-x86_64'
        )

        self.assertEqual(response['environmentId'], 'fake_env_id')

if __name__ == '__main__':
    unittest.main()

    - [ ] Test C

    import unittest
from unittest.mock import patch, MagicMock

class TestLambdaFunctionCreation(unittest.TestCase):

    @patch('boto3.client')
    def test_create_function(self, mock_boto_client):
        lambda_mock = MagicMock()
        mock_boto_client.return_value = lambda_mock
        lambda_mock.create_function.return_value = {'FunctionArn': 'fake_function_arn'}

        response = lambda_mock.create_function(
            FunctionName='test_function',
            Runtime='python3.8',
            Handler='lambda_function.lambda_handler',
            Role='fake_role_arn',
            Code={'S3Bucket': 'fake_bucket', 'S3Key': 'fake_key'}
        )

        self.assertEqual(response['FunctionArn'], 'fake_function_arn')

if __name__ == '__main__':
    unittest.main()


**Test Configuration**:
* Firmware version:
* Hardware:
* Toolchain:
* SDK:

## Screenshots

Please add screenshots of the relevant changes (if applicable).

## Additional Context

Add any other context or comments about the pull request here.
