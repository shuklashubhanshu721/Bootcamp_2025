import logging

def setup_logging():
    """Configure global application logging."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
    )
    logger = logging.getLogger("bootcamp_2025")
    return logger

logger = setup_logging()

def response_formatter(data=None, message="Success", status=True):
    """Standard API response format."""
    return {
        "status": status,
        "message": message,
        "data": data or {}
    }