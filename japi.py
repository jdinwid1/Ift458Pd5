import urllib.request

def getStockData(symbol):
    apiKey = "N2IG8Q9WK1JZZ7U9"
    url = "https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={0}&apikey={1}".format(symbol, apiKey)
    connection = urllib.request.urlopen(url)
    responseString = connection.read().decode()
    print(responseString)

def __main__():
    while (True):
        answer = input("Enter a stock symbol or enter quit to quit:\n")
        if (answer.lower() == "quit"):
            break
        getStockData(answer)

if __name__ == "__main__":
    __main__();
