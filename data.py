import requests


# File created to get question from Application Programming Interface


NUMBER_OF_QUESTIONS = 10
DIFFICULTY = "easy"

parameters = {
    "amount": NUMBER_OF_QUESTIONS,
    "difficulty": DIFFICULTY,
    "type": "boolean",
}

questions_api_response = requests.get(
    url="https://opentdb.com/api.php", params=parameters
)
questions_api_response.raise_for_status()

questions_json = questions_api_response.json()

questions_data = questions_json["results"]
