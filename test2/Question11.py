class Logger:
    def log(self, message, message_type = "info"):
        if message_type == "error":
            print(f"ERROR : {message}")
        elif message_type == "warning":
            print(f"WARNING : {message}")
        else:
            print(f"INFO : {message}")

def main():
    logger = Logger()
    logger.log("Starting Application") # info message
    logger.log("Index out of bounds", "error")
    logger.log("Low Disk Space", "warning")
main()
