# log.py

from typing import TypedDict, Unpack
from datetime import datetime

# Define a structured dictionary for access event logging using TypedDict (Python 3.12+)
class AccessEvent(TypedDict):
    user: str
    role: str
    action: str
    timestamp: str

def log_access_event(**kwargs: Unpack[AccessEvent]) -> None:
    """
    Log different types of access events with specific `**kwargs` types.
    """
    # Using advanced f-strings with multiline, nested expressions, and comments
    log_message = (
        f"User: {kwargs['user']}\n"
        f"Role: {kwargs['role'].upper()}\n"
        f"Action: {kwargs['action']}\n"
        f"Timestamp: {datetime.now().isoformat()}  # Current timestamp\n"
    )
    print(log_message)

# Example usage with inline unpacking
log_access_event(user="Alice", role="member", action="login", timestamp="2024-11-01T10:00:00")