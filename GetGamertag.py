import requests
class Checker:
    def __init__(self,gamertag) -> None:
        self.gamertag = gamertag
        self.url = "https://playerdb.co/api/player/xbox/"
        self.data = None
        self.headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"}

    def GetData(self,gamertag):
        base_url = f'{self.url}{self.gamertag}'
        response = requests.get(base_url, headers=self.headers)
        if response.status_code == 200:
            self.data = response.json()
            return self.data  
        else:
            self.data = response.json()
            return self.data 
         
    def GetAvailabiltity(self,gamertag):
        if self.data["code"] == "player.found":
            status = "is currently unavailable"
        elif self.data["code"] == "xbox.bad_response_code":
            status = "is available"
        return status