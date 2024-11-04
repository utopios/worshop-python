# 1. Structural Pattern Matching with `match` and `case`
def describe(value):
    """
    Function to describe an object using pattern matching.
    """
    match value:
        case {'type': 'fruit', 'name': str(name)}:
            return f"This is a {name}."
        case {'type': 'veggie', 'name': str(name)}:
            return f"This is a {name}, which is a vegetable."
        case _:
            return "Unknown object"

# Usage examples
print(describe({'type': 'fruit', 'name': 'apple'}))  # Output: This is a apple.
print(describe({'type': 'veggie', 'name': 'carrot'}))  # Output: This is a carrot, which is a vegetable.
print(describe({'type': 'unknown'}))  # Output: Unknown object


def user_greeting(profile):
    """
    Function to return a customized greeting based on user profile.
    """
    match profile:
        case {'name': str(name), 'age': int(age)} if age >= 18:
            return f"Welcome, {name}! You are an adult."
        case {'name': str(name), 'age': int(age)}:
            return f"Hello, {name}! You are under 18."
        case {'name': str(name)}:
            return f"Welcome, {name}! Your age is not specified."
        case _:
            return "Unknown profile format"

def match_age(age:int) -> str:
    match age:
        case age if age >= 18:
            return "majeur"
        case _:
            return "mineur"

def mois(mois_int:int) -> str:
    match mois_int:
        case 1:
            return "Janvier"
        ### ....
        case _:
            return "Erreur mois"

# Usage examples
print(user_greeting({'name': 'Alice', 'age': "test"}))
print(user_greeting({'name': 'Bob', 'age': 17}))
print(user_greeting({'name': 'Charlie'}))
print(user_greeting({'username': 'Dave'}))

def greet(name: str | None) -> str:
    """
    Function that returns a greeting message.
    """
    return f"Hello, {name or 'guest'}"

print(greet("Ihab"))
print(greet(None))

# 3. New `connect_accepted_socket()` method in asyncio
import asyncio
import socket

async def handle_connection(reader, writer):
    """
    Asynchronous function to handle a network connection.
    """
    data = await reader.read(1024)
    print(data)
    writer.close()

async def main():
    """
    Asynchronous server using `connect_accepted_socket`.
    """
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.bind(('localhost', 8082))
    server_sock.listen()
    loop = asyncio.get_running_loop()
    
    while True:
        client_sock, addr = server_sock.accept()
        reader, writer = await asyncio.connect_accepted_socket(loop, client_sock)
        loop.create_task(handle_connection(reader, writer))

asyncio.run(main())  