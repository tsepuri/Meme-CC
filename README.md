# Meme-CC

Meme-CC is under contruction. 
The mini-game Meme-GG, based off 'Higher or Lower' can be currently run by following the steps below. 

### Project requirements

This project needs npm, pip and Python 3 to run. (This project has only been tested on Python 3.8). You also need access to either the Reddit or Twitter API tools or both. 


## Project setup

```
cd client
npm install
npm run build
cd ../server
```
It is recommended but not required that you enter a virtual environment here with ```python -m venv venv``` and ```source venv/bin/activate```
```
pip install -r requirements.txt
```
The project can store images locally or use them from the web. Replace the .env_template file with your information in a .env file. 

If you cannot run Makefile on your system, simply execute the commands in the file. Replace python with python3 in server/Makefile if you run python3 using 'python3 filename'. 
```
make seed
```
You will be prompted to choose how many images are used (the more the better). 
  
### Compiles and hot-reloads for development
```
make dev

```

