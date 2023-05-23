from nova.tts import TtsEngine
from nova.speech_recognition import SrEngine
from nova import Config


tts_engine = TtsEngine(Config.language)

sr_engine = SrEngine(tts_engine)
sr_engine.start_polling()
