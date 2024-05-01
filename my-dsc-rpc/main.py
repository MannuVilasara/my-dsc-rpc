from pypresence import Presence
from time import sleep, time
from utils import get_memory_usage, get_cpu_usage, songinfo, get_system_uptime
from colorama import Fore, Style

presence = Presence("1235105826016858143")
presence.connect()

while True:
    info = songinfo()
    details = f"▶️ {info['artist']} - {info['title']}"
    if info["status"] == "Paused":
        details = f"⏸️ {info['artist']} - {info['title']}"
    large_text = f"Playing {info['artist']} - {info['title']} "
    if info["status"] == "Paused":
        large_text = f"Paused at {info['artist']} - {info['title']}"
    presence.update(
        state=f"💻 CPU {get_cpu_usage()}%, RAM {get_memory_usage()['used_memory']}/{get_memory_usage()['total_memory']} GB | {get_memory_usage()["memory_percent"]}% used",
        details=details,
        large_image=info["artUrl"],
        large_text=large_text,
        small_image="https://avatars.githubusercontent.com/u/107882187?s=200&v=4",
        small_text=f"Hyprland | the current song is {info['title']} by {info['artist']}. My laptop has been up for {str(get_system_uptime())[0]}hr and {str(get_system_uptime())[2:4]}min",
        start=int(time()),
        buttons=[{"label": "Install Arch", "url": "https://archlinux.org"}],
    )
    print(
        f"=> {Fore.MAGENTA}INFO:{Style.RESET_ALL} {Fore.CYAN}[ARCH-LINUX]{Style.RESET_ALL} (archbtw)| Uptime: {get_system_uptime()}, {Fore.RED}CPU: {get_cpu_usage()}%{Style.RESET_ALL}, {get_memory_usage()['memory_percent']}% mem used."
    )
    sleep(15)
