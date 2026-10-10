
import boto3
import logging
import os

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Use the Lambda function's Region by default.
ec2 = boto3.client(
    "ec2",
    region_name=os.environ.get("AWS_REGION")
)


def get_instances_by_action(action):
    """Return instance IDs matching the Action tag."""
    response = ec2.describe_instances(
        Filters=[
            {
                "Name": "tag:Action",
                "Values": [action]
            },
            {
                "Name": "instance-state-name",
                "Values": [
                    "pending",
                    "running",
                    "stopping",
                    "stopped"
                ]
            }
        ]
    )

    instance_ids = []

    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            instance_ids.append({
                "id": instance["InstanceId"],
                "state": instance["State"]["Name"]
            })

    return instance_ids


def lambda_handler(event, context):
    """Stop Auto-Stop instances and start Auto-Start instances."""
    results = {
        "stopped": [],
        "started": [],
        "already_stopped": [],
        "already_running": []
    }

    # Stop instances tagged Action=Auto-Stop.
    for instance in get_instances_by_action("Auto-Stop"):
        instance_id = instance["id"]
        state = instance["state"]

        if state == "running":
            ec2.stop_instances(InstanceIds=[instance_id])
            logger.info("Stop requested for %s", instance_id)
            results["stopped"].append(instance_id)

        elif state == "stopped":
            logger.info("%s is already stopped", instance_id)
            results["already_stopped"].append(instance_id)

        else:
            logger.info(
                "Skipping %s because its state is %s",
                instance_id,
                state
            )

    # Start instances tagged Action=Auto-Start.
    for instance in get_instances_by_action("Auto-Start"):
        instance_id = instance["id"]
        state = instance["state"]

        if state == "stopped":
            ec2.start_instances(InstanceIds=[instance_id])
            logger.info("Start requested for %s", instance_id)
            results["started"].append(instance_id)

        elif state == "running":
            logger.info("%s is already running", instance_id)
            results["already_running"].append(instance_id)

        else:
            logger.info(
                "Skipping %s because its state is %s",
                instance_id,
                state
            )

    logger.info("Execution results: %s", results)

    return {
        "statusCode": 200,
        "body": results
    }
