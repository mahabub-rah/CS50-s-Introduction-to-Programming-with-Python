import argparse, sys, requests

parser = argparse.ArgumentParser(exit_on_error=False)
parser.add_argument('number')
try:
    args = parser.parse_args()
    num = float(args.number)
except argparse.ArgumentError:
    sys.exit('Missing command-line argument')
except ValueError:
    sys.exit('Command-line argument is not a number')


try:
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=54894533ffcc7e5099f8fec9e85203f130f4030da041cc64091bac9c95504a53")
    data = response.json()["data"]
    amount = num * float(data["priceUsd"])
    print(f"${amount:,.4f}")

except requests.RequestException:
    sys.exit("Error fetching data")

