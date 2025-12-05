# 🌦️ Weather Oversight – Automated WhatsApp Weather Bot

![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-Free-green)
![Status](https://img.shields.io/badge/Status-Active-success)
![Platform](https://img.shields.io/badge/Platform-Windows-lightblue)
![API](https://img.shields.io/badge/API-Open--Meteo-orange)

Weather Oversight is a Python automation script that fetches real-time weather forecast data from **Open-Meteo** and sends a formatted weather update to a WhatsApp group using **pywhatkit**.

Designed to run automatically (via Task Scheduler), it reports the weather for the **next hour** in a clean WhatsApp message.

This script was made for fun and was made to be used only by me but I decided to uploaded just on the off chance that someone else needed this.

---

## ✨ Features

- 🔍 Hourly weather data:
  - Temperature  
  - Precipitation Probability  
  - Cloud Cover  
  - Rain Amount  
- 🌡️ Daily maximum temperature  
- ⏱️ Automatically calculates the next hour forecast  
- ⏰ Runs only between specific hours (default 09:00–23:00)  
- 📩 Sends formatted WhatsApp messages  
- 🌍 No API key required (Open-Meteo)

---

## 📦 Requirements

### Python  
- Python **3.8+**

### Install Dependencies  
``` bash
pip install requests pywhatkit
```

## ⚙️ Setup & Configuration

``` python
latitudeCord = 0.0000
longitudeCord = 0.0000
```
Replace with your latitude & longitude.

## Add your whatsapp group ID
``` python
groupId = "groupID"
```
### To find the group ID:
- You have to be admin
- Open WhatsApp Web
- Enter your group
- Check the URL → the long string after /t/ is the group ID

## Edit Allowed Runtime Hours (Optional)
``` python
if (currentHour >= 9) and (currentHour <= 23):
```
Modify these hours to your liking.
Remember it is for the next hour's data

## Automatic Execution
Windows Task Scheduler
Create a new task
Trigger: hourly
Action: run Python with script path

## 🧩 How It Works
- Checks if the script is allowed to run
- Fetches weather data from Open-Meteo
- Calculates the next hour timestamp
- Locates that timestamp in hourly data
- Prepares a formatted message
- Sends it automatically to your WhatsApp group

## ⚠️ Notes
- WhatsApp Web must remain logged in
- pywhatkit will briefly open a browser tab
- If your PC is slow, increase these values:
```python
waitTime = 34
closeTime = 30
```

## 🐞 Troubleshooting
| Problem              | Cause                        | Fix                           |
|----------------------|------------------------------|-------------------------------|
| `index == -1`        | Timestamp mismatch           | Keep `timezone="auto"`        |
| No message sent      | Wrong WhatsApp group ID      | Verify the ID from WhatsApp Web URL |
| Browser closes early | System is too slow           | Increase `waitTime` and `closeTime` |
| Script exits early   | Outside allowed run hours    | Edit `shouldProgramRun()`     |

## 📜 License

Free to use, modify, and distribute.
