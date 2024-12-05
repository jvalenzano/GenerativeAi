import express from 'express';
import path from 'path';
import fs from 'fs';
import { exec } from 'child_process';
import sdk from 'microsoft-cognitiveservices-speech-sdk';
import multer from 'multer';
import ffmpeg from 'ffmpeg-static';
import 'dotenv/config';

const upload = multer({ dest: 'uploads/' });
const app = express();
app.use(express.json());
app.use(express.static('public'));
const uploadDir = 'uploads';

const subscriptionKey = process.env.SUBSCRIPTION_KEY;
const serviceRegion = process.env.SERVICE_REGION;
const speechRecognitionLanguage = 'en-US';

const convertedFilename = path.join(uploadDir, 'converted.wav');

app.post('/upload', upload.single('audio'), async (req, res) => {
  if (!req.file) {
    return res.status(400).json({ success: false, message: 'No file uploaded' });
  }

  const filename = req.file.path;
  console.log('Uploaded file:', req.file);
  console.log('Filename:', filename);

  try {
    await convertAudioFile(filename, convertedFilename);
    const transcription = await transcribeAudioFile(convertedFilename);
    res.json({ success: true, transcription });
  } catch (error) {
    console.error(error.message);
    res.status(500).json({ success: false, message: error.message });
  }
});

app.get('/', (req, res) => {
  res.sendFile('index.html');
});

async function convertAudioFile(inputFile, outputFile) {
  if (fs.existsSync(outputFile)) {
    fs.unlinkSync(outputFile);
  }

  const command = `"${ffmpeg}" -i "${inputFile}" -acodec pcm_s16le -ar 16000 -ac 1 "${outputFile}"`;
  return new Promise((resolve, reject) => {
    exec(command, (error, stdout, stderr) => {
      if (error) {
        reject(new Error(`Error converting audio file: ${error.message}`));
      } else {
        resolve();
      }
    });
  });
}

async function transcribeAudioFile(audioFile) {
  const pushStream = sdk.AudioInputStream.createPushStream();

  return new Promise((resolve, reject) => {
    fs.createReadStream(audioFile)
      .on('data', (arrayBuffer) => pushStream.write(arrayBuffer.slice()))
      .on('end', () => pushStream.close())
      .on('error', (err) => reject(new Error(`Error reading audio file: ${err.message}`)));

    const audioConfig = sdk.AudioConfig.fromStreamInput(pushStream);
    const speechConfig = sdk.SpeechConfig.fromSubscription(subscriptionKey, serviceRegion);
    speechConfig.speechRecognitionLanguage = speechRecognitionLanguage;

    const recognizer = new sdk.SpeechRecognizer(speechConfig, audioConfig);

    recognizer.recognizeOnceAsync(
      (result) => {
        recognizer.close();
        resolve(result.privText);
      },
      (err) => {
        recognizer.close();
        reject(new Error(`Error transcribing audio: ${err.message}`));
      }
    );
  });
}

app.listen(3000, () => {
  console.log('Server is running on port 3000');
});