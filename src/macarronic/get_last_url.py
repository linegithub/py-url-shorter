# Initial ID offset set for obfuscation.
first_id = 1000000000
current_id = 1000000000

# TODO: Implement a reliable, persistent, and atomic mechanism (DB sequence, Redis, etc.)
# to manage the current ID counter across application restarts and concurrent requests.

def get_last_id():
    global current_id
    current_id = current_id +1
    return current_id