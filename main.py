import asyncio
import logging
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ChatMemberUpdated
from pyrogram.errors import ChatAdminRequired, UserAdminInvalid, FloodWait
from config import BOT_TOKEN, API_ID, API_HASH

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Initialize bot
app = Client("auto_kicker_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start") & filters.private)
async def start_command(client, message):
    user_name = message.from_user.first_name
    bot_username = (await client.get_me()).username
    
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Add to Channel", url=f"https://t.me/{bot_username}?startgroup=true&admin=ban_users")]
    ])
    
    welcome_text = f"""
👋 Hello {user_name}!

🤖 **Auto-Kicker Bot**
Auto-kicks users who leave your channel.

**How to use:**
1. Add me to your channel
2. Give me admin rights with 'Ban Users' permission
3. I'll automatically ban users who leave the channel

Powered by @AnnihilusOP
"""
    
    await message.reply_text(welcome_text, reply_markup=keyboard)

@app.on_message(filters.command("help"))
async def help_command(client, message):
    help_text = """
🆘 **Help - Auto-Kicker Bot**

**Commands:**
• /start - Start the bot
• /help - Show this help message

**Setup:**
1. Add bot to your channel
2. Promote bot as admin with 'Ban Users' permission
3. Bot will monitor and ban users who leave

**Note:** Bot must be admin to function properly.

Powered by @AnnihilusOP
"""
    await message.reply_text(help_text)

@app.on_chat_member_updated()
async def handle_member_update(client, chat_member_updated: ChatMemberUpdated):
    try:
        # Check if someone left the chat
        if (chat_member_updated.old_chat_member and 
            chat_member_updated.old_chat_member.status in ["member", "administrator", "creator"] and
            chat_member_updated.new_chat_member.status == "left"):
            
            user = chat_member_updated.new_chat_member.user
            chat = chat_member_updated.chat
            
            # Skip if user is bot or if it's the same bot
            if user.is_bot:
                return
                
            try:
                # Ban the user who left
                await client.ban_chat_member(chat.id, user.id)
                logger.info(f"Banned user {user.first_name} (@{user.username or 'N/A'}) [ID: {user.id}] from {chat.title}")
                
            except ChatAdminRequired:
                logger.warning(f"Bot is not admin in {chat.title}. Cannot ban users.")
                try:
                    await client.send_message(
                        chat.id, 
                        "⚠️ I need admin rights with 'Ban Users' permission to function properly!\n\nPowered by @AnnihilusOP"
                    )
                except:
                    pass
                    
            except UserAdminInvalid:
                logger.warning(f"Cannot ban admin user {user.first_name} in {chat.title}")
                
            except FloodWait as e:
                logger.warning(f"Rate limited. Waiting {e.value} seconds")
                await asyncio.sleep(e.value)
                
            except Exception as e:
                logger.error(f"Error banning user {user.id}: {str(e)}")
                
    except Exception as e:
        logger.error(f"Error in member update handler: {str(e)}")

@app.on_message(filters.new_chat_members)
async def bot_added_to_group(client, message):
    # Check if our bot was added
    bot_id = (await client.get_me()).id
    
    for new_member in message.new_chat_members:
        if new_member.id == bot_id:
            try:
                # Check if bot has admin rights
                bot_member = await client.get_chat_member(message.chat.id, bot_id)
                
                if bot_member.status != "administrator" or not bot_member.privileges.can_restrict_members:
                    await message.reply_text(
                        "⚠️ **Admin Rights Required**\n\n"
                        "Please promote me as admin with 'Ban Users' permission to start monitoring.\n\n"
                        "Powered by @AnnihilusOP"
                    )
                else:
                    await message.reply_text(
                        "✅ **Auto-Kicker Bot Activated**\n\n"
                        "I'm now monitoring this channel. Users who leave will be automatically banned.\n\n"
                        "Powered by @AnnihilusOP"
                    )
                    
            except Exception as e:
                logger.error(f"Error checking bot permissions: {str(e)}")
                await message.reply_text(
                    "⚠️ Please make me admin with 'Ban Users' permission.\n\nPowered by @AnnihilusOP"
                )

async def main():
    logger.info("Starting Auto-Kicker Bot...")
    await app.start()
    logger.info("Bot started successfully!")
    
    # Keep the bot running
    try:
        while True:
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        logger.info("Bot stopped")
    finally:
        await app.stop()

if __name__ == "__main__":
    asyncio.run(main())