import os
from dotenv import load_dotenv
load_dotenv()

from crew import UniversityCrew
def run():
    inputs = {
        'uni_name': 'University of California, Berkeley',
    }
    UniversityCrew().crew().kickoff(inputs = inputs)

if __name__ == '__main__':
    run()