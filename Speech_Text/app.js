import express from 'express';
import path from 'path';
import fs from 'fs';
import { exec } from 'child_process';
import sdk from 'microsoft-cognitiveservices-speech-sdk';
import multer from 'multer';

import 'dotenv/config';
import { fileURLToPath } from 'url'; // Import the fileURLToPath function

import { TextAnalyticsClient, AzureKeyCredential } from "@azure/ai-text-analytics";

import { spawn } from 'child_process';
//import ffmpeg from 'fluent-ffmpeg';
import ffmpeg from 'fluent-ffmpeg';
import ffmpegStatic from 'ffmpeg-static';


// Load the .env file if it exists
import * as dotenv from "dotenv";
dotenv.config();

const upload = multer({ dest: 'uploads/' });
const app = express();
app.use(express.json());
app.use(express.static('public'));
const uploadDir = 'uploads';
import { SpeechConfig, AudioConfig, SpeechRecognizer } from 'microsoft-cognitiveservices-speech-sdk';
const __filename = fileURLToPath(import.meta.url);
const currentDirectory = path.dirname(__filename); // Get the current directory path
const subscriptionKey = process.env.SUBSCRIPTION_KEY;
const serviceRegion = process.env.SERVICE_REGION;
const speechRecognitionLanguage = 'en-US';

const speechConfig = sdk.SpeechConfig.fromSubscription(subscriptionKey, serviceRegion);


const convertedFilename = path.join(uploadDir, 'converted.wav');

app.post('/upload', upload.single('audio'), async (req, res) => {
  if (!req.file) {
    return res.status(400).json({ success: false, message: 'No file uploaded' });
  }

  const filename = req.file.path;
  console.log('Uploaded file:', req.file);
  console.log('Filename:', filename);
  /*
  try {
    await convertAudioFile(filename, convertedFilename);
    setTimeout(async () => {

    const transcription = await transcribeAudioFile(convertedFilename);
    res.json({ success: true, transcription });
  }, 3000); // 10000 milliseconds = 10 second

  } catch (error) {
    console.error(error.message);
    res.status(500).json({ success: false, message: error.message });
  }
  */
  //await convertAudioFile(filename, convertedFilename);
  const transcription = await transcribeFull(filename);
  res.json({ success: true, transcription });

});

app.get('/', (req, res) => {
  res.sendFile('index.html');
});


const convertedFilename2 = path.join(uploadDir, 'emptyAudioConversion11.wav');

//select from speechtotextnition dir. **************
app.post('/upload2', upload.single('video'), async (req, res) => {
  if (!req.file) {
    return res.status(400).json({ success: false, message: 'No file uploaded' });
  }

  const filename = req.file.path;
  console.log('Uploaded file:', req.file);
  console.log('Filename:', filename);

  try {
    console.log('converting video');
    ffmpeg.setFfmpegPath(ffmpegStatic);

    // Example: Convert a video file
    let upDir = path.join(uploadDir, 'emptyVideoConversion.wav');
    ffmpeg(filename)
      .output(upDir)
      .on('end', () => console.log('Conversion finished!'))
      .on('error', (err) => console.error('An error occurred:', err))
      .run();


    convertAudioFile(upDir, convertedFilename2);
    setTimeout(async () => {

      //console.log('Step: await convertAudioFile completed:');
      const transcription = await transcribeFull(convertedFilename2);
      //console.log('Step: Transcription Finished Sending JSON response.');
      res.json({ success: true, transcription });

    }, 10000); // 10000 milliseconds = 10 second


  } catch (error) {
    console.error(error.message);
    res.status(500).json({ success: false, message: error.message });
  }
});


app.get('/api/pirates', (req, res) => {
  const pirate =  { id: 1, name: 'Blackbeard' };
  res.send({ data: pirate });
});

app.get('/', (req, res) => {
  res.sendFile('index.html');
});


