from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters, CallbackContext


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f"/calc +, -, *, /")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(update.message.text)


async def calculator(update: Update, context: CallbackContext):
    msg = update.message.text
    data = msg[5:]
    if '+' in data:
        num1, num2 = data.split('+')
        msg = int(num1) + int(num2)
    if '-' in data:
        num1, num2 = data.split('-')
        msg = int(num1) - int(num2)
    if '*' in data:
        num1, num2 = data.split('*')
        msg = int(num1) * int(num2)
    if '/' in data:
        num1, num2 = data.split('/')
        msg = int(num1) / int(num2)
    await update.message.reply_text(f'Результат  {msg}')
