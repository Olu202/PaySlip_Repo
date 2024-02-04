import random

def generate_workers(num_workers):
    """
    Generates a list of workers with random names, salaries, and genders.

    Args:
        num_workers (int): The number of workers to generate.

    Returns:
        list: A list of dictionaries, where each dictionary represents a worker.
    """
    workers = []
    for _ in range(num_workers):
        name = f"NXU Staff {random.randint(1, 503)}"
        salary = random.randint(5000, 35000)
        gender = random.choice(["Male", "Female"])
        worker = {"name": name, "salary": salary, "gender": gender}
        workers.append(worker)
    return workers

def generate_payment_slips(workers):
    """
    Generates payment slips for each worker in the list.

    Args:
        workers (list): A list of dictionaries, where each dictionary represents a worker.

    Returns:
        list: A list of strings, where each string represents a payment slip.
    """
    payment_slips = []
    for worker in workers:
        try:
            name = worker["name"]
            salary = worker["salary"]
            gender = worker["gender"]
            if salary > 10000 and salary < 20000:
                employee_level = "A1"
            elif salary > 7500 and salary < 30000 and gender == "Female":
                employee_level = "A5-F"
            else:
                employee_level = "No Level"
            payment_slip = f"Name: {name}, Salary: ${salary:.2f}, Employee Level: {employee_level}"
            payment_slips.append(payment_slip)
        except KeyError as e:
            print(f"Error processing worker: {worker}. Missing key: {e}")
    return payment_slips

if __name__ == "__main__":
    num_workers = 400
    workers = generate_workers(num_workers)
    payment_slips = generate_payment_slips(workers)
    for slip in payment_slips:
        print(slip)
