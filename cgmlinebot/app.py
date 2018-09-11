from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    SourceUser
)

import os

app = Flask(__name__)

line_bot_api = LineBotApi('wVVeWkYUbXO8Wgggzc0Ln2hPftw17YbLvyapHNYIPDDknV6CqWr19DE4O91uyRPW3v0SX3gNjm/PlDa9qYO3vyASUnK299WweU1zyCXYJJBW35ABPSygvbTo65LZjvkiG6fCz8lKWkBRSEdUbFWRtwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('e8c0f7a3550a6b7053a7f4bc362e7493')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):

    showMsg = ''
    recvMsg = event.message.text

    if recvMsg == 'profile':
        if isinstance(event.source, SourceUser):
            profile = line_bot_api.get_profile(event.source.user_id)
            line_bot_api.reply_message(
                event.reply_token, [
                    TextSendMessage(text='Display name: ' + profile.display_name),
                    TextSendMessage(text='Status message: ' + profile.status_message)
                ]
            )
        else:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="Bot can't use profile API without user ID"))
    elif recvMsg.upper() == "HI".upper():
        showMsg = "Who are you?"
    elif recvMsg.upper() == 'HUEI'.upper():
        showMsg = "Tonight's moon is beautiful"
    else:
        showMsg = "Hi, " + recvMsg 

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=showMsg))


if __name__ == "__main__":
    port = int(os.environ.get('PORT',5000))
    app.run(host='0.0.0.0', port=port)
