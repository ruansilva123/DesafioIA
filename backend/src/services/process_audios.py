import azure.cognitiveservices.speech as speechsdk
import wave
import ffmpeg
import os
import decouple
from decouple import config

SPEECH_API_KEY = config('SPEECH_API_KEY')
SPEECH_REGION = "eastus"

transcricao = ""

def convert_to_wav(input_file, output_file=None):
    """
    Converte um arquivo de vídeo MP3 ou MP4 para o formato WAV.
    """

    ffmpeg_path = r'../../docs/ffmpeg/bin/ffmpeg.exe'

    if not os.path.exists(input_file):
        raise FileNotFoundError(f"O arquivo de entrada '{input_file}' não foi encontrado.")

    if output_file is None:
        output_file = os.path.splitext(input_file)[0] + ".wav"

    try:
        ffmpeg.input(input_file).output(output_file, format='wav').run(overwrite_output=True)
        return output_file
    except Exception as e:
        print(f"Ocorreu um erro ao tentar converter o arquivo: {e}")
        raise


def transcribed_handler(event):
    global transcricao
    print(f"TRANSCRIBED: Text={event.result.text} Speaker ID={event.result.speaker_id}")
    transcricao += event.result.text


def session_stopped_handler(event):
    """ Função de callback para quando a sessão for parada """
    print("Transcription session stopped.")
    print("Transcrição finalizada:", transcricao)


def canceled_handler(event):
    """ Função de callback para quando houver erro """
    print(f"Transcription canceled: {event.error_details}")


def transcribe_audio_from_file(wav_file, language='pt-BR'):
    """ Transcrição do arquivo de áudio para arquivo de  """

    speech_config = speechsdk.SpeechConfig(subscription=SPEECH_API_KEY, region=SPEECH_REGION)
    speech_config.speech_recognition_language = language

    audio_config = speechsdk.audio.AudioConfig(filename=wav_file)

    speech_recognizer = speechsdk.SpeechRecognizer(speech_config, audio_config)

    speech_recognizer.recognized.connect(transcribed_handler)
    speech_recognizer.session_stopped.connect(session_stopped_handler)
    speech_recognizer.canceled.connect(canceled_handler)

    speech_recognizer.start_continuous_recognition_async()

    return transcricao

if __name__ == "__main__":
    file_path = "../../docs/amanda-1.mp3"
    wave_file = "../../docs/amanda-1.wav"
    convert_to_wav(file_path, wave_file)
    transcricao = transcribe_audio_from_file(wave_file)