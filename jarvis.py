try:
    import pyttsx3
    import datetime
    import speech_recognition as sr
    import webbrowser
    import random
    import os
    import requests
    import wikipedia
    import psutil

except ImportError:
    import os
    os.system('pip install speechRecognition  wikipedia pocketsphinx smtplib  psutil pyttsx3 pyaudio')

finally:
    import pyttsx3
    import datetime
    import speech_recognition as sr
    import webbrowser
    import random
    import os
    import requests
    import wikipedia
    import psutil

main_list = ["wmplayer.exe"]

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voices', voices[0].id)

def speak(audio):
    try:
        engine.say(audio.lower())
        engine.runAndWait()
    except Exception as e:
        print(e)

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir.")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir.")
    else:
        speak("Good Evening Sir.")
    speak("I am jarvis.   Plese tell me how can i assist you.")
    # speak('Loading resiurces please wait.')

def takecommand():
    """ it takes microphone input form user and return in text"""
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        speak("listening.")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("recognizing....")
        speak("recognizing.")
        # query = r.recognize_google_cloud(audio, language='en-US')
        # query = r.recognize_sphinx(audio, language='en-US')
        query = r.recognize_google(audio, language='en-in')
        if type(query) is None:
            query = "None"
        print(f"User input: {query}")
    
    except Exception as e:
        print(e)
        speak("Say that again please...")
        return "None"
    else:
        return query

def check_internet():
    try:
        requests.get("https://www.google.com/")
    except:
        return True #False
    else:
        return True

def command_to_wikipedia(com):
    com = com.replace("according to wikipedia", "")
    try:
        ans = wikipedia.summary(com, sentences=2)
    except:
        speak("recource error")
        return "None"
    else:
        return ans

def say_time():
    time = str(datetime.datetime.now().strftime("%H:%M:%S"))
    speak(f"The time is, {time}")

def play_random_music():
    music_path = "C:\\Users\\awais\\Music"
    music_list = os.listdir(music_path)
    r = random.randint(1, len(music_list))
    try:
        os.startfile(os.path.join(music_path, music_list[r-1]))
    except FileNotFoundError:
        speak("File does not exists")

def open_vscode():
    vs_code_path = "E:\\New folder\\Microsoft VS Code\\Code.exe"
    try:
        os.startfile(vs_code_path)
    except FileNotFoundError:
        speak("File does not exists")

def open_office_word():
    office_path = "D:\\ms office 2007\\Office12\\WINWORD.EXE"
    try:
        os.startfile(office_path)
    except FileNotFoundError:
        speak("File Does not exists")

def close_program(program_name):
    pass
    try:
        for process in psutil.porcess_iter(['pid', 'name']):
            if process.info['name'].lower() == program_name.lower():
                psutil.Process(process.info['pid']).terminate()
                speak(f"Successfuly terrminated {program_name}")
                break
    except Exception as e:
        print(e)
        speak(f"an error accored while terminateing {program_name}")
#empity commit

def run_main():
    wishme()
    if True:
        if check_internet():
            command = takecommand().lower()
            # command = "close music player"
            if "the time" in command:
                say_time()
            elif "according to wikipedia" in command:
                speak(command_to_wikipedia(command))

            elif "are you listening" in command or "are you there" in command or "are you their" in command:
                speak("I am listening you. Please tell me how can i assist you")
            elif "thanks jarvis" in command:
                speak("You welcome sir, please inform me if you have any querstion")

            #opening browsers and apps====================
            elif "open google" in command:
                webbrowser.open("google.com")
            elif "open youtube" in command:
                webbrowser.open("youtube.com")
            elif "open gmail" in command:
                webbrowser.open("gmail.com")
            elif "open stakoverflow" in command:
                webbrowser.open("stakeoverflow.com")
            elif "open ai" in command or "chat gpt" in command or "chatgpt" in command:
                webbrowser.open("https://chat.openai.com/")
            elif "open github" in command or "open git" in command:
                webbrowser.open("github.com")
            #========================================
            elif "open microsoft office word" in command or "ms word" in command:
                open_office_word()
            elif "open code" in command or "vs code" in command or "visual studio code" in command:
                open_vscode()

            # playing musics videos =========================
            elif "play music" in command:
                play_random_music()

            #closeing programs commands ============================
            elif "close music player" in command:
                close_program("Groov Music")
            elif "quite" in command or "exit" in command:
                speak("Thanks for using me. Good bye.")
                exit()
            else:
                pass
        else:
            speak("Your are not connected with my source files. Plese connect with internet and try again later.")
            exit()
if __name__ == "__main__":
    run_main()