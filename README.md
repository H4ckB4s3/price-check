# HNS Historical Price Calculator

A web-based tool to calculate the historical USD value of Handshake (HNS) tokens since February 13, 2020. The calculator uses precise average price calculations to provide accurate historical valuations.

## Features

- 📅 Date picker with calendar interface
- 💰 Real-time HNS price display
- 📊 Precise average price calculations
- 💵 USD and BTC value conversions
- 📱 Responsive design
- 🎨 Clean, dark theme UI

## Dependencies

This project relies on two external services:

1. **Price API**: [`https://price.hns.dev/`](https://price.hns.dev/)
   - Provides current and historical HNS price data
   - Used endpoints:
     - `/latest` - Current price
     - `/historical?from={date}&currency={usd|btc}` - Historical prices

2. **CORS Proxy**: [`https://corsproxy.io/`](https://corsproxy.io/)
   - Enables cross-origin requests to the price API
   - Required due to browser CORS restrictions

## Usage

1. Select a date using the calendar picker
2. Enter the amount of HNS tokens
3. Click "Check Historical Price in USD"
4. View the calculated USD and BTC values

The calculator shows:
- Historical USD value of your HNS
- Historical BTC value of your HNS
- Average price per HNS on the selected date

## Technical Details

- Built with vanilla HTML, CSS, and JavaScript
- Uses high-precision arithmetic for accurate calculations
- Handles very small BTC values with custom formatting
- UTC date handling to ensure timezone consistency
