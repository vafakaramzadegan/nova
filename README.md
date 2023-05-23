# Nova: A Virtual Assistant Written in Python

Nova is a virtual assistant that uses the OpenAI API and a chatGPT model to interact with human users via speech. Nova is constantly listening for voice input and when sound is detected, it uses speech recognition to check if a special trigger like "Hey Nova" was said by the user. After that, it starts to listen for the upcoming commands or speech from the user, and this time it sends the detected text from the command to the chatGPT model through the OpenAI API. As soon as it gets the response, it converts it to audio using the gTTS package and plays the audio output using pydub.

## Features

Nova offers a range of features that can be customized through the env file. These features include:

- Using the OpenAI API key to connect to the chatGPT model
- Setting the language for the communication with Nova
- Setting the user's name, timezone, and country
- Customizing the assistant's name and trigger phrase
- Setting the assistant's listening timeout

## Installation
Before getting started, please make sure that you have already installed the required prerequisites on your computer. You can do this by running the following commands on your terminal:

```
sudo apt update
sudo apt install portaudio19-dev python3-pyaudio
sudo apt install ffmpeg
```
Once the prerequisites are installed, you can proceed with setting up the program by following the steps below:

1. Clone the repository on your local machine by running the following command on your terminal:

   ```
   git clone https://github.com/vafakaramzadegan/nova.git
   ```
   
2. Navigate to the project directory by running the following command:

   ```
   cd nova
   ```
   
3. Create a virtual environment for the project by running the following command:

   ```
   python3 -m venv venv
   ```
   
4. Activate the virtual environment:

   ```
   source ./venv/bin/activate
   ```
   
5. Install the requirements for the project by running the following command:

   ```
   pip3 install -r requirements.txt
   ```
   
6. You can now run the program by executing the following command:

   ```
   python3 <file_name>.py
   ```


## Contribution Guidelines

If you would like to contribute to Nova, please follow these steps:

1. Create an issue in the repository to discuss your proposed changes.
2. Fork the repository and make your desired changes.
3. Submit a Pull Request for the changes you have made.
4. Your changes will be reviewed, and if approved, they will be merged into the main repository.

All contributions, be it bug fixes, new features, or documentation improvements, are warmly welcomed.

Thank you for your interest in Nova, and I look forward to your contributions!