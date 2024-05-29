import asyncio
import psutil
import datetime

from winrt.windows.media.control import \
    GlobalSystemMediaTransportControlsSessionManager as MediaManager




def get_system_uptime():
    uptime_seconds = psutil.boot_time()

    uptime_timedelta = datetime.datetime.now() - datetime.datetime.fromtimestamp(
        uptime_seconds
    )

    return uptime_timedelta


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


async def get_media_info():
    sessions = await MediaManager.request_async()
    current_session = sessions.get_current_session()

    if current_session:
        if current_session.source_app_user_model_id:
            info = await current_session.try_get_media_properties_async()
            info_dict = {song_attr: info.__getattribute__(song_attr) for song_attr in dir(info) if song_attr[0] != '_'}

            info_dict['genres'] = list(info_dict['genres'])

            return info_dict

    raise Exception('TARGET_PROGRAM is not the current media session')



def songinfo():
    current_media_info = asyncio.run(get_media_info())
    status = "Playing"
    return {
            "status": status,
            "artist":  current_media_info["artist"],
            "title": current_media_info["title"]
        }
