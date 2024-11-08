from flask import Flask, render_template
import json
import random
import requests

app = Flask(__name__)

def get_meme():
    url = "https://meme-api.com/gimme"
    try:
        response = requests.get(url)
        # Print response details for debugging
        print(f"Status Code: {response.status_code}")
        print(f"Response Text: {response.text}")
        
        if response.status_code == 200:
            data = response.json()
            meme_large = data["preview"][-2]
            subreddit = data["subreddit"]
            return meme_large, subreddit
        else:
            # Return a fallback or default values if the API fails
            return "https://via.placeholder.com/400x300?text=Meme+Unavailable", "Error"
            
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return "https://via.placeholder.com/400x300?text=Meme+Unavailable", "Error"
    except json.JSONDecodeError as e:
        print(f"JSON decode error: {e}")
        return "https://via.placeholder.com/400x300?text=Meme+Unavailable", "Error"

@app.route("/")
def index():
    memepic, subreddit = get_meme()
    return render_template("meme_index.html", meme_pic=memepic, subreddit=subreddit)

if __name__ == "__main__":
    # Running on port 5000
    app.run(host="0.0.0.0", port=5000, debug=True)  # Added debug=True for more information
