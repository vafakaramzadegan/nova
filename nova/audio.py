from pydub import AudioSegment
from pydub.playback import play as pydub_play
from io import BytesIO
from nova import Config


def play(data: str | BytesIO) -> None:
    audio = AudioSegment.from_file(data, format='mp3')
    pydub_play(audio)


def answer_notification_sound(func) -> any:
    def wrapper(*args, **kwargs):
        play(Config.assistant_start_listen_audio)
        func(*args, **kwargs)

    return wrapper
