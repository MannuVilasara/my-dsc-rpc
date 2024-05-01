from pypresence import Presence
import subprocess
import sys
import psutil

def run_command(command):
    try:
        # Run the command
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = process.communicate()

        # Decode output
        output = output.decode('utf-8').strip()
        error = error.decode('utf-8').strip()

        # Check for errors
        if process.returncode != 0:
            print(f"Error executing command '{command}': {error}", file=sys.stderr)
            return None
        else:
            return output
    except Exception as e:
        print(f"An error occurred: {str(e)}", file=sys.stderr)
        return None
    
def get_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    return cpu_usage

def bytes_to_gigabytes(bytes):
    return bytes / (1024 * 1024 * 1024)

def get_memory_usage():
    # Get memory usage statistics
    mem = psutil.virtual_memory()

    # Total physical memory (RAM) in gigabytes
    total_memory = bytes_to_gigabytes(mem.total)
    # Available physical memory (RAM) in gigabytes
    available_memory = bytes_to_gigabytes(mem.available)
    # Used physical memory (RAM) in gigabytes
    used_memory = bytes_to_gigabytes(mem.used)
    # Percentage of used memory
    memory_percent = mem.percent

    return {
        'total_memory': total_memory,
        'available_memory': available_memory,
        'used_memory': used_memory,
        'memory_percent': memory_percent
    }