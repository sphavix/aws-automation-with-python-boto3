"""Create a dictionary of AWS services and modify the dictionary appropriately"""

def main():
    # Create a dictionary of AWs services and their descriptions
    aws_services = {
        'S3': "Simple Storage Service for object storage.",
        'Lambda': "Serverless compute services used to build serveless applications.",
        'DynamoDB': "Document storage using key value pairs."
    }
    # print the dictionary
    print(f"Simple dictionary of AWS services and descriptions.")
    print(aws_services)


    # Access the description of an item in the dictionary
    lambda_service = aws_services['Lambda']
    print(f"\nDescription of Lambda Service: {lambda_service}")

    # Modify the description of a service
    aws_services['Lambda'] = "Serverless compute AWS Service used to build serveless applications."
    print(f"\nUpdated description of Lambda Service: {aws_services}")

    # Add a new service and a description to the dictionary
    aws_services['SNS'] = "Simple Notification Service to send notifications"
    print(f"\nAdded a new service: {aws_services['SNS']}")

    #Remove the service from the dictionary
    del aws_services['Lambda']
    print(f"\nRemoved one of the services amongst {aws_services} from the dictionary")

    # Use the keys(), values(), and items() methods to display different aspects of the dictionary
    print(aws_services.keys())
    print(aws_services.values())
    print(aws_services.items())

    # Modify the dictionary to add a nested structure with addtional information
    aws_services['S3'] = {
        'description': "Simple Storage Service for object storage.",
        'launch_year': 2006
    }

    # print the modified dictionary with nested structure
    print(f"\nModified dictionary with nested structure: ")
    print(aws_services['S3'])


if __name__ == '__main__':
    main()
    

    