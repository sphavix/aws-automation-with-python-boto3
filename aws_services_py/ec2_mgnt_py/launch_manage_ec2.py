"""
This script launches and manages an EC2 instance using the Boto3 library.
"""

import boto3

# create ec2 resource and instance name
ec2 = boto3.resource('ec2')
instance_name = 'boto3-ec2-instance'

# store instance id
instance_id = None
instance_exits = False

# check if instance which is being launched already exists
# and only manage an existing instance
def check_instance_exists():
    global instance_id
    instances = ec2.instances.filter(Filters=[{'Name': 'tag:Name', 'Values': [instance_name]}])
    for instance in instances:
        for tag in instance.tags:
            if tag['Key'] == 'Name' and tag['Value'] == instance_name:
                instance_exits = True
                instance_id = instance.id
                print(f"Instance {instance_id} already exists and is running.")
                break
        if instance_exits:
            break

# Check if the instance exists and is stopped
def check_instance_exists_and_stopped():
    global instance_id
    instances = ec2.instances.filter(Filters=[{'Name': 'tag:Name', 'Values': [instance_name]}])
    for instance in instances:
        if instance.state['Name'] in ['stopped']:
            instance_id = instance.id
            print(f"Instance {instance_id} already exists with state: {instance.state['Name']}.")
            break
         

# launch an instance if it does not exist
def launch_ec2_instance():
    global instance_id
    if not check_instance_exists():
        instance = ec2.create_instances(
            ImageId='ami-091a5ee0157d25e3f',  # Replace with a valid AMI ID
            MinCount=1,
            MaxCount=1,
            InstanceType='t3.micro',
            #KeyName='your-key-pair',  # Replace with your key pair name
            TagSpecifications=[{
                'ResourceType': 'instance',
                'Tags': [
                    {
                        'Key': 'Name', 
                        'Value': instance_name
                    }
                ]
            }]
        )
            
    instance_id = instance[0].id
    print(f"New instance with ID: {instance_id} has been launched successfully.")

# Stop the instance if it exists and is running
def stop_ec2_instance():
    global instance_id
    if instance_id:
        instance = ec2.Instance(instance_id)
        if instance.state['Name'] == 'running':
            instance.stop()
            print(f"Instance {instance_id} has been stopped.")
        else:
            print(f"Instance {instance_id} is not running.")
    else:
        print("No instance found to stop.")

# Start the instance if it exists and is stopped
def start_ec2_instance():
    global instance_id
    if check_instance_exists_and_stopped():
        instance = ec2.Instance(instance_id)
        if instance.state['Name'] == 'stopped':
            instance.start()
            print(f"Instance {instance_id} has been started.")
        else:
            print(f"Instance {instance_id} is already running.")

# Check if the instance exists and is running, otherwise launch a new instance
if __name__ == "__main__":
    # Create the EC2 instance if it does not exist
    if check_instance_exists_and_stopped():
        launch_ec2_instance()
    else:
        print(f"Instance already exists. Ready for management.")

    # Optionally, launch the instance if it does not exist
    #if not check_instance_exists():
    #    launch_ec2_instance()
    #else:
    #    print(f"Instance already exists. Ready for management.")

    # Optionally, you can stop the instance
    #stop_ec2_instance()
    

    # Optionally, you can start the instance
    #start_ec2_instance()