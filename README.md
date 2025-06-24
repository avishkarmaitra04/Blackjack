<p align="center">
  <img src="https://img.shields.io/badge/Author-Avishkar%20Maitra-blue?style=flat-square" />
  <img src="https://img.shields.io/badge/Python-3.8+-yellow?style=flat-square&logo=python" />
  <img src="https://img.shields.io/github/license/avishkarmaitra04/blackjack-python?style=flat-square" />
</p>

# 🃏 Blackjack CLI Game (Python)

A command-line Blackjack game written in Python by [@avishkarmaitra04](https://github.com/avishkarmaitra04). This version features betting, insurance, double down, and split hand logic — all playable in the terminal!
## 🚀 Features

- 💰 Betting system with balance tracking
- 🛡 Insurance option when dealer shows Ace
- 💥 Double down (only on first turn)
- ✂️ Split hands when dealt a pair
- 🧠 Dealer logic that hits below 17
- 📊 Stats tracking (Wins / Losses / Pushes)
- 🔁 Continuous play until balance reaches ₹0

## ▶️ How to Play 

- Start the game in your terminal.
- You begin with ₹1000 balance.
- Enter your bet using chip-style amounts or full value.
- Choose actions:
  - Hit: Take another card
  - Stand: End your turn
  - Double Down: Double bet + one card (only 1st turn)
  - Split: Split if dealt a pair
  - Insurance: Available when dealer shows Ace
- Win/lose/draw affects balance and stats.
- The game ends when you're out of money or exit manually.

## 🌐 Future Plans

- 🔁 Flask Web Version (in progress)
- 🎨 Styling and animations
- 🧑‍🤝‍🧑 Multiplayer support
- ☁️ Online deployment

## 🤝 Contributions
Suggestions, issues, or forks are welcome!
Let’s make Blackjack smarter and cleaner together.

## 📦 Requirements

No libraries needed — just run with Python 3:

```bash
python blackjack.py
