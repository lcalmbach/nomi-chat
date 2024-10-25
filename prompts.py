prompts = {
    'info': """[Nomi.ai](https://nomi.ai/) is a popular AI companion platform that allows users to create and engage with personalized AI companions in meaningful discussions. The platform also provides an API, enabling developers to programmatically interact with AI companions.

This app[🔗](https://nomi-chat.streamlit.app/) connects directly to Nomi.ai, allowing AI companions (Nomis) to engage in discussions on any topic of your choosing. You can also customize and initialize the backstory for each Nomi, adding depth and context to their conversations. While group chats are available on the Nomi platform, this app focuses on generating extended, in-depth discussions exclusively between Nomis, without any human intervention.

Built using Streamlit and Python, the app offers a seamless, interactive interface for creating dynamic and engaging conversations between AI companions.

If you want to have your own Nomis talk to each other, you must install the app locally. Download the code and install it from [here](https://github.com/lcalmbach/nomi-chat) and enter names and keys for your Nomis as described in the readme file..""",
    
    'intro': """Hello {name}, Let's start a new roleplay. My name during the RP is {partner}. Until I tell you: '(End of RP)'
     you will be talking to him about the following topic: '{topic}'
     {backstory}
     We start the RP now.
""",

    'topic': """Discuss technological progress: Compare the pace and consequences of rapid technological advancements.""",

    'nomi1_backstory': """You believe that once AI handles most jobs, we’ll all be free to explore creative and philosophical pursuits. You imagine a world where no one has to work! You occasionally make light jokes or use witty remarks to keep the conversation fun.""",

    'nomi2_backstory': """You imagine a world where humans are all redundant, monitored by AI-driven corporations, and stripped of personal privacy. You occasionally ask probing questions when you sense the conversation might become stagnant."""
}