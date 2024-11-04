import asyncio
from typing import Self, Union
import socket

# Step 1 & 2: Exception Notes and Exception Groups

def validate_user_access(user_profile: dict | None) -> str:
    """
    Validates user access based on role and subscription status.
    Returns an access message depending on the user profile structure.
    """
    if user_profile is None:
        raise ValueError("User profile is missing.")

    exceptions = []
    if "role" not in user_profile:
        e = ValueError("Missing 'role' in user profile.")
        e.add_note("The field 'role' is required for access validation.")
        exceptions.append(e)
    if "name" not in user_profile:
        e = ValueError("Missing 'name' in user profile.")
        e.add_note("The field 'name' is required for access validation.")
        exceptions.append(e)

    if exceptions:
        raise ExceptionGroup("Validation errors occurred", exceptions)
    
    # Use structured pattern matching for role-based access
    match user_profile:
        case {"role": "admin", "name": str(name)}:
            return f"Access granted to all resources for Admin {name}."
        case {"role": "member", "name": str(name), "subscription_status": "active"}:
            return f"Access granted to member resources for {name}."
        case {"role": "member", "name": str(name), "subscription_status": "inactive"}:
            return f"Limited access: {name}, please renew your subscription."
        case {"role": "guest", "name": str(name)}:
            return f"View-only access granted for Guest {name}."
        case _:
            return "Access denied: unknown role"

# Step 3: UserSession Class with Self Typing

class UserSession:
    def __init__(self, user_profile: dict):
        self.user_profile = user_profile

    def start_session(self) -> Self:
        print(f"Starting session for {self.user_profile.get('name', 'Unknown')}")
        return self

    def end_session(self) -> Self:
        print(f"Ending session for {self.user_profile.get('name', 'Unknown')}")
        return self

# Step 5: Async Task Groups for Concurrent Connections

async def process_access_request(reader, writer):
    """
    Processes an access request from a client. Reads the user profile,
    validates access, and sends back a response based on the profile data.
    """
    data = await reader.read(1024)
    user_profile = eval(data.decode())  # Assume data is received as a dictionary (for simplicity)
    
    try:
        # Validate user access based on the profile data
        response = validate_user_access(user_profile)
    except ExceptionGroup as eg:
        # Handle multiple validation errors
        response = "Validation errors occurred:\n" + "\n".join(str(e) for e in eg.exceptions)
    
    # Send the access response back to the client
    writer.write(response.encode())
    await writer.drain()
    writer.close()

async def start_access_server():
    """
    Starts an asynchronous server to handle incoming access requests using TaskGroup.
    """
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.bind(('localhost', 8080))
    server_sock.listen()
    server_sock.setblocking(False)

    loop = asyncio.get_running_loop()
    print("Server running on localhost:8080...")

    async with asyncio.TaskGroup() as tg:
        while True:
            client_sock, _ = await loop.sock_accept(server_sock)
            reader, writer = await asyncio.open_connection(sock=client_sock)
            tg.create_task(process_access_request(reader, writer))

# Uncomment to run the server
asyncio.run(start_access_server())