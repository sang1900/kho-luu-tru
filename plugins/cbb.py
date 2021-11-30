from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>Bot được tạo bởi <a href='https://t.me/trumlinknong'>Trùm Link Nóng</a>\nGiới thiệu :</b> Đây là một con bot Telegram được tạo ra nhằm mục đích lưu trữ thông tin/tệp/file/tin nhắn/video/hình ảnh hoàn toàn miễn phí.\n\n<b>CÁC PHIÊN BẢN CỦA BOT\n Phiên Bản Free : </b>Lưu trữ không giới hạn, khi lấy link chia sẻ/link lữu trữ cần vượt link rút gọn.\n<b>Phiên Bản Plus : </b> Lưu trữ không giới hạn, xoả bỏ link rút gọn <b>(15k/tháng)</b>\n<b>Phiên Bản Premium : </b> Lưu trữ không giới hạn, xoá link rút gọn, tự quản lý bot, sửa tin nhắn chào mừng khi /start, kéo member vào group/channel khi có người muốn truy cập link lưu trữ, có tự quản lý các tệp/file đã lưu trữ không lo mất link khi xoá tin nhắn <b>(30k/tháng)</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("❌ Đóng", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
