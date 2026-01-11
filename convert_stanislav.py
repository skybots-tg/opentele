import asyncio
import sys
import os
import pathlib

# Add base dir to path 
base_dir = pathlib.Path(__file__).parent.absolute().__str__()
sys.path.insert(0, base_dir)

from src.td import TDesktop
from src.tl.telethon import TelegramClient
from src.api import API, UseCurrentSession

async def main():
    tdata_path = r"C:\Users\Dmitry\Desktop\Телеграмы\Telegram Stanislav #3 Stories\tdata"
    session_path = r"C:\Users\Dmitry\Desktop\Телеграмы\Telegram Stanislav #3 Stories\stanislav3"
    
    print(f"Loading tdata from: {tdata_path}")
    
    # Key file is "key_datas" which means key_data + s suffix, so keyFile="data" (default)
    tdesk = TDesktop(tdata_path)
    
    if not tdesk.isLoaded():
        print("Failed to load tdata!")
        return
    
    print(f"Loaded {tdesk.accountsCount} account(s)")
    
    # Convert to telethon session
    client = await tdesk.ToTelethon(
        session=session_path,
        flag=UseCurrentSession,
        api=API.TelegramDesktop
    )
    
    print(f"Session saved to: {session_path}.session")
    print("Done!")

if __name__ == "__main__":
    asyncio.run(main())
