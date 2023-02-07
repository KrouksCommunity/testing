import hashlib

def hash_string(input_string):
    m = hashlib.md5()
    m.update(input_string.encode())
    return m.hexdigest()

def brute_force_hash(charset, max_length, target_hash):
    for length in range(1, max_length + 1):
        for combination in generate_combinations(charset, length):
            hashed_combination = hash_string(combination)
            if hashed_combination == target_hash:
                return combination
    return None

def generate_combinations(charset, length):
    if length == 1:
        for char in charset:
            yield char
    else:
        for char in charset:
            for tail in generate_combinations(charset, length - 1):
                yield char + tail

# Define the character set to use for the brute force
charset = "abcdefghijklmnopqrstuvwxyz0123456789"
# Define the maximum length of the combinations to generate
max_length = 5
# Define the target hash to reverse
target_hash = "d8578edf8458ce06fbc5bb76a58c5ca4"

result = brute_force_hash(charset, max_length, target_hash)

if result:
    print("The original string is:", result)
else:
    print("No combination found.")
