import urllib.request

goog_url = 'https://query1.finance.yahoo.com/v7/finance/download/GOOG?period1=1499195379&period2=1501873779&interval=1d&events=history&crumb=6WnYdqoZOpG'

def download_stock_data(csv_url):
    response = urllib.request.urlopen(csv_url)
    csv = response.read()
    csv_srt = str(csv)
    lines = csv_srt.split("\\n")
    dest_url = r'goog.csv'
    fx = open(dest_url, "w")
    for line in lines:
        fx.write(line + "\n")
    fx.close()

download_stock_data(goog_url)