"""
Rule-Based AI Chatbot
DecodeLabs Internship - Week 1 Project

A terminal chatbot that matches user input against predefined rules
using if-elif-else logic and basic string methods.
"""

from datetime import datetime

# ---------- Configuration ----------
BOT_NAME = "DecodeBot"
CREATOR = "an intern at DecodeLabs"

GREETINGS = ("hello", "hi", "hey")
EXIT_COMMANDS = ("bye", "exit", "quit")


def show_banner():
    """Print the welcome banner."""
    print("=" * 50)
    print(f"{'Welcome to ' + BOT_NAME:^50}")
    print(f"{'Rule-Based Chatbot | DecodeLabs':^50}")
    print("=" * 50)
    print("Type 'help' to see what I can do.")
    print("Type 'bye', 'exit' or 'quit' to leave.")
    print("-" * 50)


def get_response(user_input):
    """
    Return (reply, should_exit) for a given user message.
    Input is cleaned with strip() and lower() so matching
    is not affected by extra spaces or capital letters.
    """
    text = user_input.strip().lower()

    # Empty input
    if text == "":
        return "Please type something so I can help you.", False

    # Exit commands
    elif text in EXIT_COMMANDS:
        return "Goodbye! Have a great day.", True

    # Greetings
    elif text in GREETINGS:
        return "Hello! How can I help you today?", False

    # Bot's name
    elif "your name" in text or "who are you" in text:
        return f"I'm {BOT_NAME}, a rule-based chatbot.", False

    # Creator
    elif "creator" in text or "who made you" in text or "who created you" in text:
        return f"I was created by {CREATOR}.", False

    # Current time
    elif "time" in text:
        now = datetime.now().strftime("%I:%M %p")
        return f"The current time is {now}.", False

    # Current date
    elif "date" in text or "today" in text:
        today = datetime.now().strftime("%A, %d %B %Y")
        return f"Today's date is {today}.", False

    # Help
    elif text == "help":
        return (
            "I can respond to:\n"
            "  - Greetings: hello, hi, hey\n"
            "  - 'What is your name?'\n"
            "  - 'Who is your creator?'\n"
            "  - 'What time is it?'\n"
            "  - 'What is the date?'\n"
            "  - Exit: bye, exit, quit"
        ), False

    # Default response
    else:
        return "Sorry, I didn't understand that. Type 'help' to see my commands.", False


def main():
    """Run the chat loop."""
    show_banner()

    while True:
        user_input = input("You: ")
        reply, should_exit = get_response(user_input)
        print(f"{BOT_NAME}: {reply}")

        if should_exit:
            break


if __name__ == "__main__":
    main()
