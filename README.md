### README for Python Flask Application

This Python application is built using Flask, a micro web framework. It's designed for handling image generation requests.

### Project Overview

This project aims to be an innovative aide for Dungeons & Dragons (D&D) players, particularly during the critical 'Session 0' and early adventure stages. The concept revolves around enhancing the D&D experience by integrating advanced technologies like AI, stable diffusion, and cross-chain blockchain transactions. A key feature is the generation of unique loot items, such as "legendary daggers," which are created as AI-generated images and minted as Non-Fungible Tokens (NFTs). This application is a blend of fantasy and cutting-edge tech, designed to bring a new dimension to the classic role-playing game.

### Technologies and Architecture

- **Backend**: Developed in Python and deployed on AWS for robust and scalable performance.
- **AI and Image Generation**: Utilizing AI and stable diffusion techniques for creating unique, AI-generated in-game items.
- **Blockchain and NFTs**: Integration with cross-chain blockchain transactions and decentralized IPFS storage for NFTs. The NFTs are available on the OpenSea marketplace.
- **Frontend Interface**: Developed in React JS, providing a seamless and intuitive user experience.
- **Augmented Reality Features**: The frontend includes augmented reality capabilities, leveraging the motion and gyroscopic features of smartphones to enhance user engagement.
- **Repository Link**: For more details on the frontend, visit the repository at [chainlink-hackathon-frontend](https://github.com/spencerkinney/chainlink-hackathon-frontend).

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
