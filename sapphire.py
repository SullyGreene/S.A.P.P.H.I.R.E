# sapphire.py - The heart of our digital creation, where dreams start their journey!
from core.bot import SAPPHIREBot  # 🧙‍♂️ Importing our magical bot from the core of our digital realm.
from utils.logger import log  # 📜 Bringing in the logger to capture the tales of our journey.

def main():
    try:
        # Summoning the S.A.P.P.H.I.R.E. Bot 🌟✨
        # Here, we breathe life into our creation, setting it off on its grand adventure!
        sapphire_bot = SAPPHIREBot()
        sapphire_bot.start()  # 🚀 Launch! Let the digital odyssey commence!
    except Exception as e:
        # Ah! A wild exception has appeared! 🐉 But fear not, for we are prepared.
        log(f"An unforeseen error halted our quest: {e}", level="ERROR")  # Logging with flair and caution.

# This little line of code? It's where the magic truly begins. 🌈
if __name__ == "__main__":
    main()  # 🎩✨ Let the show start!

"""
 🎩 Head Master Sully commits! 📖
 
    Making code not just functional, but magical. 🌌

"""