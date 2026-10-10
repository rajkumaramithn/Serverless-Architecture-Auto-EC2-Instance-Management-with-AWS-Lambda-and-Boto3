# Automated EC2 Instance Management Using AWS Lambda and Boto3

## 1. Project Overview

This project demonstrates how to automate the starting and stopping of Amazon **EC2** instances using **AWS** Lambda and Boto3, the **AWS** **SDK** for Python.

The Lambda function identifies **EC2** instances based on their tags and performs the required action automatically.

- **Action=Auto-Stop:** Stops instances that are running.
- **Action=Auto-Start:** Starts instances that are stopped.

This automation helps reduce unnecessary compute usage and demonstrates the practical application of serverless computing and cloud resource management.

## 2. Objectives

- Create and configure **EC2** instances.
- Apply tags to identify the required instance actions.
- Create an **AWS** Lambda function using Python and Boto3.
- Configure **IAM** permissions for **EC2** instance management.
- Test the function using a manual Lambda invocation.
- Verify execution results by checking the instance states.
  
## 3. Technologies Used

| Technology | Purpose |
|---|---|
| Amazon EC2 | Virtual server instances |
| AWS Lambda | Serverless execution of the Python function |
| Python | Programming language |
| Boto3 | AWS SDK for Python |
| AWS IAM | Access control and permissions |
| GitHub | Source code management and documentation |

## 4. Project Architecture

## Two EC2 instances are created.

## Each instance is assigned an `Action` tag. ## The Lambda function is invoked manually. ## Boto3 queries EC2 for instances matching each tag. ## Running `Auto-Stop` instances receive a stop request. ## Stopped `Auto-Start` instances receive a start request. ## Execution messages are recorded in CloudWatch Logs. ## The resulting instance states are verified in the EC2 console.

## 5. EC2 Instance Configuration

| Instance Name | Tag Key | Tag Value | Expected Final State |
|---|---|---|---|
| ec2-auto-stop | Action | Auto-Stop | Stopped |
| ec2-auto-start | Action | Auto-Start | Running |

### Screenshots

****EC2** instances Setup**

![**EC2** instances](Screenshots/GAOSA_1.png)

![**EC2** instances](Screenshots/GAOSA_2.png)

![**EC2** instances](Screenshots/GAOSA_3.png)

![**EC2** instances](Screenshots/GAOSA_4.png)

![**EC2** instances](Screenshots/GAOSA_5.png)

![**EC2** instances](Screenshots/GAOSA_6.png)

![**EC2** instances](Screenshots/GAOSA_7.png)

![**EC2** instances](Screenshots/GAOSA_8.png)

![**EC2** instances](Screenshots/GAOSA_9.png)

![**EC2** instances](Screenshots/GAOSA_10.png)

![**EC2** instances](Screenshots/GAOSA_11.png)

![**EC2** instances](Screenshots/GAOSA_12.png)

**Auto-Stop tag**

![Auto-Stop tag](screenshots/02-auto-stop-tag.png)

**Auto-Start tag**

![Auto-Start tag](screenshots/03-auto-start-tag.png)

## 6. IAM Configuration

An **IAM** role named `Lambda-**EC2**-Instance-Management-Role` is assigned to the Lambda function.

The custom **IAM** policy grants these permissions:

- `ec2:DescribeInstances`
- `ec2:StopInstances`
- `ec2:StartInstances`

These permissions allow the function to identify instances and request the required state changes.

![**IAM** role configuration](screenshots/04-iam-role.png)

## 7. Lambda Function Configuration

| Setting | Value |
|---|---|
| Function name | ec2-tag-based-instance-manager |
| Runtime | Python 3.x |
| SDK | Boto3 |
| Execution role | Lambda-EC2-Instance-Management-Role |
| Invocation method | Manual test event |

The function uses **EC2** tag filters to identify matching instances and checks their current states before requesting changes.

![Lambda function overview](screenshots/05-lambda-overview.png)

### Source Code

The complete implementation is available in [`lambda_function.py`](lambda_function.py).

## 8. Testing Procedure

## Ensure the `Auto-Stop` instance is running.

## Ensure the `Auto-Start` instance is stopped. ## Open the Lambda function in the AWS Console. ## Create a test event containing an empty JSON object: `{}`. ## Invoke the function. ## Review the execution response. ## Inspect CloudWatch Logs for instance IDs and action messages. ## Refresh the EC2 Instances page and verify the final states.

## 9. Test Results

Record the actual results obtained during execution.

| Test Case | Expected Result | Actual Result |
|---|---|---|
| Stop tagged instance | Instance becomes stopped | Update after testing |
| Start tagged instance | Instance becomes running | Update after testing |
| Lambda invocation | Successful execution | Update after testing |

### Lambda Invocation

![Lambda test result](screenshots/07-lambda-test-success.png)

### Final EC2 Instance States

![Final **EC2** instance states](screenshots/09-final-instance-states.png)

## 10. Key Learnings

- Understanding **EC2** instance states and tags.
- Creating Lambda functions using Python.
- Using Boto3 to interact with **AWS** services.
- Configuring **IAM** roles and permissions.
- Maintaining project documentation using GitHub.

## 11. Conclusion

This project demonstrates tag-based **EC2** instance management using **AWS** Lambda and Boto3. It automates starting and stopping instances based on their tags, records execution details in CloudWatch, and verifies the resulting instance states.

## 12. References

- [**AWS** Lambda Documentation](https://docs.aws.amazon.com/lambda/)
- [Boto3 Documentation](https://docs.aws.amazon.com/boto3/)
- [**EC2** Instance Management with Boto3](https://docs.aws.amazon.com/boto3/latest/guide/ec2-example-managing-instances.html)
- [Amazon **EC2** **API** Reference](https://docs.aws.amazon.com/boto3/latest/reference/services/ec2.html)
