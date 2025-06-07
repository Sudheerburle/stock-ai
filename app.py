import streamlit as st
import yfinance as yf

st.set_page_config(page_title="Stock AI", layout="centered")

st.title("📈 Stock Recommendation AI")
stock = st.text_input("Enter Stock Symbol (e.g., RELIANCE.NS)", "RELIANCE.NS")

if stock:
    data = yf.download(stock, period="6mo")
    if not data.empty:
        data['SMA_20'] = data['Close'].rolling(window=20).mean()
        data['SMA_50'] = data['Close'].rolling(window=50).mean()

        latest_price = data['Close'].iloc[-1]
        sma_20 = data['SMA_20'].iloc[-1]
        sma_50 = data['SMA_50'].iloc[-1]

        st.write(f"Latest Price: ₹{latest_price:.2f}")
        st.write(f"SMA 20: ₹{sma_20:.2f} | SMA 50: ₹{sma_50:.2f}")

        if sma_20 > sma_50:
            st.success("Recommendation: ✅ BUY")
        else:
            st.warning("Recommendation: ⚠️ SELL or HOLD")
    else:
        st.error("Invalid stock symbol or no data.")
