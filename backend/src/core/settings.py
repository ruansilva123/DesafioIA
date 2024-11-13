from decouple import config


""" Project Configs """

FILES_PATH = ".\\files"


""" API Keys """

GEMINI_KEY = config('GEMINI_KEY')
# GOOGLE_CLOUD_SPEECH = config('GOOGLE_CLOUD_SPEECH')
# API_KEY_OPENAI=config('API_KEY_OPENAI')
SPEECH_API_KEY=config('SPEECH_API_KEY')