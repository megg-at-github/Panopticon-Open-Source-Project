# Welcome message and initial check
print('Welcome to Panopticon Sentinel Software')

# Placeholder for hostname and date
running = input("host[PLACEHOLDER]/[PLACEHOLDER]/[DATE] UTC/")

# Generic login prompt
notif = input("Enter Login Key")

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
    print(f'system: [PLACEHOLDER_OS], cpu: [PLACEHOLDER_CPU], storage: [PLACEHOLDER_STORAGE], ram: [PLACEHOLDER_RAM], no. of softcomp containing: [PLACEHOLDER_COMPONENT_COUNT] comp.')
else:
    print(f"[{PLACEHOLDER_HOSTNAME}]/[PLACEHOLDER_DATE] UTC/Error occured")

# Placeholder input for further instructions
notif = input("[PLACEHOLDER_INPUT_PROMPT]")

# Macro information extraction command and response
if running == "extrt macro info":
    print('entry pin: [PLACEHOLDER_PIN], Administrator: [PLACEHOLDER_ADMIN], progrunn: [PLACEHOLDER_PROGRAM_COUNT], programs on use: [PLACEHOLDER_PROGRAM_1]; [PLACEHOLDER_PROGRAM_2]')
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
    print(f'system: [PLACEHOLDER_OS], cpu: [PLACEHOLDER_CPU], storage: [PLACEHOLDER_STORAGE], ram: [PLACEHOLDER_RAM], no. of softcomp containing: [PLACEHOLDER_COMPONENT_COUNT] comp.')
else:
    print(f"[{PLACEHOLDER_HOSTNAME}]/[PLACEHOLDER_DATE] UTC/Error occured")

# Placeholder input for any additional instructions
notif = input("[PLACEHOLDER_INPUT_PROMPT]")

# Macro information extraction command and response
if running == "extrt macro info":
    print('entry pin: [PLACEHOLDER_PIN], Administrator: [PLACEHOLDER_ADMIN], progrunn: [PLACEHOLDER_PROGRAM_COUNT], programs on use: [PLACEHOLDER_PROGRAM_1]; [PLACEHOLDER_PROGRAM_2]')
else:
    print(f"[{PLACEHOLDER_HOSTNAME}]/[PLACEHOLDER_DATE] UTC/Error occured")
