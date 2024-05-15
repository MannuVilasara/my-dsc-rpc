from pypresence import Presence
from time import sleep
from utils import get_memory_usage, get_cpu_usage, songinfo, get_system_uptime
from colorama import Fore, Style

presence = Presence("1235105826016858143")
presence.connect()

while True:
    mem_usage = get_memory_usage()
    uptime = str(get_system_uptime())
    cpu = get_cpu_usage()
    info = songinfo()
    big_img = info["artUrl"]
    if info["status"] == "Stopped":
        big_img = "https://github.com/MannuVilasara/Minimal-Fetch/blob/main/logos/arch/logo-big.png?raw=true"
    details = f"▶️ {info['title']}"
    if info["status"] == "Paused":
        details = f"⏸️ {info['title']}"
    large_text = f"Playing {info['artist']} - {info['title']} "
    if info["status"] == "Paused":
        large_text = f"Paused at {info['artist']} - {info['title']}"
    hours = uptime[0]
    minutes = uptime[2:4]
    if minutes[0] == ":":
        minutes = uptime[3:5]
        hours = uptime[0:2]
    presence.update(
        state=f"💻 CPU {cpu}%, RAM {mem_usage['used_memory']}/{mem_usage['total_memory']} GB | {mem_usage["memory_percent"]}% used",
        details=details,
        large_image=big_img,
        large_text=large_text,
        small_image="https://avatars.githubusercontent.com/u/107882187?s=200&v=4",
        small_text=f"Hyprland | the current song is {info['title']} by {info['artist']}. My laptop has been up for {hours}hr and {minutes}min",
        buttons=[{"label": "Install Arch", "url": "https://archlinux.org"},{"label": "Github", "url": "https://github.com/MannuVilasara"}],
    )
    print(
        f"=> {Fore.MAGENTA}INFO:{Style.RESET_ALL} {Fore.CYAN}[ARCH-LINUX]{Style.RESET_ALL} (archbtw)| Uptime: {uptime}, {Fore.RED}CPU: {cpu}%{Style.RESET_ALL}, {mem_usage['memory_percent']}% mem used."
    )
    sleep(15)
