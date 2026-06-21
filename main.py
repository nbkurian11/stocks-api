import yfinance as yf


while True:

    t = input("Enter a ticker (or 'quit' to exit): ")

    if t.lower() == "quit":
        break


    tick = yf.Ticker(t)

    info = tick.info


    print(f"----{t.upper()}----")
    print(f"Price: ${info['currentPrice']:.2f}")

    change = info['regularMarketChange']

    if change >= 0:
        print(f"Change: +${change:.2f}")
    else:
        print(f"Change: -${abs(change):.2f}")

    changepercent = info['regularMarketChangePercent']

    if changepercent >= 0:
        print(f"Change Percent: +{changepercent:.2f}%")
    else:
        print(f"Change Percent: -{abs(changepercent):.2f}%")



    print(f"52 low: ${info['fiftyTwoWeekLow']:.2f}")
    print(f"52 high: ${info['fiftyTwoWeekHigh']:.2f}")




