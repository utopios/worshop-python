# session.py

from typing import Literal, Unpack, Self, override
from log import log_access_event

# Define user session roles for type checking
Role = Literal["member", "admin", "guest"]

# Base class for user sessions
class BaseUserSession:
    def __init__(self, user: str, role: Role) -> None:
        self.user = user
        self.role = role

    def log_session(self) -> None:
        """
        Log session details.
        """
        log_access_event(user=self.user, role=self.role, action="session_start", timestamp="2024-11-01T10:00:00")
        print(f"Session started for {self.user} as a {self.role}.")

# Derived class for admin sessions with @override decorator
class AdminSession(BaseUserSession):
    def __init__(self, user: str) -> None:
        super().__init__(user, "admin")

    @override  # Ensure that this method correctly overrides the base method (Python 3.12+)
    def log_session(self) -> None:
        """
        Log admin session details with additional privileges.
        """
        log_access_event(user=self.user, role=self.role, action="admin_session_start", timestamp="2024-11-01T10:00:00")
        print(f"Admin session started for {self.user}. Access granted to all resources.")

# Example usage
admin_session = AdminSession("Bob")
admin_session.log_session()