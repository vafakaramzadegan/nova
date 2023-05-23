import speech_recognition as sr
from nova.tts import TtsEngine
from nova.dialog import DialogList
from nova import Config
from nova.audio import play
from nova.openai import OpenAi
import time


class SrEngine:
    listening = False

    def __init__(self, tts_engine: TtsEngine):
        self.openai = OpenAi()
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

        # Adjust for ambient noise to improve accuracy
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=0.2)

        self.tts_engine = tts_engine

    def __listen(self, recognizer, audio):
        try:
            # Convert audio to text and make lowercase for consistency
            command_transcript = recognizer.recognize_google(audio).lower()
            print('You probably said:', command_transcript)

            # Handle assistant trigger phrase
            if command_transcript == Config.assistant_trigger_phrase:
                command_transcript = ''
                self.tts_engine.say(DialogList.get_random_greeting())
                self.listening = True

            # Handle command input
            if self.listening:
                if command_transcript != '':
                    # Play audio to indicate the assistant is processing the command
                    play(Config.assistant_busy_audio)

                    # Use OpenAI to generate a response to the command and speak the response
                    self.tts_engine.say(self.openai.query(command_transcript))
                    self.listening = False

                    # Play audio to indicate the assistant has stopped listening
                    play(Config.assistant_stop_listen_audio)

        except sr.RequestError as e:
            print('Could not request results: {0}'.format(e))

        except sr.UnknownValueError:
            # Ignore unknown value errors for now
            print('')

    def start_polling(self):
        # Start the recognizer in the background to listen for commands
        self.recognizer.listen_in_background(self.microphone, self.__listen)

        # Keep the program running indefinitely
        while True:
            time.sleep(0.2)
