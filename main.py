import os
import sys
import keyboard
import pyperclip
import time
from openai import OpenAI
from google import genai
from google.genai import types
import logging
from dotenv import load_dotenv
from pathlib import Path


TRANSLATOR = 'google'
if len(sys.argv) > 1:
    arg = sys.argv[1].lower()
    if arg in ['--google', '-g']:
        TRANSLATOR = 'google'
    elif arg in ['--openai', '-o']:
        TRANSLATOR = 'openai'

# identifies where the main file is located
# and using it to look for the .env (it helps in case of global installation)
script_dir = Path(__file__).parent.absolute()
load_dotenv(script_dir/'.env')

if TRANSLATOR == 'google':
    API_KEY = os.environ.get("OPENAI_KEY", "")
    if API_KEY == "":
        raise Exception("Env variable named OPENAI_KEY not found")
elif TRANSLATOR == 'openai':
    API_KEY = os.environ.get("GOOGLE_KEY", "")
    if API_KEY == "":
        raise Exception("Env variable named GOOGLE_KEY not found")


def translate_with_google(selected_text):
    """
    This google is gemini, not google translator.
    """
    logging.info('Translating with google...')
    client = genai.Client(api_key=API_KEY)
    language = selected_text.split(':')[0]
    text = selected_text.split(':')[1]
    logging.info('Original text: ', text)

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=text,
        config=types.GenerateContentConfig(
            temperature=0.1,
            system_instruction=f"Translate to {language} and return only the translated text."
        )
    )

    logging.info('translation from google:', response.text)
    return response.text


def translate_with_openai(selected_text):
    """
    sending the text to chatgpt to translate it.
    google translator translation is really bad.
    """
    logging.info('Translating with google...')
    client = OpenAI(api_key=API_KEY)
    language = selected_text.split(':')[0]
    text = selected_text.split(':')[1]

    response = client.responses.create(
        model="gpt-5-nano",
        instructions=f"Translate to {language} and return only the text.",
        input=text,
    )

    return response.output_text


def on_triggered():
    # Releasing the pressed buttons to not interfere with the ctrl-c command.
    keyboard.release('ctrl')
    keyboard.release('alt')
    keyboard.release('r')

    keyboard.send('ctrl+c')
    time.sleep(0.1)

    original_text = pyperclip.paste()
    if not original_text:
        return

    # Pasting intermediary text to indicate that the translation is happening.
    pyperclip.copy(f'Traduzindo (pode levar alguns segundos)... {original_text}')
    keyboard.press_and_release('ctrl+v')
    keyboard.press_and_release('ctrl+a')

    # leaving as elif so we can have more options, such as claude or whatever.
    if TRANSLATOR == 'google':
        new_text = translate_with_google(original_text)
    elif TRANSLATOR == 'openai':
        new_text = translate_with_openai(original_text)

    # Pasting the new text.
    pyperclip.copy(new_text)
    keyboard.press_and_release('ctrl+v')


def start():
    print(f"Running T-1000 with {TRANSLATOR}... Press Ctrl+Alt+R to translate the selected text.")
    # Register the hotkey
    keyboard.add_hotkey('ctrl+alt+r', on_triggered)

    # Keep the program running
    keyboard.wait()


if __name__ == '__main__':
    start()
