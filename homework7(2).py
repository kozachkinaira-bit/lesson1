import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename="error.log",
    format="%(asctime)s - %(levelname)s - %(message)s",
)

while True:
    try:
        a = int(input("Введіть перше число: "))
        b = int(input("Введіть друге число: "))
        count = a / b
        print(f"Result: {count}")
        break 

    except ValueError as e:
        print("Incorrect input data...")
        logging.error(f"Incorrect input data: {e}") 

    except ZeroDivisionError as zde:
        print("Not allowed operation...")
        logging.error(f"Not allowed operation: {zde}")  

logging.info("Program has stopped...")