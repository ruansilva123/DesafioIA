import azure.cognitiveservices.speech as speechsdk
import wave

SPEECH_API_KEY = "<YOUR_API_KEY>"
SPEECH_REGION = "eastus"

transcricao = ""

def transcribed_handler(event):
    global transcricao
    print(f"TRANSCRIBED: Text={event.result.text} Speaker ID={event.result.speaker_id}")
    transcricao += event.result.text

# Função de callback para quando a sessão for parada
def session_stopped_handler(event):
    print("Transcription session stopped.")
    print("Transcrição finalizada:", transcricao)

# Função de callback para quando houver erro
def canceled_handler(event):
    print(f"Transcription canceled: {event.error_details}")

def transcribe_audio_from_file(wav_file, language='pt-BR'):
    # Configuração do serviço de fala
    speech_config = speechsdk.SpeechConfig(subscription=SPEECH_API_KEY, region=SPEECH_REGION)
    speech_config.speech_recognition_language = language

    # Configuração de áudio para entrada WAV
    audio_config = speechsdk.audio.AudioConfig(filename=wav_file)

    # Criação do transcritor de conversação
    conversation_transcriber = speechsdk.ConversationTranscriber(speech_config, audio_config)

    # Associar as funções de callback aos eventos
    conversation_transcriber.transcribed.connect(transcribed_handler)
    conversation_transcriber.session_stopped.connect(session_stopped_handler)
    conversation_transcriber.canceled.connect(canceled_handler)

    # Iniciar a transcrição
    print(f"Transcribing from: {wav_file}")
    conversation_transcriber.start_transcribing_async()

    return transcricao

if __name__ == "__main__":
    wave_path = "../../../docs/amanda-1.mp3"
    transcricao = transcribe_audio_from_file(wave_path)