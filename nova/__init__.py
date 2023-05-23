import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    # define folder paths
    data_folder = os.path.join(os.path.dirname(__file__), '..', 'data')
    tmp_folder = os.path.join(data_folder, 'tmp')
    audio_folder = os.path.join(data_folder, 'audio')
    dialog_dir = os.path.join(data_folder, 'dialogs')
    tasks_module_dir = os.path.join(os.path.dirname(__file__), 'task_modules')

    # get environment variables
    language = os.getenv('language')
    user_name = os.getenv('your_name')
    user_timezone = os.getenv('your_timezone')
    user_country = os.getenv('your_country')
    openai_api_key = os.getenv('openai_api_key')
    assistant_name = os.getenv('assistant_name').lower()
    assistant_trigger_phrase = os.getenv('assistant_trigger_phrase').lower()
    assistant_listen_timeout = os.getenv('assistant_listen_timeout')

    # set audio file paths
    assistant_start_listen_audio = os.path.join(audio_folder, 'open.wav')
    assistant_stop_listen_audio = os.path.join(audio_folder, 'close.wav')
    assistant_busy_audio = os.path.join(audio_folder, 'busy.wav')
