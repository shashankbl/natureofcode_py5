# main.py
import logging
# Create logger
logger = logging.getLogger('prologger')
logger.setLevel(logging.DEBUG)

# Create file handler
file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.DEBUG)

# Create console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

def main():
    print(f"Hello World!")
    logger.info("Executing main.py")

if __name__ == "__main__":
    main()