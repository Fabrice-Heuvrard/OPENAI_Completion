# OPENAI_Completion

ChatGPT - A text generation program using OpenAI's GPT-3 API
This program uses OpenAI's GPT-3 API to generate text based on a prompt. Users can select the GPT-3 model to use, adjust the degree of creativity (temperature), and choose the number of tokens to use (which will be deducted from the credit).

Prerequisites
Before using this program, you need to obtain an OpenAI API key and store it in a text file named openAI_KEY.txt.

How to use the program
Launch the program using the command python chatGPT.py. You will be prompted to select the GPT-3 model to use, adjust the degree of creativity (temperature), and choose the number of tokens to use. You can then enter your prompt, and the program will generate a response using OpenAI's GPT-3 API.

Functions
read_api_key(file_path)
Reads and returns the OpenAI API key stored in a text file.

select_GPT_3_model()
Displays the available GPT-3 model options and prompts the user to select one. Returns the selected model or None if the selection is not valid.

select_GPT_3_temperature()
Prompts the user to enter the desired degree of creativity (temperature), then adjusts the value to ensure it is between 0 and 1.

select_GPT_3_token()
Prompts the user to enter the number of tokens to use, which will be deducted from the credit. Returns the value entered.

main()
The main function that calls the other functions to prompt the user for the necessary information to generate text using OpenAI's GPT-3 API. It also generates the text from the response provided by the API and displays it to the user, as well as the credit consumption statistics.
