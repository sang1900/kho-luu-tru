from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from bot import Bot
from config import ADMINS
from helper_func import encode, get_message_id
import requests

@Bot.on_message(filters.private & filters.command('batch'))
async def batch(client: Client, message: Message):
    while True:
        try:
            first_message = await client.ask(text = "Chuyển tiếp tin nhắn hoặc link đầu tiên trong khoảng bạn muốn lưu trữ từ kênh Database (có trích dẫn)\nVD: Bạn muốn lưu từ tin nhắn 1 đến tin nhắn 10 thì : \n<b>Tin nhắn/link đầu tiên</b> : là tin nhắn/link của tin nhắn số 1", chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
        except:
            return
        f_msg_id = await get_message_id(client, first_message)
        if f_msg_id:
            break
        else:
            await first_message.reply("❌ Lỗi \n Bài viết được chuyển tiếp này không phải từ Kênh DB của tôi hoặc Liên kết này được lấy từ Kênh DB", quote = True)
            continue

    while True:
        try:
            second_message = await client.ask(text = "Chuyển tiếp tin nhắn hoặc link đầu tiên trong khoảng bạn muốn lưu trữ từ kênh Database (có trích dẫn)\nVD: Bạn muốn lưu từ tin nhắn 1 đến tin nhắn 10 thì : \n<b>Tin nhắn/link cuối cùng</b> : là tin nhắn/link của tin nhắn số 10", chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
        except:
            return
        s_msg_id = await get_message_id(client, second_message)
        if s_msg_id:
            break
        else:
            await second_message.reply("❌ Lỗi \n Bài đăng được chuyển tiếp này không phải từ Kênh Database của tôi hoặc Liên kết này được lấy từ Kênh DB", quote = True)
            continue


    string = f"get-{f_msg_id * abs(client.db_channel.id)}-{s_msg_id * abs(client.db_channel.id)}"
    base64_string = await encode(string)
    link = f"https://t.me/{client.username}?start={base64_string}"
    url = f"https://link1s.com/api?api=9e9c26d7a2a2759289d9f95c84931a0471da7243&url={link}"
    link1s = requests.get(url).json()["shortenedUrl"]
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("🔁 Share URL", url=f'https://telegram.me/share/url?url={link1s}')]])
    await second_message.reply_text(f"✅ Lưu Trữ Thành Công\n<b>🔗 Your URL : </b>{link1s}\n\n(Vì đây là bản free nên cần mở link rút gọn để lấy link lưu trữ, liên hệ <a href='https://facebook.com/sang1900>Admin</a> để xoá link rút gọn)", quote=True, reply_markup=reply_markup)


@Bot.on_message(filters.private & filters.command('genlink'))
async def link_generator(client: Client, message: Message):
    while True:
        try:
            channel_message = await client.ask(text = "Chuyển tiếp tin nhắn từ Kênh Database (có Trích dẫn) hoặc Gửi liên kết Bài đăng trên Kênh DB", chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
        except:
            return
        msg_id = await get_message_id(client, channel_message)
        if msg_id:
            break
        else:
            await channel_message.reply("❌ Lỗi Bài viết được chuyển tiếp này không phải từ Kênh Database của tôi hoặc Liên kết này không được lấy từ Kênh DB", quote = True)
            continue

    base64_string = await encode(f"get-{msg_id * abs(client.db_channel.id)}")
    link = f"https://t.me/{client.username}?start={base64_string}"
    url = f"https://link1s.com/api?api=9e9c26d7a2a2759289d9f95c84931a0471da7243&url={link}"
    link1s = requests.get(url).json()["shortenedUrl"]
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("🔁 Chia sẻ URL", url=f'https://telegram.me/share/url?url={link1s}')]])
    await channel_message.reply_text(f"✅ Lưu Trữ Thành Công\n<b>🔗 Your URL : </b>{link1s}\n\n(Vì đây là bản free nên cần mở link rút gọn để lấy link lưu trữ, liên hệ <a href='https://facebook.com/sang1900>Admin</a> để xoá link rút gọn)", quote=True, reply_markup=reply_markup)
