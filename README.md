# DMGPT
OpenAI interfaced dungeon master. It will use whisper to talk to chatGPT, you will be able  to choose between GPT3.5 or GPT4, play audio for dialogue, and create images for characters and places.

https://github.com/openai

###  LLM 
https://platform.openai.com/docs/api-reference

### voice to text
https://github.com/openai/whisper

### text to voice
https://elevenlabs.io/

### image generator


## Project Structure

The project has the following file structure:

```
my-fastapi-react-app/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── models/
│   │   │   └── __init__.py
│   │   ├── routes/
│   │   │   ├── __init__.py
│   │   │   └── items.py
│   │   └── schemas/
│   │       └── __init__.py
│   ├── requirements.txt
│   └── README.md
├── frontend/
│   ├── public/
│   │   ├── index.html
│   │   └── favicon.ico
│   ├── src/
│   │   ├── App.js
│   │   ├── index.js
│   │   ├── components/
│   │   │   └── ItemList.js
│   │   └── utils/
│   │       └── api.js
│   ├── package.json
│   ├── package-lock.json
│   └── README.md
└── README.md
```