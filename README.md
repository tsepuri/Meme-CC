# Meme-CC

Meme-CC is under contruction. 
The mini-game Meme-GG, based off 'Higher or Lower' can be currently run by following the steps below. 

### Project requirements

This project needs npm, pip and Python>3 to run. (This project has only been tested on Python>3.8). 


## Project setup

```
cd client
npm install
npm run build
cd ../server
pip install -r requirements.txt
```
Currently, the project can only be run locally. Replace the .envtemplate file with your information in a .env file. If you have python v3.8

If you cannot run Makefile on your system, simply execute the commands in the file. Replace python3 with python in server/Makefile if you run python3 using 'python <filename>. 
```
make seed
```
You will be prompted to choose how many images are downloaded and used (the more the better). 
  
### Compiles and hot-reloads for development
```
cd ../server
make dev

```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).
