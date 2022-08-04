#Thanks to Yukki @teamyukki

from typing import Dict, List, Union

from modules.core.mongo import mongodb


async def get_private_served_chats() -> list:
    chats_list = []
    async for chat in privatedb.find({"chat_id": {"$lt": 0}}):
        chats_list.append(chat)
    return chats_list

async def is_served_private_chat(chat_id: int) -> bool:
    chat = await privatedb.find_one({"chat_id": chat_id})
    if not chat:
        return False
    return True

async def add_private_chat(chat_id: int):
    is_served = await is_served_private_chat(chat_id)
    if is_served:
        return
    return await privatedb.insert_one({"chat_id": chat_id})

async def remove_private_chat(chat_id: int):
    is_served = await is_served_private_chat(chat_id)
    if not is_served:
        return
    return await privatedb.delete_one({"chat_id": chat_id})
