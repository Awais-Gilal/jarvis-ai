import psutil

for proc in psutil.process_iter(['pid', "name"]):
    print(proc.info['name'])
    # if proc.info['name'].lower() == 'vlc.exe'.lower():
    #     psutil.Process(proc.info['pid']).terminate()

        
        