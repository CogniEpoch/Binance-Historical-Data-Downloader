# Binance Historical Data Downloader


This Python script allows you to download historical data for any cryptocurrency (for example: BTC-USDT) trading pair from Binance at different time frames.

## Usage

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/CogniEpoch/Binance-Historical-Data-Downloader.git


## Usage

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/CogniEpoch/Binance-Historical-Data-Downloader.git

2. Install the required dependencies:
   ```bash
   pip install requests 

3. Update the script with your desired date range, download directory, and time frame.

4. Run the script:
    ```bash
    python binance_data_downloader.py

> [!NOTE]
>  Parameters:
>    - start_date: The start date for downloading historical data.
>    - end_date: The end date for downloading historical data.
>    - download_directory: The directory where the downloaded data will be saved.
>    - Time_frame: The time frame for historical data (e.g., 1s, 1m, 1h). Check the available time frames on the official Binance website.
# **Example**:
**Define the start date and end date :**

    start_date = date(2018, 3, 5)
    end_date = date(year, month, day)

**Specify the download directory :**

    download_directory = '/content/'

**Specify the time frame (e.g., 1s, 1m, 1h) :**

    Time_frame = '1s'
    
> [!IMPORTANT]
> Ensure that you have a stable internet connection.
> 
> The script downloads data at the specified time frame for each day in the specified date range.

> [!TIP]
> You can change the BTCUSDT to your favored coin with correct format from offical website, and if available, it will download.

> [!CAUTION]
>  # Disclaimer
>  This script is for educational purposes only. Use it responsibly and in accordance with Binance's terms of use.
