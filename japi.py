import urllib.request
import json

def getStockData(symbol):
    apiKey = "N2IG8Q9WK1JZZ7U9"
    url = "https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={0}&apikey={1}".format(symbol, apiKey)
    connection = urllib.request.urlopen(url)
    responseString = connection.read().decode()
    data = json.loads(responseString)
    print(data['Global Quote']['05. price'])
    return data['Global Quote']['05. price']

def __main__():
    fileContents = []
    while (True):
        answer = input("Enter a stock symbol or enter quit to quit:\n")
        if (answer.lower() == "quit"):
            break
        fileContents.append("The current price of " + answer + " is: " + getStockData(answer))
    for contentLine in fileContents:
        f = open("japi.out", "a")
        f.write(contentLine + "\n")
        f.close()


if __name__ == "__main__":
    __main__();
