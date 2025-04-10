My first public trading algorithm. This took me way too damn long.

It includes cool features like news flashes on key global issues, built-in risk controls, multiple trading strategies, and a full backtesting module with performance metrics you can analyse for mathematical confidence.

Note that you'll need to create, **at least**, a paper trading Alpaca API account to run this. The bot depends on API keys and security codes that are unique to each user.

# DO NOT PUSH YOUR UNIQUE API KEYS TO GITHUB IF YOU ARE A CONTRIBUTOR.

---

### Features

- Momentum and mean reversion strategies
- News-based risk override (Trump-focused at this moment in time; very eventful)
- Backtesting with performance metrics
- Live/paper trading execution with Alpaca API

---

### To run this locally:

Install via pip:

```bash
pip install -r requirements.txt
```

### Configuration

Set your keys in `.env`:

```
ALPACA_API_KEY=your_key
ALPACA_SECRET_KEY=your_secret
ALPACA_BASE_URL=https://paper-api.alpaca.markets
NEWS_API_KEY=your_newsapi_key
```

Strategy settings and symbols can be edited in:

- `config/settings.json`
- `config/symbols.json`

---

### Running the Algorithm

To run the strategy loop:

```bash
python main.py
```

To run in manual news-only mode, set `"manual_mode": true` in `settings.json`.

---

This project holds an MIT License.

---

Email me if you would like to collaborate: adam.bouchenaf23@gmail.com


