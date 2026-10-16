# HNS Historical Price Calculator

## Usage

1. Open a terminal and navigate to the folder. For example:
cd ~/Desktop/price-check-main (Adjust the path if your folder is somewhere else.)
2. Start the Python server
Run:
python3 server.py
3. Open your browser and visit:
 http://127.0.0.1:8000/

The calculator shows:
- Historical USD value of your HNS
- Historical BTC value of your HNS
- Average price per HNS on the selected date

## Technical Details

- Built with vanilla HTML, CSS, and JavaScript
- Uses high-precision arithmetic for accurate calculations
- Handles very small BTC values with custom formatting
- UTC date handling to ensure timezone consistency
