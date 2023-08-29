from cx_Freeze import setup, Executable

# Specify your main script (Python file)
main_script = "decryption.py"

# Create an executable
executables = [Executable(main_script)]

# Define other options
options = {
    "build_exe": {
        "includes": ["PIL"],  # Add other modules here
    }
}

# Setup
setup(
    name="DecryptionApp",
    version="1.0",
    description="Decryption Application",
    executables=executables,
    options=options
)
