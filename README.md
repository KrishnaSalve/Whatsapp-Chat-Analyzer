# WhatsApp Chat Analyzer 

![1_O9ERcJLSpFcdIG4Ry1ednA](https://github.com/user-attachments/assets/37386b56-577c-4013-84aa-846ac76312e6)


Welcome to the WhatsApp Chat Analyzer project! This tool is designed to help you analyze your exported WhatsApp chat data to gain insights into your conversations. With this tool, you can extract various statistics, visualize message patterns, and discover trends over time.

### Description 

The WhatsApp Chat Analyzer is a powerful tool designed to help users delve into the details of their WhatsApp conversations. By analyzing your exported chat data, this tool can provide valuable insights, trends, and patterns that might otherwise go unnoticed. Whether you're curious about your chatting habits, the most active participants in a group chat, or the frequency of certain keywords or emojis, this analyzer offers a comprehensive look into your digital interactions.

### Overview

In today's digital age, messaging apps have become a primary means of communication. WhatsApp, being one of the most popular messaging platforms, is used by millions of people worldwide. With the WhatsApp Chat Analyzer, you can transform your conversations into meaningful data.

The tool allows users to process the exported chat text files and generate various statistics and visual representations, such as:

  - Participation Metrics : Understand who the most active chat participants are and how the conversation dynamics play out over time.
  - Temporal Patterns : Identify when conversations are most frequent, pinpointing peak activity hours and days.
  - Language Usage : Explore the lexicon of your chats, finding common words, phrases, and sentiment trends.
  - Emoji Analysis : Discover which emojis are most popular in your conversations and who uses them the most.
  - Visual Summaries : Engage with your chat data through a variety of charts and graphs that make analysis intuitive and accessible.

Whether for personal curiosity, academic study, or business insights, the WhatsApp Chat Analyzer provides a gateway to understanding your digital communication habits with ease and depth.


### Features 

The WhatsApp Chat Analyzer is a comprehensive tool that leverages multiple Python files to provide a seamless and feature-rich analysis experience. 

Here's an overview of the key features and the corresponding files that power them:

1. File Upload and Preprocessing : 

  - File : `preprocess.py`
  - Description : The `preprocess.py`  file handles the file upload functionality and preprocesses the exported WhatsApp chat data. It structures the raw chat information into a usable DataFrame for further analysis.

2. User-Specific Analysis : 
  - File : `app.py`
  - Description : The `app.py` file, which is the main entry point of the application, allows users to select specific chat participants or view overall group statistics for analysis.

3. Statistical Summaries : 
  - File : `helper.py`
  - Description : The `helper.py` file contains functions that fetch and calculate various statistics, such as the total number of messages, words, media files, and links shared within the chat.

4. Time-Based Visualizations : 
  - Files : `helper.py`, `app.py`
  - Description : The `helper.py` file houses functions that generate the monthly and daily timeline visualizations, which are then displayed in the `app.py` file using Streamlit.

5. Activity Maps : 
  - File : `helper.py`
  - Description : The `helper.py` file includes functions that create the weekly activity heatmap, as well as the most busy day and month bar charts, providing insights into periodic chatting habits.

6. User Engagement : 
  - File : `helper.py`
  - Description : The `helper.py` file contains the logic to identify the most active users in a group chat setup, which is then presented in the `app.py` file.

7. Word and Emoji Analysis : 
  - File : `helper.py`
  - Description : The `helper.py` file houses functions that generate the word cloud, list the most common words, and analyze emoji usage patterns. These insights are then displayed in the `app.py` file.


By separating the concerns into multiple files, the WhatsApp Chat Analyzer project maintains a modular and maintainable structure. The `app.py` file serves as the main interface, orchestrating the various analysis features by leveraging the helper functions defined in `helper.py` and `preprocess.py`. This architectural approach promotes code reusability, testability, and scalability as the project evolves.


### Project Structure 

The WhatsApp Chat Analyzer project consists of the following files : 

1. `README.md` : This file contains the project overview, features, installation instructions, and usage documentation.

2. `app.py` : 
  - This is the main entry point of the application, where the Streamlit-based user interface is defined.
  - It handles the file upload, user selection, and orchestrates the various analysis features.
  - It leverages the helper functions from `helper.py` and the preprocessing logic from `preprocess.py` to generate the desired outputs.

3. `helper.py` : 
  - This file contains the core logic and helper functions for the analysis features.
  - It includes functions for fetching statistics, creating visualizations, and performing various data transformations.
  - The functions in this file are called by the `app.py` file to power the analysis capabilities.

4. `preprocess.py` : 
  - This file is responsible for preprocessing the exported WhatsApp chat data.
  - It handles the file parsing, date and time extraction, and structuring the data into a usable DataFrame.
  - The preprocessed data is then passed to the `app.py` file for further analysis.

5. `WhatsApp Chat Analyzer.ipynb` : 
  - This Jupyter Notebook file contains the initial exploratory data analysis and prototyping of the project.
  - It serves as a development and experimentation environment for the project.

6. `procfile` : 
  - This file is used for deployment on platforms like Heroku, specifying the command to start the Streamlit application. (We have not yet deployed our project on Heroku, it is created for future developments.)

7. `setup.sh` : 
  - This shell script is used for deployment on platforms like Heroku, setting up the necessary environment and dependencies. (This file is for future developments and we have not deployed our project on Heroku yet.)

8. requirements.txt : 
  - This file lists all the Python dependencies required to run the WhatsApp Chat Analyzer project.
  - It ensures that the project can be easily set up and installed on different environments.

By organizing the project into these files, the WhatsApp Chat Analyzer maintains a clear separation of concerns, making the codebase more modular, maintainable, and scalable. The app.py file acts as the central hub, while the helper.py and preprocess.py files encapsulate the specific functionalities, promoting code reuse and testability.




### Installation

1. Clone the repository:

       git clone https://github.com/KrishnaSalve/Whatsapp-Chat-Analyzer.git

2. Navigate to the project directory:

       cd whatsapp-chat-analyzer

3. Install the required dependencies:

       pip install -r requirements.txt

**Usage**

1. Run the Streamlit Application:
      
       streamlit run app.py

 

  This will start the web application and make it accessible at http://localhost:8501/


2. Upload the Chat File : 

- Run the application by navigating to http://localhost:8501/

- In the sidebar, click on the "Choose a file" button to upload your exported WhatsApp chat file.


3. Select the User : 

- After uploading the file, the application will display the preprocessed chat data in a table.

- In the sidebar, use the dropdown menu to select the user you want to analyze. You can choose "Overall" to view the analysis for the entire group.

4. Analyze the Chat : 

- Once you have selected the user, click the "Show Analysis" button in the sidebar.
- The application will then display various insights and visualizations based on the selected user's chat data.


The application is built using Streamlit, a Python library that enables the creation of interactive and visually appealing web applications. By leveraging the code provided in the app.py, helper.py, and preprocess.py files, you can customize and extend the functionality of the WhatsApp Chat Analyzer to suit your specific needs


### Result

The WhatsApp Chat Analyzer provides a comprehensive analysis of the chat data. The key results are as follows: 

**Top Statistics**
- Total Messages :  The total number of messages in the chat.
- Total Words : The total number of words in the chat.
- Total Media files : The total number of media files (images, videos, documents, etc.) shared in the chat.
- Total Links : The total number of links shared in the chat.

**Monthly Timeline**
- The monthly timeline shows the message activity over time, with the number of messages plotted against the months.

**Daily Timeline**
- The daily timeline shows the message activity over time, with the number of messages plotted against the days.

**Activity Map**

The activity map provides insights into the busiest days and months in the chat:

- Most Busy Day : The day of the week with the highest message activity.
- Most Busy Month : The month with the highest message activity.


**Weekly Activity Heatmap**
- The weekly activity heatmap displays the message activity throughout the week, with the intensity of the activity represented by the color of the cells.


**Most Busy Users (Group Level)**
- If the "Overall" option is selected, the tool identifies the most active users in the group, displaying a bar chart and a data frame with the user names and their message counts.

**WordCloud**
- The WordCloud visualization provides a visual representation of the most common words used in the chat.

**Most Common Words**
- The tool also generates a data frame with the most common words used in the chat, along with their frequencies.

**Emoji Analysis**
- The emoji analysis includes a data frame with the count of each emoji used in the chat, as well as a pie chart visualizing the distribution of the top emojis.


The WhatsApp Chat Analyzer project provides a comprehensive set of insights and visualizations to help users understand the dynamics and patterns within their chat data.




## Contributing
We welcome contributions from the community to help improve and expand the WhatsApp Chat Analyzer project. If you're interested in contributing, please follow these guidelines:

**Report Issues** : 

If you encounter any bugs, errors, or have suggestions for improvements, please open an issue on the project's GitHub repository. When reporting an issue, provide a clear and detailed description of the problem, including any relevant error messages or screenshots.

**Submit Bug Fixes or Enhancements** : 

If you've identified a bug or have an idea for an enhancement, feel free to submit a pull request. Before starting work, please check the existing issues to ensure that your proposed change hasn't already been addressed.
When submitting a pull request, make sure to:

    1. Fork the repository and create a new branch for your changes.
    2. Clearly describe the problem you're solving and the proposed solution in the pull request description.
    3. Follow the project's coding style and conventions.
    4. Include relevant tests (if applicable) to ensure the stability of your changes.
    5. Update the documentation, including the README file, if necessary.




**Improve Documentation**

If you notice any issues or have suggestions for improving the project's documentation, such as the README file, please submit a pull request with the necessary changes.

**Provide Feedback**

We value your feedback and suggestions for improving the WhatsApp Chat Analyzer project. Feel free to share your thoughts, ideas, or use cases by opening an issue or reaching out to the project maintainers.

**Code of Conduct**

When contributing to this project, please adhere to the project's Code of Conduct to ensure a welcoming and inclusive environment for all participants.

Thank you for your interest in contributing to the WhatsApp Chat Analyzer project. We appreciate your support and look forward to collaborating with you.


### Contact

If you have any questions, feedback, or would like to get in touch with the project maintainers, you can reach us through the following channels:

- **Project Maintainer**

Name : Krishna Salve 

Email : krishnasalve97@gmail.com

Linkedin : Krishna Salve

GitHub : KrishnaSalve



- **Project Repository**

     https://github.com/KrishnaSalve/Whatsapp-Chat-Analyzer




