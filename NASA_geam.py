import requests
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import time
import warnings
from matplotlib.patches import Circle, Wedge, Rectangle
import matplotlib.patches as mpatches

warnings.filterwarnings('ignore')

# Professional design settings
plt.style.use('dark_background')
plt.rcParams['font.size'] = 11
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['axes.titlesize'] = 14

print("🌌" * 60)
print("🚀 SOLAR DEFENDER: Interactive Space Weather Adventure 🚀")
print("🌌" * 60)
print("🌟 NASA Space Apps Challenge - Educational Game for Kids & Youth 🌟")
print()


class EnhancedSolarDefenderGame:
    def __init__(self):
        self.player_name = ""
        self.score = 0
        self.earth_health = 100
        self.power_grid = 100
        self.satellites = 100
        self.communications = 100
        self.solar_data = None
        self.api_key = 'DEMO_KEY'
        self.mission_history = []
        
        # Professional colors
        self.colors = {
            'excellent': '#00ff88',
            'good': '#66ff66',
            'warning': '#ffcc00',
            'danger': '#ff6600',
            'critical': '#ff0044',
            'info': '#00ffff'
        }

    def welcome_animation(self):
        """Special welcome message"""
        print("\n" + "✨" * 50)
        print("🎮 Welcome to Solar Defender Game! 🎮")
        print("✨" * 50)
        time.sleep(1)

        for i in range(3):
            print(f"\r🚀 Starting mission in {3 - i}...", end="")
            time.sleep(1)
        print("\r🎯 Mission started! Ready to protect Earth! 🌍        ")

    def get_player_info(self):
        """Get player information"""
        print("\n" + "👨‍🚀" * 20)
        self.player_name = input("What's your name, Space Commander? 👉 ")
        print(f"Welcome Commander {self.player_name}! Your mission: Protect Earth from solar storms!")

    def fetch_solar_data(self):
        """Fetch solar data from NASA"""
        print("\n📡 Connecting to NASA satellites...")

        try:
            url = "https://api.nasa.gov/DONKI/FLR"
            params = {
                'startDate': (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d'),
                'endDate': datetime.now().strftime('%Y-%m-%d'),
                'api_key': self.api_key
            }

            response = requests.get(url, params=params, timeout=10)

            if response.status_code == 200:
                data = response.json()
                if data:
                    self.solar_data = self.process_real_data(data)
                    print("✅ Received real data from NASA!")
                    return True

            print("🔄 Using advanced simulation data...")
            self.solar_data = self.create_simulation_data()
            return True

        except Exception as e:
            print("🎮 Switching to game simulation mode...")
            self.solar_data = self.create_simulation_data()
            return True

    def process_real_data(self, data):
        """Process real NASA data"""
        processed = []
        for flare in data[:7]:
            processed.append({
                'id': flare.get('flareID', 'Unknown'),
                'class': flare.get('classType', 'B1.0'),
                'time': flare.get('beginTime', datetime.now().isoformat()),
                'intensity': float(flare.get('classType', 'B1.0')[1:]) if len(
                    flare.get('classType', 'B1.0')) > 1 else 1.0
            })
        return processed

    def create_simulation_data(self):
        """Create realistic simulation data"""
        flare_classes = ['B3.2', 'C1.5', 'M2.1', 'B7.8', 'X1.3', 'C5.6', 'M4.2']
        simulation_data = []

        for i, flare_class in enumerate(flare_classes):
            simulation_data.append({
                'id': f'SOLAR-FLARE-{i + 1}',
                'class': flare_class,
                'time': (datetime.now() - timedelta(hours=i * 6)).isoformat(),
                'intensity': float(flare_class[1:]) if len(flare_class) > 1 else 1.0
            })

        return simulation_data

    def calculate_impact(self, flare_class):
        """Calculate solar flare impact"""
        impacts = {
            'A': {'power': 0, 'satellites': 0, 'comm': 0, 'message': "Minimal impact", 'icon': '🌤️'},
            'B': {'power': 5, 'satellites': 3, 'comm': 8, 'message': "Minor radio interference", 'icon': '📻'},
            'C': {'power': 15, 'satellites': 10, 'comm': 20, 'message': "GPS and radio disruption", 'icon': '📡'},
            'M': {'power': 30, 'satellites': 25, 'comm': 40, 'message': "Potential power grid fluctuations", 'icon': '⚡'},
            'X': {'power': 50, 'satellites': 40, 'comm': 60, 'message': "Critical infrastructure at risk!", 'icon': '💥'}
        }

        flare_type = flare_class[0] if flare_class else 'B'
        return impacts.get(flare_type, impacts['B'])

    def show_earth_status(self):
        """Display current Earth status"""
        print("\n" + "🌍" * 30)
        print("📊 Earth Status Dashboard:")
        print("🌍" * 30)

        def progress_bar(value, label, max_value=100):
            bars = int(value / max_value * 20)
            if value >= 75:
                color = '🟩'
            elif value >= 50:
                color = '🟨'
            elif value >= 25:
                color = '🟧'
            else:
                color = '🟥'
            return f"{label}: |{color * bars}{'⬜' * (20 - bars)}| {value}%"

        print(progress_bar(self.earth_health, "🌍 Earth Health"))
        print(progress_bar(self.power_grid, "⚡ Power Grid"))
        print(progress_bar(self.satellites, "🛰️ Satellites"))
        print(progress_bar(self.communications, "📡 Communications"))
        print(f"🎯 Player Score: {self.score}")

    def handle_solar_flare(self, flare_data):
        """Handle incoming solar flare"""
        flare_class = flare_data['class']
        impact = self.calculate_impact(flare_class)

        print(f"\n{impact['icon']} Incoming Solar Flare: {flare_class}")
        print(f"📢 {impact['message']}")

        print("\n🎮 Quick action required!")
        print("Choose defense strategy:")
        print("1. 🛡️ Deploy satellite shields (-10 points)")
        print("2. ⚡ Activate grid protection (-15 points)")
        print("3. 📡 Boost communications (-8 points)")
        print("4. 🎯 Integrated defense (-20 points)")

        while True:
            try:
                choice = int(input("Enter your choice (1-4): "))
                if 1 <= choice <= 4:
                    break
                else:
                    print("Please enter a number between 1 and 4")
            except:
                print("Please enter a valid number")

        defense_success = self.apply_defense_strategy(choice, impact)
        
        # Save mission record
        self.mission_history.append({
            'flare': flare_class,
            'choice': choice,
            'success': defense_success
        })

        if defense_success:
            self.score += 25
            print("✅ Excellent defense! Earth is safe!")
        else:
            print("🔄 Partial success. Some damage occurred.")

        return defense_success

    def apply_defense_strategy(self, choice, impact):
        """Apply chosen defense strategy"""
        success = True

        if choice == 1:
            self.satellites = max(0, self.satellites - impact['satellites'] + 15)
            self.score -= 10
            print("🛡️ Satellite shields activated! Protecting space assets!")

        elif choice == 2:
            self.power_grid = max(0, self.power_grid - impact['power'] + 20)
            self.score -= 15
            print("⚡ Grid protection activated! Stabilizing power flow!")

        elif choice == 3:
            self.communications = max(0, self.communications - impact['comm'] + 12)
            self.score -= 8
            print("📡 Communications boosted! Maintaining global connection!")

        elif choice == 4:
            self.power_grid = max(0, self.power_grid - impact['power'] + 10)
            self.satellites = max(0, self.satellites - impact['satellites'] + 8)
            self.communications = max(0, self.communications - impact['comm'] + 10)
            self.score -= 20
            print("🎯 Integrated defense activated! Full protection active!")

        self.earth_health = (self.power_grid + self.satellites + self.communications) // 3

        return success

    def create_enhanced_visualization(self):
        """Create enhanced professional educational graphics"""
        if not self.solar_data:
            return

        fig = plt.figure(figsize=(20, 14), facecolor='#0a0a0a')
        fig.suptitle('🎮 Solar Defender - Mission Analysis',
                     fontsize=24, color='#00ffff', fontweight='bold', y=0.98)

        gs = fig.add_gridspec(3, 3, hspace=0.35, wspace=0.3)

        # 1. Solar Flare Distribution - Enhanced pie chart
        ax1 = fig.add_subplot(gs[0, 0])
        self.create_enhanced_pie_chart(ax1)

        # 2. Intensity Timeline - Enhanced
        ax2 = fig.add_subplot(gs[0, 1:])
        self.create_intensity_timeline(ax2)

        # 3. Earth Systems Status - 3D bar chart
        ax3 = fig.add_subplot(gs[1, 0])
        self.create_systems_status(ax3)

        # 4. Flare Impact Comparison
        ax4 = fig.add_subplot(gs[1, 1])
        self.create_impact_comparison(ax4)

        # 5. Performance Gauge
        ax5 = fig.add_subplot(gs[1, 2])
        self.create_performance_gauge(ax5)

        # 6. Earth Impact Map
        ax6 = fig.add_subplot(gs[2, :2])
        self.create_earth_impact_map(ax6)

        # 7. Mission Log
        ax7 = fig.add_subplot(gs[2, 2])
        self.create_mission_log(ax7)

        plt.tight_layout()
        plt.savefig('solar_defender_report.png', dpi=300, facecolor='#0a0a0a')
        plt.show()

    def create_enhanced_pie_chart(self, ax):
        """Professional pie chart"""
        flare_classes = [flare['class'][0] for flare in self.solar_data]
        class_counts = pd.Series(flare_classes).value_counts()

        colors_map = {
            'A': '#00ff88',
            'B': '#66ff66',
            'C': '#ffcc00',
            'M': '#ff6600',
            'X': '#ff0044'
        }
        colors = [colors_map.get(c, '#ffffff') for c in class_counts.index]

        wedges, texts, autotexts = ax.pie(
            class_counts.values,
            labels=class_counts.index,
            autopct='%1.1f%%',
            colors=colors,
            startangle=90,
            textprops={'color': 'white', 'fontsize': 12, 'weight': 'bold'},
            wedgeprops={'edgecolor': 'white', 'linewidth': 2.5}
        )

        for autotext in autotexts:
            autotext.set_color('black')
            autotext.set_fontsize(11)
            autotext.set_weight('bold')

        ax.set_title('🌞 Solar Flare Distribution',
                    color='#00ffff', fontsize=13, pad=15, weight='bold')

    def create_intensity_timeline(self, ax):
        """Enhanced intensity timeline"""
        intensities = [flare['intensity'] for flare in self.solar_data]
        times = range(len(intensities))
        classes = [flare['class'] for flare in self.solar_data]

        # Main line
        ax.plot(times, intensities, color='#00ffff', linewidth=3, alpha=0.7, zorder=2)
        ax.fill_between(times, intensities, alpha=0.3, color='#00ffff', zorder=1)

        # Colored points
        color_map = {
            'A': '#00ff88', 'B': '#66ff66', 'C': '#ffcc00',
            'M': '#ff6600', 'X': '#ff0044'
        }

        for t, intensity, flare_class in zip(times, intensities, classes):
            color = color_map.get(flare_class[0], '#ffffff')
            size = intensity * 100 + 150
            ax.scatter(t, intensity, c=color, s=size, alpha=0.9,
                      edgecolors='white', linewidths=2.5, zorder=3)

            # Labels
            ax.annotate(flare_class, (t, intensity),
                       xytext=(0, 12), textcoords='offset points',
                       ha='center', fontsize=10, color='white', weight='bold',
                       bbox=dict(boxstyle='round,pad=0.5',
                                facecolor=color, alpha=0.8,
                                edgecolor='white', linewidth=1.5))

        ax.set_title('📈 Flare Intensity Timeline',
                    color='#00ffff', fontsize=13, weight='bold')
        ax.set_ylabel('Intensity', color='white', fontsize=11)
        ax.set_xlabel('Flare Sequence', color='white', fontsize=11)
        ax.grid(True, alpha=0.3, color='#00ffff', linestyle=':', linewidth=1)
        ax.tick_params(colors='white')
        ax.set_facecolor('#0a0a0a')

    def create_systems_status(self, ax):
        """Systems Status - Enhanced bar chart"""
        systems = ['⚡ Power', '🛰️ Satellites', '📡 Communications']
        values = [self.power_grid, self.satellites, self.communications]

        colors = []
        for v in values:
            if v >= 75:
                colors.append('#00ff88')
            elif v >= 50:
                colors.append('#ffcc00')
            elif v >= 25:
                colors.append('#ff6600')
            else:
                colors.append('#ff0044')

        bars = ax.barh(systems, values, color=colors, alpha=0.85,
                      edgecolor='white', linewidth=2.5)

        # Add shadows
        for i, (bar, value) in enumerate(zip(bars, values)):
            shadow = Rectangle((0, bar.get_y() + 0.02),
                             value, bar.get_height(),
                             facecolor='black', alpha=0.3, zorder=0)
            ax.add_patch(shadow)

            # Values
            ax.text(value + 2, bar.get_y() + bar.get_height()/2,
                   f'{value}%', va='center', fontsize=12,
                   fontweight='bold', color='white')

        ax.set_xlim(0, 110)
        ax.set_title('🌍 Earth Systems Status',
                    color='#00ffff', fontsize=13, pad=10, weight='bold')
        ax.grid(True, alpha=0.2, axis='x', color='#00ffff', linestyle=':')
        ax.tick_params(colors='white')
        ax.set_facecolor('#0a0a0a')

    def create_impact_comparison(self, ax):
        """Impact Comparison"""
        if len(self.solar_data) < 3:
            return

        flare_impacts = []
        flare_labels = []
        flare_colors = []

        color_map = {
            'A': '#00ff88', 'B': '#66ff66', 'C': '#ffcc00',
            'M': '#ff6600', 'X': '#ff0044'
        }

        for flare in self.solar_data[:5]:
            impact = self.calculate_impact(flare['class'])
            total_impact = impact['power'] + impact['satellites'] + impact['comm']
            flare_impacts.append(total_impact)
            flare_labels.append(flare['class'])
            flare_colors.append(color_map.get(flare['class'][0], '#ffffff'))

        bars = ax.bar(flare_labels, flare_impacts, color=flare_colors,
                     alpha=0.85, edgecolor='white', linewidth=2.5)

        # Values above bars
        for bar, impact in zip(bars, flare_impacts):
            ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 3,
                   str(impact), ha='center', va='bottom',
                   fontsize=11, fontweight='bold', color='white')

        ax.set_title('⚠️ Flare Impact Comparison',
                    color='#00ffff', fontsize=13, pad=10, weight='bold')
        ax.set_ylabel('Total Impact', color='white', fontsize=11)
        ax.grid(True, alpha=0.2, axis='y', color='#00ffff', linestyle=':')
        ax.tick_params(colors='white')
        ax.set_facecolor('#0a0a0a')

    def create_performance_gauge(self, ax):
        """Performance Gauge"""
        # Calculate performance percentage
        max_score = len(self.solar_data) * 25
        performance = (self.score / max_score * 100) if max_score > 0 else 0

        # Background circle
        circle_bg = Circle((0.5, 0.5), 0.4, color='#1a1a1a', transform=ax.transAxes)
        ax.add_patch(circle_bg)

        # Performance arc
        theta1 = 180
        theta2 = 180 - (performance * 1.8)

        if performance >= 75:
            color = '#00ff88'
            status = 'Excellent'
        elif performance >= 50:
            color = '#ffcc00'
            status = 'Good'
        elif performance >= 25:
            color = '#ff6600'
            status = 'Fair'
        else:
            color = '#ff0044'
            status = 'Poor'

        wedge = Wedge((0.5, 0.5), 0.4, theta2, theta1,
                     transform=ax.transAxes, color=color, alpha=0.8)
        ax.add_patch(wedge)

        # Center text
        ax.text(0.5, 0.55, f'{performance:.0f}%',
               transform=ax.transAxes, ha='center', va='center',
               fontsize=36, fontweight='bold', color=color)
        ax.text(0.5, 0.42, status,
               transform=ax.transAxes, ha='center', va='center',
               fontsize=14, color='white', weight='bold')

        ax.set_title('🎯 Performance Gauge',
                    color='#00ffff', fontsize=13, pad=10, weight='bold')
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.axis('off')

    def create_earth_impact_map(self, ax):
        """Earth Impact Map"""
        # Draw Earth
        theta = np.linspace(0, 2*np.pi, 100)
        x_earth = np.cos(theta)
        y_earth = np.sin(theta)

        ax.fill(x_earth, y_earth, color='#1a4d80', alpha=0.9, zorder=1)
        ax.plot(x_earth, y_earth, color='#00ffff', linewidth=4, zorder=2)

        # Latitude and longitude lines
        for lat in np.linspace(-0.8, 0.8, 5):
            x_lat = np.cos(theta) * np.sqrt(max(0, 1 - lat**2))
            y_lat = np.ones_like(theta) * lat
            ax.plot(x_lat, y_lat, color='#00ffff', alpha=0.3, linewidth=1.5)

        # Impact zones
        dangerous_flares = [f for f in self.solar_data if f['class'][0] in ['M', 'X']]

        if dangerous_flares:
            for i, radius in enumerate([1.15, 1.3, 1.45]):
                alpha = 0.5 - i*0.1
                color = '#ff0044' if any(f['class'][0] == 'X' for f in dangerous_flares) else '#ff6600'
                circle = Circle((0, 0), radius, fill=False,
                              edgecolor=color, linewidth=3,
                              linestyle='--', alpha=alpha, zorder=3)
                ax.add_patch(circle)

            # Auroras
            aurora_theta = np.linspace(np.pi/6, 5*np.pi/6, 50)
            for pole in [1, -1]:
                x_aurora = 1.2 * np.cos(aurora_theta)
                y_aurora = pole * 1.2 * np.abs(np.sin(aurora_theta))
                ax.plot(x_aurora, y_aurora, color='#00ff88',
                       linewidth=4, alpha=0.8, zorder=4)

        # Center text
        ax.text(0, 0, '🌍\nEARTH', ha='center', va='center',
               fontsize=20, color='white', weight='bold',
               bbox=dict(boxstyle='round,pad=1',
                        facecolor='#0a0a0a', alpha=0.8,
                        edgecolor='#00ffff', linewidth=3))

        ax.set_title('🌍 Planetary Impact Map',
                    color='#00ffff', fontsize=13, pad=10, weight='bold')
        ax.set_xlim(-1.8, 1.8)
        ax.set_ylim(-1.8, 1.8)
        ax.set_aspect('equal')
        ax.axis('off')
        ax.set_facecolor('#0a0a0a')

    def create_mission_log(self, ax):
        """Mission Log"""
        ax.axis('off')
        ax.set_title('📜 Mission Log',
                    color='#00ffff', fontsize=13, pad=10, weight='bold')

        y_pos = 0.9
        strategy_names = {
            1: "🛡️ Satellite Shields",
            2: "⚡ Grid Protection",
            3: "📡 Comm Boost",
            4: "🎯 Integrated Defense"
        }

        for i, mission in enumerate(self.mission_history[:5]):
            status = "✅" if mission['success'] else "⚠️"
            strategy = strategy_names.get(mission['choice'], "❓")
            text = f"{status} {mission['flare']}: {strategy}"

            ax.text(0.1, y_pos, text, transform=ax.transAxes,
                   fontsize=11, color='white', weight='bold',
                   bbox=dict(boxstyle='round,pad=0.5',
                            facecolor='#1a1a1a', alpha=0.8,
                            edgecolor='#00ffff', linewidth=1))
            y_pos -= 0.18

        ax.set_facecolor('#0a0a0a')

    def educational_facts(self):
        """Display educational facts about space weather"""
        facts = [
            "💡 The Sun is 93 million miles away but affects Earth in 8 minutes!",
            "🌌 Solar flares travel at light speed - 186,000 miles per second!",
            "📡 A single X-class flare can release energy equal to billions of atomic bombs!",
            "🛰️ Astronauts on the Space Station need special protection during solar storms!",
            "🌍 Earth's magnetic field is our natural shield against solar radiation!",
            "🌈 Beautiful auroras are created when solar particles hit our atmosphere!",
            "⚡ The largest recorded solar storm in 1859 disrupted telegraph systems!",
            "🔭 NASA's Solar Dynamics Observatory monitors the Sun 24/7 to protect Earth!"
        ]

        print("\n" + "📚" * 20)
        print("🎓 Space Weather Facts for Kids:")
        print("📚" * 20)

        for i, fact in enumerate(facts[:4]):
            print(f"{i + 1}. {fact}")
            time.sleep(1.5)

    def game_loop(self):
        """Main game loop"""
        print("\n" + "🎮" * 30)
        print("Starting Solar Defense Mission...")
        print("🎮" * 30)

        # Process each solar flare
        for i, flare in enumerate(self.solar_data[:5]):
            print(f"\n🌀 Mission Phase {i + 1}/5")
            print("=" * 40)

            self.handle_solar_flare(flare)
            self.show_earth_status()

            # Check for game over
            if self.earth_health <= 0:
                print("\n💀 Mission Failed: Earth's systems collapsed!")
                break

            time.sleep(2)

        # Show final results
        self.show_final_results()

    def show_final_results(self):
        """Display final game results"""
        print("\n" + "🏆" * 30)
        print("🎯 Mission Complete - Final Results:")
        print("🏆" * 30)

        self.show_earth_status()

        # Determine rank
        if self.score >= 80:
            rank = "🌟 Solar Defender Master 🌟"
            message = "Amazing! You're a true space weather expert!"
        elif self.score >= 50:
            rank = "🎖️ Space Commander 🎖️"
            message = "Excellent work! Earth is in safe hands!"
        elif self.score >= 25:
            rank = "🚀 Space Cadet 🚀"
            message = "Good effort! Keep learning about space weather!"
        else:
            rank = "⭐ Space Beginner ⭐"
            message = "Good start! More training will make you better!"

        print(f"\n🎖️ Your Rank: {rank}")
        print(f"💬 {message}")

        # Educational facts
        self.educational_facts()

        # Visualizations
        print("\n📊 Generating mission analysis...")
        time.sleep(2)
        self.create_enhanced_visualization()

    def start_game(self):
        """Start the game"""
        self.welcome_animation()
        self.get_player_info()

        if self.fetch_solar_data():
            self.game_loop()

        print(f"\n👏 Thanks for playing, Commander {self.player_name}!")
        print("🌎 Remember: Understanding space weather helps us protect our planet!")


# Run the game
if __name__ == "__main__":
    print("\n" + "🌟" * 60)
    print("Loading Solar Defense System...")
    print("🌟" * 60)
    time.sleep(1)
    
    game = EnhancedSolarDefenderGame()
    game.start_game()
    
    print("\n" + "🚀" * 60)
    print("✅ Mission completed successfully!")
    print("💫 See you in the next mission, Solar Defender!")
    print("🚀" * 60)