async function convertAudioFile(inputFile, outputFile) {
  if (fs.existsSync(outputFile)) {
    fs.unlinkSync(outputFile);
  }

  const command = `"${ffmpegStatic}" -i "${inputFile}" -acodec pcm_s16le -ar 16000 -ac 1 "${outputFile}"`;
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


function transcribeAudioFile22() {
  const convertedFilename = path.join('converted-short.wav');

  console.log("transcribing audio file.")
  const pushStream = sdk.AudioInputStream.createPushStream();

  return new Promise((resolve, reject) => {
    fs.createReadStream(convertedFilename)
      .on('data', function (arrayBuffer) { pushStream.write(arrayBuffer.slice()); })
      .on('end', function () { pushStream.close() })
      .on('error', (err) => reject(new Error(`Error reading audio file: ${err.message}`)));
    /*
    fs.createReadStream(convertedFilename)
      .on('data', (arrayBuffer) => pushStream.write(arrayBuffer.slice()))
      .on('end', () => pushStream.close())
      .on('error', (err) => reject(new Error(`Error reading audio file: ${err.message}`)));
*/
    const audioConfig = sdk.AudioConfig.fromStreamInput(pushStream);
    const speechConfig = sdk.SpeechConfig.fromSubscription(subscriptionKey, serviceRegion);
    speechConfig.speechRecognitionLanguage = speechRecognitionLanguage;

    const recognizer = new sdk.SpeechRecognizer(speechConfig, audioConfig);

    let conversationTranscriber = new sdk.ConversationTranscriber(speechConfig, audioConfig);

    //let speechRecognizer = new sdk.SpeechRecognizer(speechConfig, audioConfig);

    // Start conversation transcription based on speech recognizer 
    recognizer.startContinuousRecognitionAsync();

    conversationTranscriber.startTranscribingAsync(
      function () { },
      function (err) {
        console.trace("err - starting transcription: " + err);
      }
    );

    let myTextRes = '';
    conversationTranscriber.transcribed = function (s, e) {
      //console.log("Result recognized: " +  sdk.ResultReason.RecognizedSpeech + " TRANSCRIBED: Text=" + e.result.text + " Speaker ID=" + e.result.speakerId);
      if (e.result.reason == sdk.ResultReason.RecognizedSpeech) {
        myTextRes = "Speaker ID = " + e.result.speakerId + '\n' + myTextRes + e.result.text + '\n';
        console.log("TRANSCRIBED: Text=" + e.result.text + " Speaker ID=" + e.result.speakerId);
      }
      else if (e.result.reason == sdk.ResultReason.NoMatch) {
        console.log("NOMATCH: Speech could not be recognized.");
      }
    };

    conversationTranscriber.speechEndDetected = function (s, e) {
      console.log('\n' + '\n' + "~~~speechEndDetected~~~" + '\n');
      console.log(myTextRes);
      recognizer.close();
      conversationTranscriber.close();
      resolve(myTextRes);
    };


    /*
    recognizer.recognizeOnceAsync(
      (result) => {
        recognizer.close();
        console.log(result.privText);
        resolve(result.privText);
      },
      (err) => {
        recognizer.close();
        reject(new Error(`Error transcribing audio: ${err.message}`));
      }
    );
    */
  });
}

async function transcribeAudioFile(audioFile) {

  const pushStream = sdk.AudioInputStream.createPushStream();
  console.log("Step: Transcribing audio file.")

  return new Promise((resolve, reject) => {


    fs.createReadStream(audioFile)
      .on('data', (arrayBuffer) => pushStream.write(arrayBuffer.slice()))
      .on('end', () => pushStream.close())
      .on('error', (err) => reject(new Error(`Error reading audio file: ${err.message}`)));

    const audioConfig = sdk.AudioConfig.fromStreamInput(pushStream);
    const speechConfig = sdk.SpeechConfig.fromSubscription(subscriptionKey, serviceRegion);
    speechConfig.speechRecognitionLanguage = speechRecognitionLanguage;

    const recognizer = new sdk.SpeechRecognizer(speechConfig, audioConfig);

    let conversationTranscriber = new sdk.ConversationTranscriber(speechConfig, audioConfig);

    //let speechRecognizer = new sdk.SpeechRecognizer(speechConfig, audioConfig);

    // Start conversation transcription based on speech recognizer 
    recognizer.startContinuousRecognitionAsync();

    conversationTranscriber.startTranscribingAsync(
      function () { },
      function (err) {
        console.trace("err - starting transcription: " + err);
      }
    );


    let myTextRes = '';
    conversationTranscriber.transcribed = function (s, e) {
      if (e.result.reason == sdk.ResultReason.RecognizedSpeech) {
        myTextRes = "Speaker ID = " + e.result.speakerId + '\n' + myTextRes + e.result.text + '\n';
        console.log("TRANSCRIBED: Text=" + e.result.text + " Speaker ID=" + e.result.speakerId);
      }
      else if (e.result.reason == sdk.ResultReason.NoMatch) {
        console.log("NOMATCH: Speech could not be recognized.");
      }
      console.log("**SPEECH RESULT: " + sdk.ResultReason.RecognizedSpeech + " TRANSCRIBED: Text=" + e.result.text + " Speaker ID=" + e.result.speakerId);
    };

    conversationTranscriber.speechEndDetected = function (s, e) {
      console.log('\n' + '\n' + "~~~speechEndDetected~~~" + '\n');
      console.log(myTextRes);
      recognizer.close();
      conversationTranscriber.close();
      resolve(myTextRes);
    };


    /*
    recognizer.recognizeOnceAsync(
      (result) => {
        recognizer.close();
        console.log(result.privText);
        resolve(result.privText);
      },
      (err) => {
        recognizer.close();
        reject(new Error(`Error transcribing audio: ${err.message}`));
      }
    );
    */

  });
}



app.listen(3000, () => {
  console.log('Server is running on port 3000');
});


//transcribeFull('converted-short.wav');


async function transcribeFull(filename) {
  let myTextRes = '';

  const speechConfig = sdk.SpeechConfig.fromSubscription(subscriptionKey, serviceRegion);

  // uploads\converted-short.wav

  let audioConfig = sdk.AudioConfig.fromWavFileInput(fs.readFileSync(filename));
  let conversationTranscriber = new sdk.ConversationTranscriber(speechConfig, audioConfig);

  speechConfig.setServiceProperty("conversationTranscriptionInRoomAndOnline", "true", sdk.ServicePropertyChannel.UriQueryParameter);
  speechConfig.setServiceProperty("conversationEndSilenceTimeoutMs", 60000, sdk.ServicePropertyChannel.UriQueryParameter);

  let pushStream = sdk.AudioInputStream.createPushStream();
  return new Promise((resolve, reject) => {

    fs.createReadStream(filename).on('data', function (arrayBuffer) {
      pushStream.write(arrayBuffer.slice());
    }).on('end', function () {
      pushStream.close();
    });

    conversationTranscriber.startTranscribingAsync(
      function () { },
      function (err) {
        console.trace("err - starting transcription: " + err);
      }
    );

    conversationTranscriber.transcribed = function (s, e) {
      if (e.result.reason == sdk.ResultReason.RecognizedSpeech) {
        //myTextRes =  "Speaker ID = " + e.result.speakerId +  '\n' +  myTextRes + e.result.text + '\n';
        myTextRes += "TRANSCRIBED: Text=" + e.result.text + " Speaker ID=" + e.result.speakerId
        console.log("TRANSCRIBED: Text=" + e.result.text + " Speaker ID=" + e.result.speakerId);
      }
      else if (e.result.reason == sdk.ResultReason.NoMatch) {
        console.log("NOMATCH: Speech could not be recognized.");
      }
      console.log("**SPEECH RESULT: " + sdk.ResultReason.RecognizedSpeech + " TRANSCRIBED: Text=" + e.result.text + " Speaker ID=" + e.result.speakerId);
    };

    conversationTranscriber.speechEndDetected = function (s, e) {
      resolve(myTextRes);
      console.log('\n' + '\n' + "~~~speechEndDetected wip~~~" + '\n');
      console.log(myTextRes);
      recognizer.close();
      conversationTranscriber.close();
      resolve(myTextRes);
    };
  });
}


//transcribeAudioFile22();
//You are absolutely correct! It's impossible to directly convert MP4 to WAV in the browser using JavaScript alone due to security restrictions and the complexity of the conversion process.
//If you run app service as docker container, you can install anything on it.

//converted-short.wav
//mk.mp4

/*
async function loadFFmpeg() {
  const ffmpeg = await import('ffmpeg-static');
  // Use ffmpeg here
  ffmpeg.input('mk.mp4')
  .output('out.wav')
  .run();
  
}

loadFFmpeg();
 */
/*
const ffmpegPath = "C:\\Users\\AndrewHimonas\\Projects\\FFFMPEG";

console.log(ffmpegPath); // Output: C:\Users\AndrewHimonas\Projects\FFFMPEG


process.env.FFMPEG_PATH = ffmpegPath;

async function convertMp4ToWav(inputFile, outputFile) {
  return new Promise((resolve, reject) => {
    console.log(ffmpeg.path);
    const ffmpegProcess = spawn(ffmpeg.path, [
      '-i', inputFile,
      outputFile
    ]);

    ffmpegProcess.on('close', (code) => {
      if (code === 0) {
        resolve();
      } else {
        reject(new Error(`Conversion failed with code: ${code}`));
      }
    });

    ffmpegProcess.stderr.on('data', (data) => {
      console.error(`FFmpeg error: ${data}`);
    });
  });
}
*/


/*
// Example usage:
const inputFile = 'mk.mp4';
const outputFile = 'output.wav';

convertMp4ToWav(inputFile, outputFile)
  .then(() => {
    console.log('Conversion successful!');
  })
  .catch(error => {
    console.error('Conversion failed:', error);
  });

*/

//WORKING

//https://stackoverflow.com/questions/55824423/how-to-transcribe-full-audio-text-from-a-wav-file
/*
const convertedFilename = path.join(uploadDir, 'converted-short.wav');
const audioFilePath = 'converted-short.wav';
var filename = "converted-short.wav"; // 16000 Hz, Mono

let pushStream = sdk.AudioInputStream.createPushStream();

fs.createReadStream(filename).on('data', function(arrayBuffer) {
    pushStream.write(arrayBuffer.slice());
}).on('end', function() {
    pushStream.close();
});

let audioConfig = sdk.AudioConfig.fromWavFileInput(fs.readFileSync(filename));
let speechRecognizer = new sdk.SpeechRecognizer(speechConfig, audioConfig);
let conversationTranscriber = new sdk.ConversationTranscriber(speechConfig, audioConfig);

fs.createReadStream(filename).on('data', function(arrayBuffer) {
  pushStream.write(arrayBuffer.slice());
}).on('end', function() {
  pushStream.close();
  console.log('finished writing');
});

conversationTranscriber.transcribed = function(s, e) {
  //console.log("Result recognized: " +  sdk.ResultReason.RecognizedSpeech + " TRANSCRIBED: Text=" + e.result.text + " Speaker ID=" + e.result.speakerId);
  if (e.result.reason == sdk.ResultReason.RecognizedSpeech) {
    console.log("TRANSCRIBED: Text=" + e.result.text + " Speaker ID=" + e.result.speakerId);
  }
  else if (e.result.reason == sdk.ResultReason.NoMatch) {
    console.log("NOMATCH: Speech could not be recognized.");
}
};

conversationTranscriber.speechEndDetected  = function (s, e) {
  console.log("(speechEndDetected)");
  //does this mean it stoped? 
};

// Start conversation transcription based on speech recognizer 
speechRecognizer.startContinuousRecognitionAsync();
    conversationTranscriber.startTranscribingAsync(
      function () {},
      function (err) {
          console.trace("err - starting transcription: " + err);
      }
  );
*/