import time
from datetime import datetime


current = time.time()
formatted = datetime.fromtimestamp(current).strftime("%B %d %Y")

print(
    "Seconds since January 1, 1970: 1,666,355,857.3622 "
    "or 1.67e+09 in scientific notation"
)
print(formatted)
