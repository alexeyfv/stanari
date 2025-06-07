# Stanari

![Streamlit](https://img.shields.io/badge/Streamlit-%E2%9C%94%EF%B8%8F-success?logo=streamlit)
![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)
![Python](https://img.shields.io/badge/Python-3.13%2B-blue?logo=python)

**Stanari** is a multilingual interactive dashboard for exploring and analyzing rental market trends in Serbia.

🔗 **Dashboard**: [stanari.streamlit.app](https://stanari.streamlit.app)

💬 **Telegram**: [@stanari_app](https://t.me/stanari_app)

## ✨ Features

- 📊 Track rental prices by district.
- 🏠 Compare prices by apartment size (rooms).
- 📈 Explore price trends over time.
- 🌍 Multilingual interface: Serbian, Russian, English.

## 🚀 Run Locally

Clone the repository and install dependencies:

``` sh
git clone https://github.com/alexeyfv/stanari.git
cd stanari

uv venv
uv sync
```

Compile translations (required for multilingual interface):

``` sh
cd locales
mo.sh
```

Run the app:

``` sh
uv run streamlit run app.py
```

Then open http://localhost:8501 in your browser.

## 🤝 Contributing

Contributions, ideas, and feedback are welcome!
Feel free to open an issue or a pull request.

## 📄 License

This project is licensed under the [GNU GPL v3.0](./LICENSE)
