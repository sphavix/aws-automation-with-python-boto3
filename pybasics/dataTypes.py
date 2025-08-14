
def main():
    # String (str)
    instance_type = 't2.micro'
    message = "My EC2 instances are of type: "

    # Integer (int)
    number_of_instances = 5
    hours_running = 10

    print(f"{message} {instance_type}. I have {number_of_instances} of them and they have been running for {hours_running} hours.")

    # Boolean (bool)
    instances_running = True
    print(f"Are all my instances running and healthy? {instances_running}.")
    print(f"My variable is of type: {type(instances_running)}.")


    # Floating-point number (float)
    instances_cost_per_hour = 1.50 #USD
    print(f"The price of running them per instance per hour is {instances_cost_per_hour} USD")


if __name__ == '__main__':
    main()