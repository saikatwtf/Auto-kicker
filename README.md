# Auto-Kicker Telegram Bot

A Telegram bot that automatically bans users who leave a connected channel.

## Features

- **Start Command**: Greets users and provides add-to-channel button
- **Auto Ban**: Automatically bans users who leave the monitored channel
- **Admin Checks**: Warns if bot lacks proper permissions
- **Error Handling**: Handles rate limits and permission errors
- **Logging**: Logs banned users for debugging

## Setup

### 1. Get Bot Credentials

1. Create a bot with [@BotFather](https://t.me/BotFather)
2. Get API credentials from [my.telegram.org](https://my.telegram.org)

### 2. Configure Bot

Set environment variables or edit `config.py`:
```bash
export BOT_TOKEN="your_bot_token_here"
export API_ID="12345678"
export API_HASH="your_api_hash_here"
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Bot

```bash
python main.py
```

## Deploy

### Deploy To Heroku
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/saikatwtf/Auto-kicker)

### Deploy To Koyeb
[![Deploy to Koyeb](https://www.koyeb.com/static/images/deploy/button.svg)](https://app.koyeb.com/deploy?type=git&repository=github.com/saikatwtf/Auto-kicker&branch=main&name=auto-kicker-bot)

### Deploy To Render
[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/saikatwtf/Auto-kicker)

### Deploy To VPS
```bash
git clone https://github.com/saikatwtf/Auto-kicker
cd Auto-kicker
pip install -r requirements.txt
export BOT_TOKEN="your_bot_token"
export API_ID="your_api_id"
export API_HASH="your_api_hash"
python main.py
```

## Manual Deployment

### Heroku
1. Fork this repository
2. Create new Heroku app
3. Connect GitHub repository
4. Set config vars: `BOT_TOKEN`, `API_ID`, `API_HASH`
5. Deploy

### Railway
1. Fork repository
2. Connect to Railway
3. Set environment variables
4. Deploy

### Render
1. Fork repository
2. Create new Web Service on Render
3. Connect repository
4. Set environment variables
5. Deploy

### Koyeb
1. Fork repository
2. Create new app on Koyeb
3. Connect GitHub repository
4. Set environment variables
5. Deploy

## Usage

1. Add bot to your channel
2. Promote bot as admin with "Ban Users" permission
3. Bot will automatically ban users who leave the channel

## Commands

- `/start` - Start the bot and get add-to-channel link
- `/help` - Show help information

## License

MIT License

---
Powered by @AnnihilusOP