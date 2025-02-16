import random
import string

def generate_random_name(user_name, department):
    first_names = ["John", "Jane", "Alex", "Emily", "Chris", "Katie", "Michael", "Sarah", "David", "Laura"]
    last_names = ["Smith", "Johnson", "Brown", "Taylor", "Anderson", "Thomas", "Jackson", "White", "Harris", "Martin"]
    
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    random_number = ''.join(random.choices(string.digits, k=4))
    random_chars = ''.join(random.choices(string.ascii_letters, k=2))
    
    return f"{user_name} - {first_name} {last_name} - {department} - {random_chars}{random_number}"

if __name__ == "__main__":
    user_name = input("Enter your name: ")
    department = input("Enter the department name: ")
    num_instances = int(input("Enter the number of EC2 instances: "))
    for _ in range(num_instances):  # Generate and print the specified number of random names
        print(generate_random_name(user_name, department))