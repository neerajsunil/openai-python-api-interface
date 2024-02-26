# ChatGPT: Asynchronous OpenAI Chat Interface
A Python script that enables asynchronous interaction with OpenAI's GPT models, allowing users to engage in natural language conversations. This script utilizes asyncio for asynchronous execution, enabling efficient handling of concurrent tasks.

## Prerequisites
Before using ChatGPT, ensure you have the following prerequisites installed:

Python 3.7 or later
OpenAI Python library (openai)
You can install the required library using pip:

```sh
pip install openai
```

## Getting Started
Set up OpenAI API key: Obtain your OpenAI API key from the OpenAI website. Replace the placeholder API_KEY in the script with your actual API key.

Choose GPT model: Select the desired GPT model from the available options provided by OpenAI. Update the MODEL variable in the script with the chosen model name.

Run the script: Execute the Python script chatgpt.py using the following command:

```sh
python chatgpt.py
```

Start conversing: Once the script is running, you can start interacting with the ChatGPT interface. Enter your messages after the prompt `You: `. To exit the conversation, type `exit`.

## Additional Notes

Stream-based interaction: ChatGPT utilizes stream-based interaction, allowing for real-time generation of responses as the conversation progresses.

Message history: The script maintains a message history to provide context to the model during conversation. Each message exchanged between the user and the assistant is stored in the message_history variable.

Asynchronous execution: The script utilizes asyncio for asynchronous execution, enabling efficient handling of I/O-bound tasks such as interacting with the OpenAI API.

Customization: Users can customize the script by adjusting parameters such as the GPT model used, API key, and conversation flow according to their requirements.

## Support
For any issues or queries related to ChatGPT, feel free to open an issue on the GitHub repository or contact the author directly.

This README provides a basic guide on how to use the provided script for asynchronous interaction with OpenAI's GPT models. Users can further customize and extend the functionality as needed for their specific use cases.
