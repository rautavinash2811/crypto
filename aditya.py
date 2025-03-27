import sys

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Main program without functions

# Accept the prime number
while True:
    prime_input = input("Provide a valid prime number: ")
    
    # Check if the input is a valid number
    if prime_input.isdigit():
        prime_value = int(prime_input)
        
        # Check if the number is a prime
        if is_prime(prime_value):
            break
        else:
            print(f"{prime_value} is not a prime number. Please enter a valid prime number.")
    else:
        print("Input is not valid. Please enter a valid number for the prime number.")

# Accept the primitive root
while True:
    root_input = input("Provide a valid primitive root: ")
    
    # Check if the input is a valid number
    if root_input.isdigit():
        root_value = int(root_input)
        
        # Check if the primitive root is smaller than the prime number
        if root_value < prime_value:
            break
        else:
            print("Primitive root cannot be equal to or larger than the prime number. Please try again.")
    else:
        print("Input is not valid. Please enter a valid number.")

# Check if the given root_value is a primitive root
generated_values = []
for i in range(1, prime_value):
    result = (root_value ** i) % prime_value
    if result in generated_values:
        print(f"{root_value} is not a primitive root of {prime_value}.")
        break
    else:
        generated_values.append(result)

print("Generated values by the primitive root are:")
print(generated_values)

# Find all primitive roots (excluding 1)
primitive_roots = []
for j in range(2, prime_value):  # Start from 2 to avoid 1 being added
    generated_values_check = []
    for i in range(1, prime_value):
        result = (j ** i) % prime_value
        if result in generated_values_check:
            break
        else:
            generated_values_check.append(result)
    if len(generated_values_check) == prime_value - 1:
        primitive_roots.append(j)

print(f"Primitive roots of {prime_value}:")
print(primitive_roots)
print(f"Total number of primitive roots of {prime_value}: {len(primitive_roots)}")

# Encryption part
print("Start of Encryption")
print(f"Prime number p is {prime_value}")

# Ensure that 'g' is a valid primitive root from the list (not 1)
g_value = primitive_roots[0]
print(f"Generator g is {g_value}")

# Accept the secret key 'a'
while True:
    a_input = input("Provide the secret key 'a': ")
    
    # Check if the input is a valid number
    if a_input.isdigit():
        secret_key = int(a_input)
        
        # Ensure the secret key is between 1 and the prime number
        if secret_key < prime_value and secret_key > 1:
            break
        else:
            print("Invalid value for 'a'. Please ensure it's between 1 and the prime number.")
    else:
        print("Input is not valid. Please enter a valid number.")

A_value = (g_value ** secret_key) % prime_value
print(f"Calculated value of A is {A_value}")

# Accept the value of k
while True:
    k_input = input("Provide the value of K: ")
    
    # Check if the input is a valid number
    if k_input.isdigit():
        k_value = int(k_input)
        break
    else:
        print("Input is not valid. Please enter a valid number.")

c1_value = (g_value ** k_value) % prime_value

# Accept plain text
while True:
    pt_input = input("Provide the plain text: ")
    
    # Check if the input is a valid number
    if pt_input.isdigit():
        plain_text = int(pt_input)
        break
    else:
        print("Input is not valid. Please enter a valid number.")

c2_value = ((plain_text * (A_value ** k_value)) % prime_value)
print(f"The values of c1 and c2 are {c1_value} and {c2_value}")

# Decryption part
print("Start of Decryption")
print("Converting cipher text back to plain text:")

inverse_value = 0
for i in range(1, prime_value):
    k = (c1_value ** secret_key * i) % prime_value
    if k == 1:
        inverse_value = i
        break
print(f"The inverse value is {inverse_value}")

decrypted_text = ((c2_value * inverse_value) % prime_value)
print(f"The original plain text is {decrypted_text}")
