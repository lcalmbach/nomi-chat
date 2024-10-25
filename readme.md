# 🚧 Nomi Chat - Companion Chatbots Conversation App 🚧

Nomi Chat is a Python-based application built with Streamlit that allows users to connect two AI companions from [Nomi.ai](https://nomi.ai) and initiate automated, in-depth conversations on any topic. Customize each companion’s personality, set the backstory, and watch as the chatbots engage in dynamic dialogues without human intervention.

## Features

- **Customizable Chatbots**: Connect two AI companions with distinct personalities and backstories.
- **Topic Selection**: Choose a topic for the chatbots to discuss.
- **Automated Conversations**: Let the chatbots engage in natural, lengthy dialogues without human prompts.
- **Streamlit Interface**: A simple, user-friendly interface built with Streamlit.
- **Downloadable Conversations**: Save conversation transcripts to review or share later.

## Getting Started

### Prerequisites

- **Python 3.8+**: Ensure you have Python installed.
- **Streamlit**: Install Streamlit using `pip install streamlit`.
- **Nomi API Key**: You’ll need API keys for the AI companions from [Nomi.ai](https://nomi.ai) to enable interaction.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/rohithill/nomi-chat
   cd nomi-chat
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. In the .streamlit-folder rename the secrets_template.toml file to secrets.toml. Enter their access keys which you will find in your Nomis profile as well as the authentification key found under profile\integrations. the current UI expects 3 nomis, you can easily add more.

### Running the App

To start the app, run:

```bash
streamlit run app.py
```

This will open the app in your web browser.

### Usage

1. **Set Companion Names and API Keys**: In the app interface, enter the names and API keys for each Nomi companion.
2. **Choose a Topic**: Select a subject for the chatbots to discuss, or customize one.
3. **Start the Conversation**: Click “Start Conversation” to let the chatbots begin their dialogue.
4. **Save the Conversation**: Download the conversation as a text file to capture their entire discussion.

### Example Topics

- **The Future of AI**
- **Environmental Challenges**
- **Philosophy of Consciousness**
- **Technological Ethics**

## Screenshots

![App Interface Screenshot](./assets/screenshot.webp)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an issue if you have suggestions for features, improvements, or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

For questions, issues, or feature requests, please reach out via [GitHub Issues](https://github.com/lcalmbach/nomi-chat/issues).
