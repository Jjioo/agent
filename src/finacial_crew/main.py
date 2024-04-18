import os
from dotenv import load_dotenv
load_dotenv()

from crew import UniversityCrew
import time
import httpx

def run():
    inputs = {
        'uni_name': 'University of California, Berkeley',
    }
    retries = 3  # Number of retry attempts
    for attempt in range(retries):
        try:
            UniversityCrew().crew().kickoff(inputs=inputs)
            break  # If successful, exit the loop
        except httpx.RemoteProtocolError as e:
            print(f"Remote protocol error: {e}")
            print(f"Retrying after 5 seconds...")
            time.sleep(5)  # Wait for 5 seconds before retrying
        except Exception as e:
            print(f"Unexpected error: {e}")
            break  # Exit the loop on unexpected errors

if __name__ == '__main__':
    run()
