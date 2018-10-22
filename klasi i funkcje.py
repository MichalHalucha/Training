class Time():
    """Czas"""

#przelicznik czasu
def int_to_time(seconds):
    time = Time()
    mintutes, time.second = divmod(seconds,60)
    time.hour,time.minute=divmod(mintutes,60)
    return time


