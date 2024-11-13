const fs = require('fs');
const { SpeechConfig, AudioConfig, ConversationTranscriber, AudioInputStream } = require("microsoft-cognitiveservices-speech-sdk");

const SPEECH_API_KEY = "a4e4f56892dd4c78bd760a1f3f316c8d";
const SPEECH_REGION = "eastus";

class TranscriptionService {

    async transcribeAudioFromFile(wavFile, language = 'pt-BR') {
        return new Promise((resolve, reject) => {

            let transcricao = "";
            const speechConfig = SpeechConfig.fromSubscription(SPEECH_API_KEY, SPEECH_REGION);
            speechConfig.speechRecognitionLanguage = language;

            const audioInput = AudioConfig.fromWavFileInput(fs.readFileSync(wavFile.path));

            let conversationTranscriber = new ConversationTranscriber(speechConfig, audioInput);
            var pushStream = AudioInputStream.createPushStream();

            fs.createReadStream(wavFile.path).on('data', function (arrayBuffer) {
                pushStream.write(arrayBuffer.slice());
            }).on('end', function () {
                pushStream.close();
            });

            console.log("Transcribing from: " + wavFile.filename);

            conversationTranscriber.sessionStopped = function (s, e) {
                resolve(transcricao);
            };
            conversationTranscriber.canceled = function (s, e) {
                conversationTranscriber.stopTranscribingAsync();
            };
            conversationTranscriber.transcribed = function (s, e) {
                console.log("TRANSCRIBED: Text=" + e.result.text + " Speaker ID=" + e.result.speakerId);
                transcricao += e.result.text;
            };

            // Start conversation transcription
            conversationTranscriber.startTranscribingAsync(
                function () { },
                function (err) {
                    reject(new Error(result.errorDetails));
                }
            );
        });
    }
}

module.exports = { TranscriptionService };
