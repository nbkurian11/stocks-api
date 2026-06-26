from flask import Flask, jsonify, render_template
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

API_KEY = os.getenv("ALPHA_VANTAGE_KEY")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/stock/<ticker>")
def get_stock(ticker):
    try:
        url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={ticker}&apikey={API_KEY}"
        response = requests.get(url)
        data = response.json()
        quote = data["Global Quote"]

        return jsonify({
            "ticker": ticker.upper(),
            "price": float(quote["05. price"]),
            "change": float(quote["09. change"]),
            "change_percent": float(quote["10. change percent"].replace("%", "")),
            "day_low": float(quote["04. low"]),
            "day_high": float(quote["03. high"])
        })

    except Exception as e:
        return jsonify({"error": "Invalid ticker or data unavailable"}), 404

if __name__ == "__main__":
    app.run(debug=True)