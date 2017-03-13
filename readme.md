# TV-PiLight


This project allows you to use a Raspberry Pi and Blinkt as a dynamic backlight.

# Launching Pi Server

The Pi-Server should be launched on the Pi using 
```sh
cd Pi-Server
docker build -t pilight .
docker run -p 3000:3000 --privileged -ti pilight
```
# Launching Desktop Client

  - Install any missing dependencies using PIP
  - Launch the script
```sh
cd Linux-Client
python send.py
``` 
# To do
  - Connect with websocket
  - Performance optimization on python script
  - more intelligent calculation of average color (black bars on 4:3 content dim LEDs considerably)

# [See it working]
   [See it working]: <https://www.instagram.com/p/BRjYKixAfh6/?taken-by=karlnu>
