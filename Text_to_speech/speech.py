import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")
while 1:
    print('Say what you want')
    a = input()
    speaker.Speak(a)
