from flask import Flask, jsonify

import yfinance as yf

app = Flask(__name__)

@app.route("/stock/<ticker>")

def get_stock(ticker):

    try:
        tick = yf.Ticker(ticker)
        info = tick.info


        return jsonify({
            "ticker": ticker.upper(),
            "currency": info["currency"],
            "price": info["currentPrice"],
            "price": info["currentPrice"],
            "change": info["regularMarketChange"],
            "change_percent": info["regularMarketChangePercent"],
            "52w_low": info["fiftyTwoWeekLow"],
            "52w_high": info["fiftyTwoWeekHigh"]
        })
    except KeyError:
        return jsonify({"error": "Invalid ticker symbol"}), 404



if __name__ == "__main__":
    app.run(debug=True)