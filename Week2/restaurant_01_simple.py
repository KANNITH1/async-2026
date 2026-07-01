# Program: Restaurant Operation (Synchronous)
# Concept: Running tasks sequentially using standard time.sleep() blocking the main thread.
from time import sleep, ctime, time

# Greeting Sync function
def greet_diners(customer):
    print(f"{ctime()} Greeting for Customer-{customer} ...")
    sleep(1)
    print(f"{ctime()} Greeting for Customer-{customer} ...Done!")

# Take Order
def take_orders(customer):
    print(f"{ctime()} Taking Order for Customer-{customer} ...")
    sleep(1)
    print(f"{ctime()} Taking Order for Customer-{customer} ...Done!")

# Do Cooking
def do_cooking(customer):
    print(f"{ctime()} Cooking for Customer-{customer} ...")
    sleep(1)
    print(f"{ctime()} Cooking for Customer-{customer} ...Done!")

# Do cooking
def mini_bar(customer):
    print(f"{ctime()} Mini Bar for Customer-{customer} ...")
    sleep(1)
    print(f"{ctime()} Mini Bar for Customer-{customer} ...Done!")

if __name__ == "__main__":
    # จุดเริ่มต้นของ Main Thread
    customers = ['A', 'B', 'C']
    
    start_time = time()
    
    # ทำงานตามลำดับทีละคน ทีละขั้นตอน (Sequential)
    for customer in customers:
        greet_diners(customer)
        take_orders(customer)
        do_cooking(customer)
        mini_bar(customer)
        
    duration = time() - start_time
    print(f"{ctime()} Finished Cooking in {duration:.2f} seconds.")