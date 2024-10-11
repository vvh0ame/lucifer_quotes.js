# lucifer_quotes.js
Web-API for [lucifer-quotes.vercel.app](https://lucifer-quotes.vercel.app) website which is simple API to retrieve some quotes of Lucifer

## Example
```JavaScript
async function main() {
	const { LuciferQuotes } = require("./lucifer_quotes.js")
	const luciferQuotes = new LuciferQuotes()
	const randomQuote = await luciferQuotes.getRandomQuote()
	console.log(randomQuote)
}

main()
```
