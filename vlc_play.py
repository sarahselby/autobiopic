import vlc
import time

mood = input("Enter your mood (happy or sad): ")
if mood == 'happy':
    file_name = "happy.mp4"
else:
    file_name = "sad.mp4"

media_player = vlc.MediaPlayer()
media = vlc.Media(file_name)
media_player.set_media(media)
media_player.media_player.set_fullscreen(True)
  

media_player.play()
time.sleep(10)