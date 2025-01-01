import express from 'express';
import axios from 'axios';
import 'dotenv/config';
import { v4 as uuidv4 } from 'uuid';

const app = express();
const port = 3000;

const subscriptionKey = process.env.TRANSLATORTEXTSUBSCRIPTIONKEY;
const endpoint = process.env.TRANSLATORTEXTENDPOINT;

if (!subscriptionKey || !endpoint) {
  throw new Error("Environment variables TRANSLATOR_TEXT_SUBSCRIPTION_KEY and TRANSLATOR_TEXT_ENDPOINT must be set");
}

app.use(express.json());
app.use(express.static('public'));

app.post('/translate', async (req, res) => {
  const { fromLanguage, toLanguage, inputText } = req.body;

  const url = `${endpoint}/translate?api-version=3.0&from=${fromLanguage}&to=${toLanguage}`;
  const headers = {
    'Ocp-Apim-Subscription-Key': subscriptionKey,
    'Ocp-Apim-Subscription-Region': 'westus2',
    'Content-type': 'application/json',
    'X-ClientTraceId': uuidv4().toString()
  };
  const body = [{
    'Text': inputText
  }];

  try {
    const response = await axios.post(url, body, { headers });
    const translatedText = response.data[0].translations[0].text;
    res.json({ translatedText });
  } catch (error) {
    console.error("Translation error: ", error);
    res.status(500).send('Error translating text');
  }
});

app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});