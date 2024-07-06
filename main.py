from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, CallbackContext
from telegram.ext import filters

# Define Morse code dictionary
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 
    'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 
    'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 
    'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', 
    '7': '--...', '8': '---..', '9': '----.', '0': '-----', ',': '--..--', '.': '.-.-.-', 
    '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-'
}

# Function to convert text to Morse code
def text_to_morse(text):
    morse = []
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            morse.append(MORSE_CODE_DICT[char])
        elif char == ' ':
            morse.append('/')
        else:
            morse.append('?')
    return ' '.join(morse)

# Function to convert Morse code to text
def morse_to_text(morse):
    words = morse.split('/')
    decoded_message = []

    for word in words:
        letters = word.split()
        decoded_word = ''.join([key for letter in letters for key, value in MORSE_CODE_DICT.items() if value == letter])
        decoded_message.append(decoded_word)

    return ' '.join(decoded_message)

# Function to start the bot
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Hi! Send me a message to convert it to Morse code or use /morse2text to decode Morse code.')

# Function to convert text to Morse code
async def handle_message(update: Update, context: CallbackContext) -> None:
    user_input = update.message.text
    morse_code = text_to_morse(user_input)
    await update.message.reply_text(morse_code)

# Function to convert Morse code to text
async def morse2text(update: Update, context: CallbackContext) -> None:
    morse_code = ' '.join(context.args)
    plain_text = morse_to_text(morse_code)
    await update.message.reply_text(plain_text)

# Main function to set up the bot
def main():
    # Create the Application and pass it your bot's token
    TOKEN = '7038777541:AAF3m10jbLY3Tuij5bgHvmD0Cr3Gk23pT9E'
    application = ApplicationBuilder().token(TOKEN).build()

    # Register handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    application.add_handler(CommandHandler("morse2text", morse2text))

    # Start the Bot
    application.run_polling()

# Run the main function
if __name__ == '__main__':
    main()
