
mode: enforce

agents:
  default:
    allowed_tools: []
    max_calls_per_minute: 10

  trading_agent:
    allowed_tools:
      - binance_spot
      - binance_futures
    max_calls_per_minute: 20
