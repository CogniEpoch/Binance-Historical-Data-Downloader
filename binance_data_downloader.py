import requests
from datetime import date, timedelta

def download_binance_data(start_date, end_date, download_directory,Time_frame):
    link_prefix = f.'BTCUSDT-{Time_frame}-'
    link_suffix = '.zip'
    delta = timedelta(days=1)

    while start_date <= end_date:
        current_date = start_date.strftime('%Y-%m-%d')
        url = f'https://data.binance.vision/data/spot/daily/klines/BTCUSDT/{Time_frame}/{link_prefix}{current_date}{link_suffix}'
        filename = f'{link_prefix}{current_date}{link_suffix}'
        filepath = f'{download_directory}/{filename}'

        response = requests.get(url)
        
        # Check if the request was successful before writing the file
        if response.status_code == 200:
            with open(filepath, 'wb') as file:
                file.write(response.content)
            print(f'{filename} downloaded successfully!\n')
        else:
            print(f'Failed to download {filename}. Status code: {response.status_code}\n')

        start_date += delta

    print('All downloads completed successfully!')

# Define the start date and end date
start_date = date(year, month, day)
end_date = date(year, month, day)

# Specify the download directory
download_directory = '/content/'

# Specify the time frame, you can check the time frames on offical website
Time_frame = 1s

# Call the download function
download_binance_data(start_date, end_date, download_directory,Time_frame)
