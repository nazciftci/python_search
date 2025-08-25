import re
from colorama import Fore, Style

def highlight(sentence: str, keyword: str) -> str:
    pat = re.compile(re.escape(keyword), re.IGNORECASE)
    return pat.sub(lambda m: Fore.RED + Style.BRIGHT + m.group(0) + Style.RESET_ALL, sentence)
##aranan kelimeyi renklendiriyor.