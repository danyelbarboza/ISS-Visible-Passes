# **ISS-Tracker-Weather** *(Development Preview)*  
*A minimal Python tool to fetch visible ISS passes with basic timezone conversion*

🔧 **Current State**: Core ISS pass-fetching functional | Weather integration pending  

---

## **Features Implemented**  
✅ Fetches ISS pass data from N2YO API  
✅ Converts UTC timestamps to local timezone  
✅ Configurable via `.env` file (latitude/longitude/API key)  
❌ Weather filtering (next phase)  

---

## **Tech Stack**  
- **Backend**: Python 3  
- **APIs**: [N2YO](https://www.n2yo.com/api/) (ISS orbital data)  
- **Libraries**: `requests`, `python-dotenv`  
- **Config**: Environment variables (`.env`)  

---

## **Quick Start**  
1. **Setup**  
   ```bash
   git clone https://github.com/yourusername/ISS-Tracker-Weather.git
   cd ISS-Tracker-Weather
   pip install requests python-dotenv
   ```

2. **Configure**  
   Create `.env` file:
   ```ini
   # .env.example
   latitude=YOUR_LAT
   longitude=YOUR_LON
   observer_alt=0
   API_KEY=your_n2yo_key
   gmt=-3  # Your GMT offset
   ```

3. **Run**  
   ```bash
   python ISS_whenever.py
   ```

---

## **Sample Output**  
```plaintext
Start: 25/04/2025 19:45, Duration: 360s
Start: 26/04/2025 05:22, Duration: 420s
```

## **Next Steps**  
➡️ Integrate OpenWeatherMap API  
➡️ Add city-to-coordinates conversion  
➡️ Build web interface (FastAPI/Flask)  

---

## License
MIT License - Available for use and modification. See the LICENSE file for details.