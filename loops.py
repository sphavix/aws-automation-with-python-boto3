"""Use a list of AWS services and loop through it"""
def main():
    # 1. Create a list of AWS services
    aws_services = ['S3', 'Lambda', 'DynamoDB', 'VPC', 'EKS']

    print(f"AWS Services list: {aws_services}")

    # use a for loop to iterate throught the list definately
    print("\nUsing a for loop to iterate the list")
    for service in aws_services:
        print(service)
    

    # 2. Use a while loop to iterate through the list in reverse order
    print("\nUsing a while loop to iterate through the list in reverse order")
    index = len(aws_services) -1
    while index >= 0:
        print(aws_services[index])
        index -= 1

    # 3. Use enumerate() with the for loop to get both index and value
    print("\nUsing enumerate() with a for loop to get the index and value")
    for index, service in enumerate(aws_services):
        print(f"Service # {index + 1}: {service}.")

if __name__ == '__main__':
    main()