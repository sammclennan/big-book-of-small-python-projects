# Progress bar simulator

import random
import time

FILE_SIZE = 4098
PROGRESS_BAR_LENGTH = 40

downloaded_data = 0

while downloaded_data < FILE_SIZE:
    downloaded_data += random.randint(0, (FILE_SIZE // 50))
    downloaded_data = min(downloaded_data, FILE_SIZE)

    portion_downloaded = downloaded_data / FILE_SIZE

    # Draw progress bar
    print(f'\r[{'█' * round(portion_downloaded * PROGRESS_BAR_LENGTH)}{' ' * round((1 - portion_downloaded) * PROGRESS_BAR_LENGTH)}] {portion_downloaded:.2%} {downloaded_data}/{FILE_SIZE}', end='', flush=True)

    time.sleep(random.random())