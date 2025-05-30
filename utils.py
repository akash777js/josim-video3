import random #JOSIM BOTS
import time #JOSIM BOTS
import math #JOSIM BOTS
import os #JOSIM BOTS
from vars import CREDIT #JOSIM BOTS
from pyrogram.errors import FloodWait #JOSIM BOTS
from datetime import datetime,timedelta #JOSIM BOTS

class Timer: #JOSIM BOTS
    def __init__(self, time_between=5): #JOSIM BOTS
        self.start_time = time.time() #JOSIM BOTS
        self.time_between = time_between #JOSIM BOTS

    def can_send(self): #JOSIM BOTS
        if time.time() > (self.start_time + self.time_between): #JOSIM BOTS
            self.start_time = time.time() #JOSIM BOTS
            return True #JOSIM BOTS
        return False #JOSIM BOTS

#lets do calculations #JOSIM BOTS
def hrb(value, digits= 2, delim= "", postfix=""): #JOSIM BOTS
    """Return a human-readable file size. #JOSIM BOTS
    """ #JOSIM BOTS
    if value is None: #JOSIM BOTS
        return None #JOSIM BOTS
    chosen_unit = "B" #JOSIM BOTS
    for unit in ("KB", "MB", "GB", "TB"): #JOSIM BOTS
        if value > 1000: #JOSIM BOTS
            value /= 1024 #JOSIM BOTS
            chosen_unit = unit #JOSIM BOTS
        else: #JOSIM BOTS
            break #JOSIM BOTS
    return f"{value:.{digits}f}" + delim + chosen_unit + postfix #JOSIM BOTS

def hrt(seconds, precision = 0): #JOSIM BOTS
    """Return a human-readable time delta as a string. #JOSIM BOTS
    """ #JOSIM BOTS
    pieces = [] #JOSIM BOTS
    value = timedelta(seconds=seconds) #JOSIM BOTS

    if value.days: #JOSIM BOTS
        pieces.append(f"{value.days}day") #JOSIM BOTS

    seconds = value.seconds #JOSIM BOTS

    if seconds >= 3600: #JOSIM BOTS
        hours = int(seconds / 3600) #JOSIM BOTS
        pieces.append(f"{hours}hr") #JOSIM BOTS
        seconds -= hours * 3600 #JOSIM BOTS

    if seconds >= 60: #JOSIM BOTS
        minutes = int(seconds / 60) #JOSIM BOTS
        pieces.append(f"{minutes}min") #JOSIM BOTS
        seconds -= minutes * 60 #JOSIM BOTS

    if seconds > 0 or not pieces: #JOSIM BOTS
        pieces.append(f"{seconds}sec") #JOSIM BOTS

    if not precision: #JOSIM BOTS
        return "".join(pieces) #JOSIM BOTS

    return "".join(pieces[:precision]) #JOSIM BOTS

timer = Timer() #JOSIM BOTS

async def progress_bar(current, total, reply, start): #JOSIM BOTS
    if timer.can_send(): #JOSIM BOTS
        now = time.time() #JOSIM BOTS
        diff = now - start #JOSIM BOTS
        if diff < 1: #JOSIM BOTS
            return #JOSIM BOTS
        else: #JOSIM BOTS
            perc = f"{current * 100 / total:.1f}%" #JOSIM BOTS
            elapsed_time = round(diff) #JOSIM BOTS
            speed = current / elapsed_time #JOSIM BOTS
            remaining_bytes = total - current #JOSIM BOTS
            if speed > 0: #JOSIM BOTS
                eta_seconds = remaining_bytes / speed #JOSIM BOTS
                eta = hrt(eta_seconds, precision=1) #JOSIM BOTS
            else: #JOSIM BOTS
                eta = "-" #JOSIM BOTS
            sp = str(hrb(speed)) + "/s" #JOSIM BOTS
            tot = hrb(total) #JOSIM BOTS
            cur = hrb(current) #JOSIM BOTS
            bar_length = 10 #JOSIM BOTS
            completed_length = int(current * bar_length / total) #JOSIM BOTS
            remaining_length = bar_length - completed_length #JOSIM BOTS

            symbol_pairs = [ #JOSIM BOTS
                ("▬", "▭"), #JOSIM BOTS
                ("✅", "☑️"), #JOSIM BOTS
                ("🐬", "🦈"), #JOSIM BOTS
                ("💚", "💛"), #JOSIM BOTS
                ("🌟", "⭐"), #JOSIM BOTS
                ("▰", "▱") #JOSIM BOTS
            ] #JOSIM BOTS
            chosen_pair = random.choice(symbol_pairs) #JOSIM BOTS
            completed_symbol, remaining_symbol = chosen_pair #JOSIM BOTS

            progress_bar = completed_symbol * completed_length + remaining_symbol * remaining_length #JOSIM BOTS

            try: #JOSIM BOTS
                await reply.edit(f'`╭──⌯═════𝐔𝐩𝐥𝐨𝐚𝐝𝐢𝐧𝐠══════⌯──╮\n├⚡ {progress_bar}\n├⚙️ Progress ➤ | {perc} |\n├🚀 Speed ➤ | {sp} |\n├📟 Processed ➤ | {cur} |\n├🧲 Size ➤ | {tot} |\n├🕑 ETA ➤ | {eta} |\n╰─═══✨🦋{CREDIT}🦋✨═══─╯`') 
                #await reply.edit(f'`╭──⌯═════𝐁𝐨𝐭 𝐒𝐭𝐚𝐭𝐢𝐜𝐬══════⌯──╮\n├⚡ {progress_bar}\n├⚙️ Progress ➤ | {perc} |\n├🚀 Speed ➤ | {sp} |\n├📟 Processed ➤ | {cur} |\n├🧲 Size ➤ | {tot} |\n├🕑 ETA ➤ | {eta} |\n╰─═══✨🦋JOSIM BOTS🦋✨═══─╯`') 
            except FloodWait as e: #JOSIM BOTS
                time.sleep(e.x) #JOSIM BOTS
