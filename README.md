# FitBuddy AI Workout Generator

A FastAPI-based web application that generates personalized workout plans using Google's Gemini AI. Users can input their fitness goals, intensity preferences, and receive customized 5-day workout plans along with nutrition tips.

## Features

- **AI-Powered Workout Generation**: Uses Google Gemini AI to create personalized workout plans
- **User Input Form**: Collects user details (name, age, weight, goal, intensity)
- **Nutrition Tips**: Provides goal-specific nutrition advice
- **Feedback System**: Allows users to provide feedback to refine workout plans
- **User Management**: Stores user data and workout history in SQLite database
- **Web Interface**: Clean HTML templates for user interaction
- **API Fallbacks**: Graceful handling of API quota limits with sample plans

## Tech Stack

- **Backend**: FastAPI (Python)
- **AI**: Google Gemini AI (gemini-2.5-flash)
- **Database**: SQLite with SQLAlchemy ORM
- **Frontend**: Jinja2 Templates with HTML/CSS
- **Environment**: Python dotenv for configuration

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd FitBuddy
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   - Create a `.env` file in the root directory
   - Add your Google AI API key:
     ```
     GOOGLE_API_KEY=your_api_key_here
     ```
   - Get your API key from [Google AI Studio](https://makersuite.google.com/app/apikey)

## Repository Setup

If setting up the repository from scratch, run the following commands:

```bash
echo "# FitBuddy" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/rishabh4uhh/FitBuddy.git
git push -u origin main
```

## Usage

1. **Run the application**:
   ```bash
   uvicorn app.main:app --reload
   ```

2. **Open your browser** and navigate to `http://127.0.0.1:8000`

3. **Generate a workout**:
   - Fill out the form with your details
   - Select your fitness goal and intensity level
   - Submit to receive your personalized workout plan

4. **Provide feedback** (optional):
   - After receiving your plan, you can submit feedback
   - The AI will refine the workout based on your input

5. **View all users** (admin feature):
   - Visit `/view-all-users` to see all stored user data

## API Endpoints

- `GET /` - Home page with input form
- `POST /generate-workout` - Generate new workout plan
- `POST /submit-feedback` - Update workout based on feedback
- `GET /view-all-users` - View all users (admin)

## Database Schema

The application uses a SQLite database with the following User model:

- `id`: Primary key
- `name`: User's name
- `age`: User's age
- `weight`: User's weight
- `goal`: Fitness goal (e.g., "weight loss", "muscle gain")
- `intensity`: Workout intensity ("beginner", "intermediate", "advanced")
- `original_plan`: Initial AI-generated workout plan
- `updated_plan`: Revised plan based on user feedback

## Configuration

The app uses the following Gemini AI models:
- Primary: `gemini-2.5-flash` for workout generation and updates
- Secondary: `gemini-2.5-flash` for nutrition tips

API quota handling includes:
- Exponential backoff retry logic
- Fallback to sample workout plans when quota exceeded
- Error handling for unexpected API failures

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer

This application is for informational purposes only and should not replace professional medical or fitness advice. Always consult with healthcare professionals before starting a new exercise program.


#TEAM MEMBERS

 Sanket Vishwakarma (Team Leader)
 Shaiendra Vishwakarma 
 Shashwat Sen
<<<<<<< HEAD
 Saransh Sahu# FitBuddy
# FitBuddy
=======
 Saransh Sahu
 # FitBuddy
>>>>>>> f56f17136f54943e55bc5513eceb11419b5d9f9a
