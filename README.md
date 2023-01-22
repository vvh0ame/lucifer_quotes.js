# lucifer_quotes.py
Web-API for [lucifer-quotes.vercel.app](https://lucifer-quotes.vercel.app) website which is simple API to retrieve some quotes of Lucifer

## Example
```python
import lucifer_quotes
lucifer_quotes = lucifer_quotes.LuciferQuotes()
random_quote = lucifer_quotes.get_random_quote()
print(random_quote)
```
