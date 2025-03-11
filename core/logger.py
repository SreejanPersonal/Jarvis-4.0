import os
import logging
from logging.handlers import RotatingFileHandler
from typing import Optional

# Create logs directory if it doesn't exist
log_dir = os.path.join(os.getcwd(), "data", "logs")
os.makedirs(log_dir, exist_ok=True)

# Configure logging
LOG_FILE = os.path.join(log_dir, "jarvis.log")
print(f"Log directory: {log_dir}")  # Print log directory path
print(f"Log file path: {LOG_FILE}")  # Print log file path
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOG_LEVEL = logging.INFO

# Configure the root logger
try:
    logging.basicConfig(
        level=LOG_LEVEL,
        format=LOG_FORMAT,
        handlers=[
            RotatingFileHandler(LOG_FILE, maxBytes=10485760, backupCount=5),  # 10MB max file size
            logging.StreamHandler()  # Also log to console
        ]
    )
except Exception as e:
    print(f"Error configuring logger: {e}")

def get_logger(name: Optional[str] = None) -> logging.Logger:
    """
    Get a logger configured with the standard settings.
    
    Args:
        name (str, optional): Name for the logger, usually __name__.
        
    Returns:
        logging.Logger: Configured logger instance.
    """
    return logging.getLogger(name)
