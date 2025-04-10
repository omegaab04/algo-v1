My first public trading algorithm. This took me too damn long. 

It includes cool features like news flashes on key issues in the world, risk controls, multiple strategies and a backtesting folder with key metrics that can be analysed for mathematical confidence. 

Not that you need to create, **at least**, a paper trading Alpaca API account in order to run this, as it depends on API keys and security codes that are unique to each user. 

**DO NOT PUSH YOUR UNIQUE API KEYS TO GITHUB IF YOU ARE A CONTRIBUTOR.**

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
