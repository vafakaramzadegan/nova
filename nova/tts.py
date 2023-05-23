from os import path
import hashlib
from io import BytesIO

from gtts import gTTS
from nova.audio import play, answer_notification_sound
from nova import Config


class TtsEngine:
    lang = ''
    req_lang = ''
    tld = ''

    def __init__(self, lang):
        super().__init__()
        self.req_lang = lang
        self.set_language()

    def set_language(self):
        lang_mapping = {
            'en_us': ('en', 'us'),
            'en_uk': ('en', 'co.uk'),
            'fr_fr': ('fr', 'fr'),
            'de_de': ('de', 'de'),
        }
        self.lang, self.tld = lang_mapping.get(
            self.req_lang.lower(), ('en', 'us'))

    def __generate_cache_filename(self, text):
        hash_object = hashlib.sha256(str.encode(text))
        hex_dig = hash_object.hexdigest()
        return path.join(Config.tmp_folder, self.req_lang, f'{hex_dig}.mp3')

    def __write_audio_to_cache(self, filename, tts_object):
        """ the tts generated audio will be converted to BytesIO, saved in the cache,
            and then returned for future use.

        Args:
            filename (str): _description_
            tts_object (gTTS): _description_

        Returns:
            BytesIO: _description_
        """
        mp3_fp = BytesIO()
        tts_object.write_to_fp(mp3_fp)
        mp3_fp.seek(0)

        with open(filename, 'wb') as f:
            f.write(mp3_fp.getbuffer())

        return mp3_fp

    def __get_audio_from_cache(self, filename):
        """ get audio from cache if exists

        Args:
            filename (str): cache filename

        Returns:
            BytesIO|bool: returns the file as BytesIO object if exists,
            otherwise returns false
        """
        if not path.isfile(filename):
            return False

        mp3_fp = BytesIO(open(filename, 'rb').read())
        mp3_fp.seek(0)

        return mp3_fp

    def prepare_to_say(self, text):
        """ convert text to audio in advance for later use or playback,
            especially when the response from Google TTS API may take some time.
            This can help avoid any potential delays.

        Args:
            text (str): text to be converted to audio
        """
        cache_filename = self.__generate_cache_filename(text)

        self.mp3_fp = self.__get_audio_from_cache(cache_filename)
        if self.mp3_fp == False:
            tts = gTTS(text=text, lang=self.lang, tld=self.tld, slow=False)
            self.mp3_fp = self.__write_audio_to_cache(cache_filename, tts)

    @answer_notification_sound
    def say_what_was_prepared(self):
        play(self.mp3_fp)

    @answer_notification_sound
    def say(self, text):
        self.prepare_to_say(text)
        play(self.mp3_fp)
