import httpx 
from typing import List, Dict
import asyncio

async def fetch_jokes(amount: int = 100) -> List[Dict]:
    jokes = []
    async with httpx.AsyncClient() as client:
        # Fetch jokes in batches of 10 (JokeAPI limit)
        for i in range(0, amount, 10):
            batch_size = min(10, amount - i)
            response = await client.get(
                f"https://v2.jokeapi.dev/joke/Any?amount={batch_size}"
            )
            if response.status_code == 200:
                data = response.json()
                jokes.extend(data['jokes'])
    
    return jokes

def process_joke(joke_data: Dict) -> Dict:
    processed_joke = {
        "category": joke_data["category"],
        "joke_type": joke_data["type"],
        "joke": joke_data.get("joke") if joke_data["type"] == "single" else None,
        "setup": joke_data.get("setup") if joke_data["type"] == "twopart" else None,
        "delivery": joke_data.get("delivery") if joke_data["type"] == "twopart" else None,
        "nsfw": joke_data["flags"]["nsfw"],
        "political": joke_data["flags"]["political"],
        "sexist": joke_data["flags"]["sexist"],
        "safe": joke_data["safe"],
        "lang": joke_data["lang"]
    }
    return processed_joke