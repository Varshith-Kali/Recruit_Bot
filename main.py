import requests
from bs4 import BeautifulSoup
import time  # Import the time module

def scrape_questions(job_description):
    # Construct the URL based on the job description
    url = f"https://www.indeed.com/q-{job_description.replace(' ', '-')}-jobs.html"

    # Define headers to mimic a browser request
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    # Send a GET request to the URL with headers
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all question elements
        question_elements = soup.find_all('div', class_='question')

        # Initialize a list to store questions
        questions = []

        # Iterate over question elements and extract the text
        for i, question_element in enumerate(question_elements):
            # Limit the number of questions to 11
            if i == 11:
                break
            # Extract text and append to the questions list
            questions.append(question_element.text.strip())

        return questions
    else:
        print("Failed to fetch questions. Status code:", response.status_code)
        return []

# Example usage
job_description = input("Enter the job description: ")
questions = scrape_questions(job_description)

# Display the scraped questions
if questions:
    print("Top 11 standard questions related to the job description:")
    for i, question in enumerate(questions, start=1):
        print(f"{i}. {question}")
else:
    print("No questions found for the given job description.")
