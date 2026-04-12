# 📡 Network Bandwidth Analyzer

## 📌 Overview

Network Bandwidth Analyzer is a simple Python-based tool that monitors real-time network bandwidth usage. It displays upload and download speeds at regular intervals, helping users understand their network activity.

---

## 🚀 Features
`
* 📊 Real-time bandwidth monitoring
* 📈 Displays upload and download speed per second
* ⚡ Lightweight and fast
* 🖥️ Works directly from the terminal
* ⏱️ Customizable monitoring interval

---

## 🛠️ Technologies Used

* Python
* psutil (for accessing system and network statistics)

---

## 📦 Installation

1. Clone the repository:

```bash
git clone https://github.com/NaveenMaurya1/Network-Bandwidth-Analyzer.git
```

2. Navigate to the project directory:

```bash
cd Network-Bandwidth-Analyzer
```

3. Install dependencies:

```bash
pip install psutil
```

---

## ▶️ Usage

Run the script:

```bash
python main.py
```

You will see output like:

```
Upload Speed: 15.20 KB/s | Download Speed: 120.45 KB/s
```

Press **Ctrl + C** to stop monitoring.

---

## ⚙️ How It Works

* Uses `psutil.net_io_counters()` to fetch network statistics
* Calculates the difference in bytes sent and received over time
* Converts bytes into human-readable format (KB, MB, etc.)
* Displays real-time upload and download speeds

---

## 📁 Project Structure

```
Network-Bandwidth-Analyzer/
│── main.py
│── README.md
```

---

## 🔮 Future Improvements

* Add graphical interface (GUI)
* Log bandwidth usage to a file
* Show historical data and charts
* Add alerts for high bandwidth usage

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

---

## 📄 License

This project is open-source and available under the MIT License.

---

## 🙌 Acknowledgements

* psutil library for system monitoring
* Python community

---

## ⭐ Support

If you found this project helpful, please give it a ⭐ on GitHub!
