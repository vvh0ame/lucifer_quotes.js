from requests import get

class LuciferQuotes:
	def __init__(self) -> None:
		self.api = "https://lucifer-quotes.vercel.app/api"
		self.headers = {
			"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
		}

	def get_random_quote(self) -> dict:
		return get(
			f"{self.api}/quotes",
			headers=self.headers).json()

	def get_multiplte_quotes(
			self,
			count: int) -> list:
		return get(
			f"{self.api}/quotes/{count}",
			headers=self.headers).json()
