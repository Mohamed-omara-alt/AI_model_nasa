# Space Weather AI and Solar Defender Game

This repository contains two Python-based projects powered by NASA data, focused on space weather monitoring and education. The projects aim to provide real-time insights into solar activity and an interactive learning experience for kids and youth.

- **Nasa.py**: A real-time solar storm prediction system that fetches solar flare data from NASA's DONKI API, processes it, generates impact reports, and creates stunning visualizations.
- **NASA_geam.py**: An interactive educational game ("Solar Defender") designed for the NASA Space Apps Challenge, where players defend Earth from solar flares while learning about space weather.

These projects demonstrate the use of AI, data visualization, and gamification to make space science accessible and engaging.

## Features

### Nasa.py (Space Weather AI)
- Fetches real-time solar flare data from NASA API (or uses simulated data as fallback).
- Processes flare data to predict impacts on Earth (e.g., power grids, satellites, communications).
- Generates a detailed cosmic weather report with risk assessments and recommendations.
- Creates a comprehensive visualization dashboard including:
  - Solar activity spectrum (bar chart).
  - Real-time impact radar.
  - Risk meter.
  - Cosmic event timeline.
  - Magnetic storm simulation.
  - Planetary impact map.
- Uses emojis and colorful outputs for an engaging console experience.

### NASA_geam.py (Solar Defender Game)
- Interactive game where players act as "Space Commanders" to protect Earth from solar flares.
- Fetches real NASA data or uses simulations for flare events.
- Player choices affect Earth's systems (power grid, satellites, communications).
- Educational facts about space weather integrated throughout the game.
- Post-game mission analysis with enhanced visualizations:
  - Flare distribution pie chart.
  - Intensity timeline.
  - Earth systems status bars.
  - Impact comparison.
  - Performance gauge.
  - Planetary impact map.
  - Mission log.
- Saves a high-resolution report image (`solar_defender_report.png`).

## Requirements

- Python 3.12+ (tested on Python 3.12.3).
- Required libraries (install via `pip`):
  ```
  pip install requests matplotlib numpy pandas
  ```
- No additional installations needed for basic functionality. The scripts handle API keys (using NASA's demo key by default).

Note: Internet access is required for real NASA data fetching. If offline, the scripts fall back to simulated data.

## Usage

### Running Nasa.py
```
python Nasa.py
```
- The script will connect to NASA (or simulate), fetch/process data, display a report, and show visualizations.
- Output includes console reports and a matplotlib dashboard.

### Running NASA_geam.py
```
python NASA_geam.py
```
- Follow the prompts to enter your name and make choices during the game.
- After completing missions, view the final results, educational facts, and visualization dashboard.
- A PNG report is saved automatically.

## Example Output

### Nasa.py
```
🌌🌌🌌... (loading animation)
🚀 SPACE WEATHER AI: REAL-TIME SOLAR STORM PREDICTION SYSTEM 🚀
...
📡 CAPTURED COSMIC EVENTS:
...
✨ COSMIC WEATHER INTELLIGENCE REPORT
...
(Visualizations appear in a new window)
```

### NASA_geam.py
```
🚀 SOLAR DEFENDER: Interactive Space Weather Adventure 🚀
...
What's your name, Space Commander? 👉 [Your Name]
...
Incoming Solar Flare: X1.3
Choose defense strategy: 1-4
...
(Mission results and visualizations)
```

## Contributing

Contributions are welcome! Feel free to:
- Fork the repository.
- Create a new branch for your feature/bugfix.
- Submit a pull request with a clear description.

Please ensure code follows PEP 8 style and includes comments.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Powered by [NASA's DONKI API](https://api.nasa.gov/).
- Inspired by space weather science and educational outreach.
- Built with open-source libraries like Matplotlib, NumPy, and Pandas.

For questions or suggestions, contact [your email or GitHub profile]. Enjoy exploring space weather! 🌌🚀
