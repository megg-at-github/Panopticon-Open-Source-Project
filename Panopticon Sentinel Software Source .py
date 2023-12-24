# Welcome message and initial check
print('Welcome to Panopticon Sentinel Software')

# Placeholder for hostname and date
running = input("host[PLACEHOLDER]/[PLACEHOLDER]/[DATE] UTC/")

# Generic login prompt
import password 
# Minimum length
min_length = 10

# Required character classes
required_classes = {
    "uppercase": True,
    "lowercase": True,
    "number": True,
    "symbol": True,
}

notif = input("Enter Login Key")

if not password.check(login_key, min_length, required_classes):
    print("Login key does not meet complexity requirements.")
    print("Please ensure your password has:")
    print(f"- At least {min_length} characters")
    print("- One uppercase letter")
    print("- One lowercase letter")
    print("- One number")
    print("- One symbol")
    quit()

import bcrypt

# Generate salt
salt = bcrypt.gensalt()

# Hash password
password = "[PLACEHOLDER_PASSWORD]".encode('utf-8')
hashed_password = bcrypt.hashpw(password, salt)

# Verify password
if bcrypt.checkpw(password, hashed_password):
    print("Password matched")
else:
    print("Password did not match.")

# Access granted/denied logic with a placeholder password
if running == "[PLACEHOLDER_PASSWORD]":
    print('Access Granted')
else:
    print(f"[{PLACEHOLDER_HOSTNAME}]/[PLACEHOLDER_DATE] UTC/Access Denied")

# Ensure connection to specific server
if running != "[PLACEHOLDER_SERVER_NAME]":
    quit()

print("Running system...")

# Placeholder input for machine confirmation
notif = input("machine found: [PLACEHOLDER_SERVER_NAME]")

# System information extraction command and response
if running == "extrt machine info":
    print(f'system: [PLACEHOLDER_OS], cpu: [PLACEHOLDER_CPU], storage: [PLACEHOLDER_STORAGE], ram: [PLACEHOLDER_RAM], no. of softcomp containing: [PLACEHOLDER_COMPONENT_COUNT] comp., average cpu performance: [PLACEHOLDER_CPU_PERFORMANCE]')
else:
    print(f"[{PLACEHOLDER_HOSTNAME}]/[PLACEHOLDER_DATE] UTC/Error occured")

# Placeholder input for further instructions
notif = input("[PLACEHOLDER_INPUT_PROMPT]")

# Macro information extraction command and response
if running == "extrt macro info":
    print('entry pin: [PLACEHOLDER_PIN], Administrator: [PLACEHOLDER_ADMIN], programs on use: [PLACEHOLDER_PROGRAM_1]; [PLACEHOLDER_PROGRAM_2]')
else:
    print(f"[{PLACEHOLDER_HOSTNAME}]/[PLACEHOLDER_DATE] UTC/Error occured")

# Repeat server check and login prompt
if running != "[PLACEHOLDER_SECOND_SERVER_NAME]":
    quit()

notif = input("Enter Login Key")

# Access granted/denied logic with a second placeholder password
if running == "[PLACEHOLDER_SECOND_PASSWORD]":
    print('Access Granted')
else:
    print(f"[{PLACEHOLDER_HOSTNAME}]/[PLACEHOLDER_DATE] UTC/Access Denied")

print("Running system...")

# Placeholder input for second machine confirmation
notif = input("machine found: [PLACEHOLDER_SECOND_SERVER_NAME]")

# System information extraction command and response
if running == "extrt machine info":
    print(f'system: [PLACEHOLDER_OS], cpu: [PLACEHOLDER_CPU], storage: [PLACEHOLDER_STORAGE], ram: [PLACEHOLDER_RAM], no. of softcomp containing: [PLACEHOLDER_COMPONENT_COUNT] comp. average cpu performance: [PLACEHOLDER_CPU_PERFORMANCE]')
else:
    print(f"[{PLACEHOLDER_HOSTNAME}]/[PLACEHOLDER_DATE] UTC/Error occured")

# Placeholder input for any additional instructions
notif = input("[PLACEHOLDER_INPUT_PROMPT]")

# Macro information extraction command and response
if running == "extrt macro info":
    print('entry pin: [PLACEHOLDER_PIN], Administrator: [PLACEHOLDER_ADMIN], programs on use: [PLACEHOLDER_PROGRAM_1]; [PLACEHOLDER_PROGRAM_2]')
else:
    print(f"[{PLACEHOLDER_HOSTNAME}]/[PLACEHOLDER_DATE] UTC/Error occured")

    
