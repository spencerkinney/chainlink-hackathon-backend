### README for Python Flask Application

This Python application is built using Flask, a micro web framework. It's designed for handling image generation requests.

### Setup Instructions

1. **Install Python**: Ensure Python is installed on your computer. Download it from the [Python website](https://www.python.org/downloads/).

2. **Clone the Repository**: Download the project code to your local machine.

3. **Create a Virtual Environment** (optional but recommended):
   - Navigate to the project directory.
   - Run `python -m venv venv` to create a virtual environment named 'venv'.
   - Activate the virtual environment:
     - Windows: `venv\Scripts\activate`
     - macOS/Linux: `source venv/bin/activate`

4. **.env File Setup**:
   - Ensure you have a `.env` file in the same directory. The file should contain:
     ```
     REPLICATE_API_TOKEN = 'API TOKEN'
     FLASK_ENV = 'development'
     ```
   - Obtain the `REPLICATE_API_TOKEN` from Spencer or [replicate.com](https://replicate.com).

5. **Install Dependencies**:
   - Ensure the virtual environment is active.
   - Run `pip install -r requirements.txt` to install required packages.

6. **Start the Flask Server**:
   - Run `flask run` to start the server.
   - Access the application at `localhost:5000`.

### Application Structure

- **Server Code (`app.py`)**: Contains the Flask server setup, route definitions, and image processing logic.

### Key Features

- **Image Generation Endpoint**: `/generate-image` - POST endpoint to process image generation prompts.
- **Home Endpoint**: `/` - A simple GET endpoint returning a status message.

### Development Notes

- The application uses environment variables set in the `.env` file for configuration.
- The server runs in development mode by default, allowing for live updates and debugging.

Experiment with the endpoints to understand the application's functionality.
