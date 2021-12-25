import requests

url = "https://movie-database-imdb-alternative.p.rapidapi.com/"

querystring = {"r":"json","i":"tt4154796"}

headers = {
    'x-rapidapi-host': "movie-database-imdb-alternative.p.rapidapi.com",
    'x-rapidapi-key': "ba2be8c31fmsh1afcef5de6d0d7dp1319e5jsn00743b0ab332"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)