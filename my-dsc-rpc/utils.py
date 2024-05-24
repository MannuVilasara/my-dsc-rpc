import subprocess
import sys
import psutil
import datetime


def get_system_uptime():
    # Get system uptime in seconds
    uptime_seconds = psutil.boot_time()

    # Convert uptime to a timedelta object
    uptime_timedelta = datetime.datetime.now() - datetime.datetime.fromtimestamp(
        uptime_seconds
    )

    return uptime_timedelta


def run_command(command):
    try:
        process = subprocess.Popen(
            command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True
        )
        output, error = process.communicate()

        output = output.decode("utf-8").strip()
        error = error.decode("utf-8").strip()

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
    return round(bytes / (1024 * 1024 * 1024), 1)


def get_memory_usage():
    mem = psutil.virtual_memory()
    total_memory = bytes_to_gigabytes(mem.total)
    used_memory = bytes_to_gigabytes(mem.used)
    memory_percent = mem.percent

    return {
        "total_memory": total_memory,
        "used_memory": used_memory,
        "memory_percent": memory_percent,
    }


def songinfo():
    status = "Playing"
    _is_playing = run_command("playerctl status")
    if _is_playing == "Stopped":
        return None
    if _is_playing == "Paused":
        status = "Paused"
    try:
        return {
                "status": status,
                "artist": run_command("playerctl metadata artist"),
                "title": run_command("playerctl metadata title"),
                "artUrl": run_command("playerctl metadata mpris:artUrl"),
                # "track": run_command("playerctl metadata xesam:url"),
                # 'duration': run_command("playerctl metadata --format '{{ duration(position) }}/{{ duration(mpris:length) }}'")
            }
    except:
        return {
            "status": status,
            "artist": run_command("playerctl metadata artist"),
            "title": run_command("playerctl metadata title"),
        }
