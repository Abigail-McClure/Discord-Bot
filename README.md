# Gif-Bot

A Discord bot that posts memes and gifs. Uses meme-api (reddit) with a Tenor GIF fallback.

## Features
- `$gif <query>` — search Tenor for GIFs
- `$meme` — tries meme-api, falls back to Tenor
- Non-blocking behavior via `asyncio.to_thread` (keeps bot responsive)
- Retries/fallbacks and safe error handling

## Prerequisites
- Python 3.8+ (3.10 or 3.11 recommended)  
- A Discord bot token (create an app at the [Discord Developer Portal](https://discord.com/developers/applications))
- A Tenor API key (get an API key in the Google Cloud Console)

## Set up:
### 1. Clone the repository
git clone https://github.com/Abigail-McClure/Discord-Bot.git
cd Discord-Bot

### 2. Create a virtual environment (recommended)
python -m venv venv\
source venv/bin/activate (for macOS / Linux)
or venv\Scripts\activate (for Windows PowerShell)

### 3. Install dependencies
pip install -r requirements.txt

### 4. Set up your environment in one of two ways:
#### Option 1 - Copy the example file:

cp .env.example .env

Then edit .env and fill in your keys:

DISCORD_TOKEN="your_discord_token_here"

TENOR_API_KEY="your_tenor_api_key_here"

#### Option 2 - Export directly in your terminal, run these commands:

export DISCORD_TOKEN="your_discord_token"

export TENOR_API_KEY="your_tenor_api_key"

(On Windows PowerShell, use $env:DISCORD_TOKEN = "token" instead.)

### 5. Run the bot
python bot.py

When the bot is online, you’ll see a message like:
Logged on as gif bot #1234!


## Commands Overview:
$meme	- Fetch a random meme (uses meme-api, falls back to Tenor) \
$gif \<search\> - Fetch a random Tenor GIF for a keyword \
$gif - Defaults to a random "meme" GIF

