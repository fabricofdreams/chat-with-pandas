# Earthquakes Data Analysis with Chat Interface

This application provides a platform for analyzing earthquake data through a conversational interface. Users can interact with the data by asking questions and receiving relevant insights.

## Features

- **Data Analysis:** Utilizes earthquake data to provide insights and analysis.
- **Conversational Interface:** Allows users to interact with the data using natural language.
- **Filtering and Sorting:** Enables users to filter and sort the data based on their preferences.

## Setup Instructions

Follow these steps to set up and run the application locally:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/fabricofdreams/chat-with-pandas/tree/main
   cd earthquakes-basic
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Environment Variables:**
   Ensure that the required environment variables are properly configured. You may need to create a `.env` file and populate it with necessary keys and values.

4. **Run the Application:**
   ```bash
   streamlit run main.py
   ```

5. **Interact with the Application:**
   Once the application is running, access it through your web browser. You can start interacting with the data by typing messages in the chat interface.

## File Structure

- **main.py:** Main application file responsible for initializing the Streamlit app and handling user interactions.
- **get_data.py:** Contains functions to retrieve and preprocess earthquake data for analysis.
- **chat_with_data.py:** Implements the conversational interface for interacting with the data.
- **ai_functions.py:** Defines auxiliary functions and AI-related utilities used in the application.

## Dependencies

- `streamlit`: For building interactive web applications with Python.
- `dotenv`: For loading environment variables from a `.env` file.
- `pandas`: For data manipulation and analysis.
- `langchain`: For handling natural language processing tasks and conversation management.
- `langchain_openai`: Provides integration with OpenAI's language models for conversational AI.

## Usage

Upon running the application, users can type messages in the chat interface to interact with the earthquake data. The system will respond with relevant insights and information based on the user's queries.

## Contributors

- [FabricOfDreams](mailto:fernando.robledoruiz@gmail.com)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Certainly! Here's an additional note to include in your README:

---

## API Key Requirement

This application requires an OpenAPI key for certain functionalities to work properly. To integrate your OpenAPI key securely:

1. **Create a `.env` File:**
   In the root directory of the project, create a file named `.env`.

2. **Store Your API Key:**
   Within the `.env` file, store your OpenAPI key in the following format:
   ```
   OPEN_API_KEY="your-api-key-here"
   ```

3. **Load the Environment Variables:**
   The application uses the `dotenv` library to load environment variables from the `.env` file during runtime.

Ensure that your OpenAPI key is properly configured in the `.env` file to enable seamless integration with the application's functionalities.
