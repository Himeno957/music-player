# ===== 强制指定 VLC 路径（打包后用） =====
def fix_vlc_path():
    """强制设置 VLC 路径"""
    import sys
    import os
    
    # 获取 exe 所在目录
    if getattr(sys, 'frozen', False):
        base_dir = os.path.dirname(sys.executable)
    else:
        base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # VLC 文件夹路径
    vlc_dir = os.path.join(base_dir, 'vlc')
    
    if os.path.exists(vlc_dir):
        # 设置环境变量
        os.environ['VLC_PLUGIN_PATH'] = os.path.join(vlc_dir, 'plugins')
        os.environ['PATH'] = vlc_dir + os.pathsep + os.environ.get('PATH', '')
        print(f"✅ 已设置 VLC 路径: {vlc_dir}")
        return vlc_dir
    else:
        print(f"❌ 未找到 VLC: {vlc_dir}")
        return None

# 立即执行
fix_vlc_path()
# ===== 结束 =====
import sys
import os
import warnings
import json
import re
import random
import codecs
import math
warnings.filterwarnings("ignore")
def fix_vlc_path():
    """强制设置 VLC 路径"""
    if getattr(sys, 'frozen', False):
        base_dir = os.path.dirname(sys.executable)
    else:
        base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 检查多个位置
    possible_paths = [
        os.path.join(base_dir, 'vlc'),
        os.path.join(base_dir, 'dist', 'vlc'),  # 新增：dist目录下
        os.path.join(os.getcwd(), 'vlc'),
        os.path.join(os.getcwd(), 'dist', 'vlc'),
        r'C:\Program Files\VideoLAN\VLC',
    ]
    
    for vlc_dir in possible_paths:
        if os.path.exists(vlc_dir):
            libvlc = os.path.join(vlc_dir, 'libvlc.dll')
            if os.path.exists(libvlc):
                os.environ['VLC_PLUGIN_PATH'] = os.path.join(vlc_dir, 'plugins')
                os.environ['PATH'] = vlc_dir + os.pathsep + os.environ.get('PATH', '')
                print(f"✅ 找到 VLC: {vlc_dir}")
                return vlc_dir
    
    print(f"❌ 未找到 VLC")
    return None

# ===== 正常导入 =====
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, TIT2, TPE1, TALB, APIC, USLT, SYLT
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent

# ===== 尝试导入 VLC =====
try:
    import vlc
    VLC_AVAILABLE = True
except:
    VLC_AVAILABLE = False


# ============================================================
# ===== VLC 路径处理（支持打包后运行） =====
# ============================================================

def get_base_dir():
    """获取程序运行目录（支持打包后）"""
    if getattr(sys, 'frozen', False):
        return sys._MEIPASS
    else:
        return os.path.dirname(os.path.abspath(__file__))

def get_vlc_path():
    """获取 VLC 路径（支持打包后和开发环境）"""
    if getattr(sys, 'frozen', False):
        # 打包后的 exe 运行 - 在 exe 所在的目录查找 vlc 文件夹
        base_dir = os.path.dirname(sys.executable)
    else:
        # 开发环境运行
        base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 检查 exe 同目录下的 vlc 文件夹
    vlc_dir = os.path.join(base_dir, 'vlc')
    if os.path.exists(vlc_dir):
        print(f"✅ 找到内置 VLC: {vlc_dir}")
        return vlc_dir
    
    # 检查是否有 vlc 子目录（备用）
    vlc_sub_dir = os.path.join(base_dir, 'vlc')
    if os.path.exists(vlc_sub_dir):
        print(f"✅ 找到内置 VLC (子目录): {vlc_sub_dir}")
        return vlc_sub_dir
    
    print(f"⚠️ 未找到内置 VLC，尝试使用系统 VLC")
    print(f"   查找路径: {vlc_dir}")
    return None

def setup_vlc_environment():
    """设置 VLC 环境变量"""
    vlc_path = get_vlc_path()
    if vlc_path:
        plugin_path = os.path.join(vlc_path, 'plugins')
        if os.path.exists(plugin_path):
            os.environ['VLC_PLUGIN_PATH'] = plugin_path
        os.environ['PATH'] = vlc_path + os.pathsep + os.environ.get('PATH', '')
        print(f"✅ 使用内置 VLC: {vlc_path}")
        return True
    else:
        print("⚠️ 未找到内置 VLC，尝试使用系统 VLC")
        return False


class Particle:
    """粒子基类"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 0
        self.size = 0
        self.opacity = 0
        self.active = True
        
    def update(self, width, height):
        pass
        
    def draw(self, painter):
        pass


class RainDrop(Particle):
    """雨滴粒子"""
    def __init__(self, width, height):
        super().__init__(random.randint(0, width), random.randint(-20, height))
        self.speed = random.uniform(8, 18)
        self.size = random.uniform(1.5, 3.5)
        self.opacity = random.uniform(30, 80)
        self.length = random.uniform(8, 20)
        self.x_offset = random.uniform(-2, 2)
        
    def update(self, width, height):
        self.x += self.x_offset + self.speed * 0.3
        self.y += self.speed
        if self.y > height + 20:
            self.y = random.randint(-20, -5)
            self.x = random.randint(0, width)
            self.speed = random.uniform(8, 18)
            self.size = random.uniform(1.5, 3.5)
            self.opacity = random.uniform(30, 80)
            self.length = random.uniform(8, 20)
            
    def draw(self, painter):
        painter.setPen(QPen(QColor(180, 210, 255, int(self.opacity)), self.size, Qt.SolidLine))
        x1 = int(self.x)
        y1 = int(self.y)
        x2 = int(self.x + self.x_offset * 2)
        y2 = int(self.y + self.length)
        painter.drawLine(x1, y1, x2, y2)


class SnowFlake(Particle):
    """雪花粒子"""
    def __init__(self, width, height):
        super().__init__(random.randint(0, width), random.randint(-20, height))
        self.speed = random.uniform(1, 3.5)
        self.size = random.uniform(2, 6)
        self.opacity = random.uniform(40, 120)
        self.swing = random.uniform(0.5, 2)
        self.swing_speed = random.uniform(0.02, 0.05)
        self.angle = random.uniform(0, 2 * math.pi)
        self.start_x = self.x
        
    def update(self, width, height):
        self.angle += self.swing_speed
        self.x = self.start_x + math.sin(self.angle) * self.swing * 15
        self.y += self.speed
        if self.y > height + 10:
            self.y = random.randint(-20, -5)
            self.start_x = random.randint(0, width)
            self.x = self.start_x
            self.speed = random.uniform(1, 3.5)
            self.size = random.uniform(2, 6)
            self.opacity = random.uniform(40, 120)
            
    def draw(self, painter):
        painter.setPen(QPen(QColor(255, 255, 255, int(self.opacity)), self.size, Qt.SolidLine))
        painter.drawPoint(int(self.x), int(self.y))


class AtmosphereWidget(QWidget):
    """氛围效果覆盖层"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setAttribute(Qt.WA_TransparentForMouseEvents)
        
        self.particles = []
        self.mode = None
        self.is_active = False
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_particles)
        self.timer.start(30)
        
        self.rain_count = 80
        self.snow_count = 60
        
        self.setup_ui()
        
    def setup_ui(self):
        self.setStyleSheet("background: transparent;")
        
    def resizeEvent(self, event):
        if self.mode == 'rain':
            self.init_rain()
        elif self.mode == 'snow':
            self.init_snow()
        super().resizeEvent(event)
        
    def init_rain(self):
        self.particles = []
        w = self.width()
        h = self.height()
        for _ in range(self.rain_count):
            self.particles.append(RainDrop(w, h))
            
    def init_snow(self):
        self.particles = []
        w = self.width()
        h = self.height()
        for _ in range(self.snow_count):
            self.particles.append(SnowFlake(w, h))
            
    def start_rain(self):
        self.mode = 'rain'
        self.is_active = True
        self.init_rain()
        self.show()
        
    def start_snow(self):
        self.mode = 'snow'
        self.is_active = True
        self.init_snow()
        self.show()
        
    def stop(self):
        self.is_active = False
        self.mode = None
        self.particles = []
        self.hide()
        
    def update_particles(self):
        if not self.is_active or not self.particles:
            return
        w = self.width()
        h = self.height()
        for p in self.particles:
            p.update(w, h)
        self.update()
        
    def paintEvent(self, event):
        if not self.is_active or not self.particles:
            return
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        for p in self.particles:
            p.draw(painter)


class VolumeSlider(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(130, 32)
        self.setMouseTracking(True)
        self.volume = 20
        self.is_hover = False
        self.is_dragging = False
        self.parent_player = parent
        
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        if self.is_hover or self.is_dragging:
            bg_color = QColor(60, 60, 60, 180)
            painter.setBrush(bg_color)
            painter.setPen(Qt.NoPen)
            painter.drawRoundedRect(0, 0, self.width(), self.height(), 6, 6)
        
        icon_x = 8
        icon_y = 6
        icon_h = 20
        
        if self.is_hover or self.is_dragging:
            icon_color = QColor(255, 255, 255)
        else:
            icon_color = QColor(255, 255, 255, 200)
        
        painter.setPen(QPen(icon_color, 2.0))
        painter.setBrush(Qt.NoBrush)
        painter.drawRect(icon_x, icon_y + 5, 8, 10)
        points = [
            QPoint(icon_x + 8, icon_y + 2),
            QPoint(icon_x + 14, icon_y + 2),
            QPoint(icon_x + 14, icon_y + icon_h - 2),
            QPoint(icon_x + 8, icon_y + icon_h - 2)
        ]
        painter.drawPolygon(QPolygon(points))
        
        if self.volume > 0:
            wave_color = QColor(255, 255, 255, 200)
            painter.setPen(QPen(wave_color, 2.0))
            if self.volume > 10:
                painter.drawArc(icon_x + 18, icon_y + 5, 6, 10, -50*16, 100*16)
            if self.volume > 40:
                painter.drawArc(icon_x + 22, icon_y + 3, 8, 14, -40*16, 80*16)
            if self.volume > 70:
                painter.drawArc(icon_x + 26, icon_y + 1, 10, 18, -30*16, 60*16)
        
        slider_x = 44
        slider_y = self.height() // 2 - 2
        slider_width = self.width() - slider_x - 10
        slider_height = 4
        
        painter.setPen(Qt.NoPen)
        painter.setBrush(QColor(255, 255, 255, 100))
        painter.drawRoundedRect(slider_x, slider_y, slider_width, slider_height, 2, 2)
        
        if self.volume > 0:
            fill_width = int(slider_width * self.volume / 100)
            painter.setBrush(QColor(255, 255, 255, 200))
            painter.drawRoundedRect(slider_x, slider_y, fill_width, slider_height, 2, 2)
        
        dot_x = slider_x + int(slider_width * self.volume / 100)
        dot_radius = 6
        painter.setBrush(QColor(255, 255, 255))
        painter.setPen(QPen(QColor(255, 255, 255, 200), 1))
        painter.drawEllipse(QPoint(dot_x, slider_y + slider_height // 2), dot_radius, dot_radius)
        
        text = f"{self.volume}%"
        painter.setPen(QColor(255, 255, 255, 220))
        painter.setFont(QFont("Arial", 8))
        
        text_rect = painter.boundingRect(0, 0, self.width(), 20, Qt.AlignCenter, text)
        text_x = dot_x - text_rect.width() // 2
        text_y = slider_y - 18
        if text_x < 0:
            text_x = 0
        if text_x + text_rect.width() > self.width():
            text_x = self.width() - text_rect.width()
        painter.drawText(text_x, text_y + text_rect.height(), text)
        
        painter.end()
        
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.is_dragging = True
            self.update_volume_from_pos(event.pos())
            self.update()
            
    def mouseMoveEvent(self, event):
        if self.is_dragging:
            self.update_volume_from_pos(event.pos())
            self.update()
        else:
            rect = self.rect()
            if rect.contains(event.pos()):
                self.is_hover = True
            else:
                self.is_hover = False
            self.update()
            
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.is_dragging = False
            self.update()
            
    def leaveEvent(self, event):
        self.is_hover = False
        self.update()
        
    def update_volume_from_pos(self, pos):
        slider_x = 44
        slider_width = self.width() - slider_x - 10
        x = pos.x() - slider_x
        if x < 0:
            x = 0
        elif x > slider_width:
            x = slider_width
        volume = int(x / slider_width * 100)
        if volume != self.volume:
            self.volume = volume
            if self.parent_player:
                self.parent_player.set_volume(volume)
            self.update()
            
    def set_volume(self, volume):
        self.volume = max(0, min(100, volume))
        self.update()


def detect_encoding(file_path):
    encodings = ['utf-8', 'utf-8-sig', 'gbk', 'gb2312', 'big5', 'gb18030', 'shift-jis']
    for enc in encodings:
        try:
            with open(file_path, 'r', encoding=enc) as f:
                f.read()
                return enc
        except:
            continue
    return 'utf-8'


def parse_lrc_file(file_path):
    lyrics = []
    encoding = detect_encoding(file_path)
    
    try:
        with open(file_path, 'r', encoding=encoding) as f:
            content = f.read()
    except:
        for enc in ['utf-8', 'gbk', 'gb2312', 'big5', 'utf-8-sig']:
            try:
                with open(file_path, 'r', encoding=enc) as f:
                    content = f.read()
                    break
            except:
                continue
        else:
            return []
    
    if not content.strip():
        return []
    
    lines = content.split('\n')
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if re.match(r'^\[[a-zA-Z]+:', line):
            continue
        
        matches = []
        m = re.search(r'\[(\d{2}):(\d{2})(?:\.|:)(\d{2})\](.*)', line)
        if m:
            matches.append((int(m.group(1)), int(m.group(2)), int(m.group(3)), m.group(4)))
        
        m = re.search(r'\[(\d{2}):(\d{2})\](.*)', line)
        if m:
            matches.append((int(m.group(1)), int(m.group(2)), 0, m.group(3)))
        
        m = re.search(r'\[(\d{1}):(\d{2})(?:\.|:)(\d{2})\](.*)', line)
        if m:
            matches.append((int(m.group(1)), int(m.group(2)), int(m.group(3)), m.group(4)))
        
        m = re.search(r'\[(\d{1}):(\d{2})\](.*)', line)
        if m:
            matches.append((int(m.group(1)), int(m.group(2)), 0, m.group(3)))
        
        m = re.search(r'\[(\d{2}):(\d{2})\.(\d{3})\](.*)', line)
        if m:
            matches.append((int(m.group(1)), int(m.group(2)), int(m.group(3)) // 10, m.group(4)))
        
        for minutes, seconds, centiseconds, text in matches:
            text = text.strip()
            if text:
                time_ms = (minutes * 60 + seconds) * 1000 + centiseconds * 10
                lyrics.append({'time_ms': time_ms, 'text': text})
    
    lyrics.sort(key=lambda x: x['time_ms'])
    
    unique_lyrics = []
    seen_times = set()
    for lyric in lyrics:
        if lyric['time_ms'] not in seen_times:
            seen_times.add(lyric['time_ms'])
            unique_lyrics.append(lyric)
    
    return unique_lyrics


def extract_embedded_lyrics(tags):
    try:
        if 'USLT' in tags:
            return str(tags['USLT'])
        elif 'SYLT' in tags:
            sylt = tags['SYLT']
            if hasattr(sylt, 'text'):
                return str(sylt.text)
            elif hasattr(sylt, 'data'):
                return str(sylt.data)
    except:
        pass
    return None


class ExpandPanel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent_player = parent
        
        self.setVisible(False)
        self.setFixedHeight(0)
        
        self.lyric_lines = []
        self.current_lyric_index = -1
        self.lyric_labels = []
        self.scroll_animation = None
        
        self.setup_ui()
        
    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        
        self.setStyleSheet("background: transparent;")
        
        top_bar = QWidget()
        top_bar.setFixedHeight(45)
        top_bar.setStyleSheet("background: transparent;")
        top_layout = QHBoxLayout(top_bar)
        top_layout.setContentsMargins(20, 5, 20, 5)
        
        self.close_btn = QPushButton("✕ 收起")
        self.close_btn.setStyleSheet("""
            QPushButton {
                background: rgba(255, 255, 255, 0.15);
                color: white;
                border: none;
                border-radius: 14px;
                padding: 5px 14px;
                font-size: 12px;
            }
            QPushButton:hover {
                background: rgba(255, 70, 70, 0.4);
            }
        """)
        self.close_btn.clicked.connect(self.hide_panel)
        top_layout.addWidget(self.close_btn)
        top_layout.addStretch()
        layout.addWidget(top_bar)
        
        content_widget = QWidget()
        content_widget.setStyleSheet("background: transparent;")
        content_layout = QHBoxLayout(content_widget)
        content_layout.setContentsMargins(40, 5, 40, 15)
        content_layout.setSpacing(40)
        
        left_widget = QWidget()
        left_widget.setFixedWidth(280)
        left_widget.setStyleSheet("background: transparent;")
        left_layout = QVBoxLayout(left_widget)
        left_layout.setAlignment(Qt.AlignCenter)
        left_layout.setSpacing(10)
        
        self.cover_label = QLabel()
        self.cover_label.setFixedSize(260, 260)
        self.cover_label.setAlignment(Qt.AlignCenter)
        self.cover_label.setStyleSheet("""
            background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                stop:0 rgba(102,126,234,0.85), stop:1 rgba(118,75,162,0.85));
            border-radius: 14px;
            color: white;
            font-size: 48px;
        """)
        self.cover_label.setText("🎵")
        left_layout.addWidget(self.cover_label, 0, Qt.AlignCenter)
        
        self.song_title = QLabel("未播放")
        self.song_title.setStyleSheet("""
            color: white;
            font-size: 20px;
            font-weight: bold;
            padding: 6px 0 1px 0;
        """)
        self.song_title.setAlignment(Qt.AlignCenter)
        left_layout.addWidget(self.song_title)
        
        self.song_artist = QLabel("")
        self.song_artist.setStyleSheet("color: rgba(255,255,255,0.7); font-size: 14px;")
        self.song_artist.setAlignment(Qt.AlignCenter)
        left_layout.addWidget(self.song_artist)
        
        self.album_label = QLabel("")
        self.album_label.setStyleSheet("color: rgba(255,255,255,0.5); font-size: 12px;")
        self.album_label.setAlignment(Qt.AlignCenter)
        left_layout.addWidget(self.album_label)
        
        left_layout.addStretch()
        content_layout.addWidget(left_widget)
        
        right_widget = QWidget()
        right_widget.setStyleSheet("background: transparent;")
        right_layout = QVBoxLayout(right_widget)
        right_layout.setContentsMargins(0, 0, 0, 0)
        right_layout.setSpacing(6)
        
        lyric_title = QLabel("🎤 歌词")
        lyric_title.setStyleSheet("color: rgba(255,255,255,0.5); font-size: 13px; font-weight: bold;")
        right_layout.addWidget(lyric_title)
        
        self.lyric_scroll = QScrollArea()
        self.lyric_scroll.setWidgetResizable(True)
        self.lyric_scroll.setMinimumHeight(280)
        self.lyric_scroll.setStyleSheet("""
            QScrollArea { background: transparent; border: none; }
            QScrollBar:vertical { width: 3px; background: transparent; }
            QScrollBar::handle:vertical { background: rgba(255,255,255,0.3); border-radius: 2px; }
        """)
        
        self.lyric_content = QWidget()
        self.lyric_content.setStyleSheet("background: transparent;")
        self.lyric_layout = QVBoxLayout(self.lyric_content)
        self.lyric_layout.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        self.lyric_layout.setSpacing(4)
        self.lyric_layout.setContentsMargins(0, 5, 10, 15)
        
        self.no_lyric_label = QLabel("暂无歌词")
        self.no_lyric_label.setStyleSheet("color: rgba(255,255,255,0.5); font-size: 15px; padding: 20px;")
        self.no_lyric_label.setAlignment(Qt.AlignCenter)
        self.lyric_layout.addWidget(self.no_lyric_label)
        
        self.lyric_scroll.setWidget(self.lyric_content)
        right_layout.addWidget(self.lyric_scroll)
        
        content_layout.addWidget(right_widget, 1)
        layout.addWidget(content_widget, 1)
        
    def show_panel(self):
        self.setVisible(True)
        self.setFixedHeight(400)
        
    def hide_panel(self):
        self.setVisible(False)
        self.setFixedHeight(0)
        
    def set_lyrics(self, lyrics):
        for label in self.lyric_labels:
            self.lyric_layout.removeWidget(label)
            label.deleteLater()
        self.lyric_labels.clear()
        
        if self.no_lyric_label is not None:
            self.lyric_layout.removeWidget(self.no_lyric_label)
            self.no_lyric_label.deleteLater()
            self.no_lyric_label = None
            
        while self.lyric_layout.count() > 0:
            item = self.lyric_layout.takeAt(0)
            if item is not None:
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
        
        if not lyrics or len(lyrics) == 0:
            self.no_lyric_label = QLabel("暂无歌词")
            self.no_lyric_label.setStyleSheet("color: rgba(255,255,255,0.5); font-size: 15px; padding: 20px;")
            self.no_lyric_label.setAlignment(Qt.AlignCenter)
            self.lyric_layout.addWidget(self.no_lyric_label)
            self.lyric_lines = []
            return
        
        self.lyric_lines = lyrics
        self.current_lyric_index = -1
        
        for line in lyrics:
            if isinstance(line, dict) and 'text' in line:
                text = line['text']
            else:
                text = str(line)
                
            label = QLabel(text)
            label.setStyleSheet("""
                font-size: 15px;
                color: rgba(255,255,255,0.7);
                padding: 3px 8px;
                border-radius: 4px;
                background: transparent;
                font-family: "Microsoft YaHei", "PingFang SC", sans-serif;
            """)
            label.setWordWrap(True)
            label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
            self.lyric_layout.addWidget(label)
            self.lyric_labels.append(label)
        
        self.lyric_layout.addStretch()
        
    def update_lyric_highlight(self, position_ms):
        if not self.lyric_lines or not self.lyric_labels:
            return
            
        current_index = -1
        for i, line in enumerate(self.lyric_lines):
            if line['time_ms'] <= position_ms:
                current_index = i
            else:
                break
        
        if current_index != self.current_lyric_index:
            self.current_lyric_index = current_index
            
            for i, label in enumerate(self.lyric_labels):
                if i == current_index:
                    label.setStyleSheet("""
                        font-size: 16px;
                        font-weight: bold;
                        color: #1a73e8;
                        padding: 3px 8px;
                        border-radius: 4px;
                        background: rgba(255,255,255,0.15);
                        font-family: "Microsoft YaHei", "PingFang SC", sans-serif;
                    """)
                else:
                    label.setStyleSheet("""
                        font-size: 15px;
                        color: rgba(255,255,255,0.7);
                        padding: 3px 8px;
                        border-radius: 4px;
                        background: transparent;
                        font-family: "Microsoft YaHei", "PingFang SC", sans-serif;
                    """)
            
            if current_index >= 0 and current_index < len(self.lyric_labels):
                self.scroll_to_lyric(current_index)
                
    def scroll_to_lyric(self, index):
        if index < 0 or index >= len(self.lyric_labels):
            return
        
        target_label = self.lyric_labels[index]
        label_pos = target_label.pos()
        label_height = target_label.height()
        scroll_height = self.lyric_scroll.viewport().height()
        
        target_y = label_pos.y() - (scroll_height - label_height) // 2
        if target_y < 0:
            target_y = 0
        
        scrollbar = self.lyric_scroll.verticalScrollBar()
        max_value = scrollbar.maximum()
        if target_y > max_value:
            target_y = max_value
        
        if self.scroll_animation is not None:
            self.scroll_animation.stop()
            self.scroll_animation.deleteLater()
            self.scroll_animation = None
        
        self.scroll_animation = QPropertyAnimation(scrollbar, b"value")
        self.scroll_animation.setDuration(120)
        self.scroll_animation.setStartValue(scrollbar.value())
        self.scroll_animation.setEndValue(target_y)
        self.scroll_animation.setEasingCurve(QEasingCurve.OutCubic)
        self.scroll_animation.start()
                
    def update_info(self, title, artist, album, cover_data=None, lyrics=None):
        self.song_title.setText(title or "未播放")
        self.song_artist.setText(artist or "")
        self.album_label.setText(album or "")
        
        if cover_data:
            try:
                pixmap = QPixmap()
                pixmap.loadFromData(cover_data)
                pixmap = pixmap.scaled(260, 260, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                rounded = QPixmap(pixmap.size())
                rounded.fill(Qt.transparent)
                painter = QPainter(rounded)
                painter.setRenderHint(QPainter.Antialiasing)
                path = QPainterPath()
                path.addRoundedRect(0, 0, 260, 260, 14, 14)
                painter.setClipPath(path)
                painter.drawPixmap(0, 0, pixmap)
                painter.end()
                self.cover_label.setPixmap(rounded)
                self.cover_label.setText("")
                self.cover_label.setStyleSheet("background: transparent; border-radius: 14px;")
            except:
                self.set_default_cover()
        else:
            self.set_default_cover()
        
        self.set_lyrics(lyrics)
        self.current_lyric_index = -1
            
    def set_default_cover(self):
        colors = ["#667eea", "#764ba2", "#f093fb", "#4facfe", "#43e97b", "#fa709a", "#f5576c", "#ffecd2"]
        color = random.choice(colors)
        self.cover_label.setStyleSheet(f"""
            background: {color};
            border-radius: 14px;
            color: white;
            font-size: 48px;
        """)
        self.cover_label.setText("🎵")
        self.cover_label.setAlignment(Qt.AlignCenter)


class MusicPlayer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("音乐播放器")
        self.setGeometry(100, 100, 950, 700)
        self.setMinimumSize(800, 600)
        
        # 设置窗口图标
        icon_path = os.path.join(get_base_dir(), "icon.ico")
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))
        
        self.music_list = []
        self.current_index = -1
        self.is_playing = False
        self.current_folder = None
        self.current_lyrics = []
        self.background_pixmap = None
        self.is_expanded = False
        
        self.hidden_files = set()
        self.hidden_files_file = "hidden_files.json"
        self.load_hidden_files()
        
        self.use_vlc = False
        self.player = None
        self.vlc_instance = None
        
        self.init_player()
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_progress)
        self.timer.start(500)
        
        self.check_timer = QTimer()
        self.check_timer.timeout.connect(self.check_playback_state)
        self.check_timer.start(1000)
        
        self.setup_ui()
        self.setup_menu()
        self.apply_style()
        
    def init_player(self):
        """初始化播放器 - 支持内置 VLC"""
        try:
            if VLC_AVAILABLE:
                # 设置 VLC 环境
                setup_vlc_environment()
                
                # 创建 VLC 实例
                vlc_path = get_vlc_path()
                if vlc_path:
                    plugin_path = os.path.join(vlc_path, 'plugins')
                    self.vlc_instance = vlc.Instance(['--plugin-path=' + plugin_path])
                else:
                    self.vlc_instance = vlc.Instance()
                
                self.player = self.vlc_instance.media_player_new()
                self.player.audio_set_volume(20)
                self.use_vlc = True
                print("✅ 使用 VLC 播放器")
                self.event_manager = self.player.event_manager()
                self.event_manager.event_attach(
                    vlc.EventType.MediaPlayerEndReached,
                    self.on_song_end
                )
                return
        except Exception as e:
            print(f"VLC 初始化失败: {e}")
        
        try:
            self.player = QMediaPlayer()
            self.player.setVolume(20)
            self.use_vlc = False
            print("✅ 使用 QMediaPlayer 播放器")
            self.player.stateChanged.connect(self.handle_player_state)
        except Exception as e:
            print(f"播放器初始化失败: {e}")
            self.player = None
    
    def check_playback_state(self):
        if not self.player or not self.is_playing:
            return
        try:
            if self.use_vlc:
                state = self.player.get_state()
                if state == vlc.State.Ended or state == vlc.State.Stopped:
                    self.next_song()
            else:
                state = self.player.state()
                if state == QMediaPlayer.StoppedState:
                    self.next_song()
        except:
            pass
    
    def on_song_end(self, event):
        QMetaObject.invokeMethod(self, "next_song", Qt.QueuedConnection)
    
    def handle_player_state(self, state):
        if state == QMediaPlayer.StoppedState and self.current_index >= 0 and self.is_playing:
            self.next_song()
    
    def load_hidden_files(self):
        try:
            if os.path.exists(self.hidden_files_file):
                with open(self.hidden_files_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.hidden_files = set(data)
        except:
            self.hidden_files = set()
    
    def save_hidden_files(self):
        try:
            with open(self.hidden_files_file, 'w', encoding='utf-8') as f:
                json.dump(list(self.hidden_files), f, ensure_ascii=False, indent=2)
        except:
            pass
        
    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        central_widget.setLayout(main_layout)
        
        self.bg_container = QWidget()
        self.bg_container.setObjectName("bgContainer")
        self.bg_container.setStyleSheet("background: #1a1a2e;")
        bg_layout = QVBoxLayout(self.bg_container)
        bg_layout.setContentsMargins(0, 0, 0, 0)
        bg_layout.setSpacing(0)
        
        self.bg_label = QLabel(self.bg_container)
        self.bg_label.setAttribute(Qt.WA_TranslucentBackground)
        self.bg_label.setGeometry(0, 0, self.width(), self.height())
        self.bg_label.lower()
        self.bg_label.hide()
        
        self.expand_panel = ExpandPanel(self)
        bg_layout.addWidget(self.expand_panel)
        
        control_bar = QWidget()
        control_bar.setFixedHeight(120)
        control_bar.setStyleSheet("background: transparent;")
        control_layout = QVBoxLayout(control_bar)
        control_layout.setContentsMargins(20, 10, 20, 10)
        
        info_layout = QHBoxLayout()
        self.song_info_label = QLabel("未播放")
        self.song_info_label.setStyleSheet("font-size: 14px; font-weight: bold; color: white; background: transparent;")
        info_layout.addWidget(self.song_info_label)
        info_layout.addStretch()
        self.artist_info_label = QLabel("")
        self.artist_info_label.setStyleSheet("font-size: 12px; color: rgba(255,255,255,0.6); background: transparent;")
        info_layout.addWidget(self.artist_info_label)
        control_layout.addLayout(info_layout)
        
        progress_layout = QHBoxLayout()
        self.current_time_label = QLabel("00:00")
        self.current_time_label.setStyleSheet("font-size: 11px; color: rgba(255,255,255,0.5); background: transparent;")
        self.progress_slider = QSlider(Qt.Horizontal)
        self.progress_slider.setRange(0, 1000)
        self.progress_slider.sliderMoved.connect(self.set_position)
        self.total_time_label = QLabel("00:00")
        self.total_time_label.setStyleSheet("font-size: 11px; color: rgba(255,255,255,0.5); background: transparent;")
        
        self.progress_slider.setStyleSheet("""
            QSlider::groove:horizontal {
                height: 4px;
                background: rgba(255,255,255,0.2);
                border-radius: 2px;
            }
            QSlider::handle:horizontal {
                background: white;
                width: 12px;
                height: 12px;
                margin: -4px 0;
                border-radius: 6px;
            }
            QSlider::sub-page:horizontal {
                background: rgba(255,255,255,0.6);
                border-radius: 2px;
            }
        """)
        
        progress_layout.addWidget(self.current_time_label)
        progress_layout.addWidget(self.progress_slider)
        progress_layout.addWidget(self.total_time_label)
        control_layout.addLayout(progress_layout)
        
        btn_layout = QHBoxLayout()
        btn_layout.setSpacing(12)
        btn_layout.setAlignment(Qt.AlignCenter)
        
        self.prev_btn = QPushButton("⏮")
        self.prev_btn.setObjectName("controlBtn")
        self.prev_btn.clicked.connect(self.prev_song)
        
        self.play_btn = QPushButton("▶")
        self.play_btn.setObjectName("controlBtn")
        self.play_btn.setFixedSize(50, 50)
        self.play_btn.clicked.connect(self.play_pause)
        
        self.next_btn = QPushButton("⏭")
        self.next_btn.setObjectName("controlBtn")
        self.next_btn.clicked.connect(self.next_song)
        
        self.volume_widget = VolumeSlider(self)
        self.volume_widget.set_volume(20)
        self.set_volume(20)
        
        self.expand_btn = QPushButton("⛶")
        self.expand_btn.setObjectName("controlBtn")
        self.expand_btn.setToolTip("展开完整播放页面")
        self.expand_btn.setStyleSheet("""
            QPushButton {
                border: none;
                background: rgba(255,255,255,0.05);
                font-size: 22px;
                padding: 10px;
                border-radius: 25px;
                color: white;
            }
            QPushButton:hover {
                background-color: rgba(255,255,255,0.15);
            }
        """)
        self.expand_btn.clicked.connect(self.toggle_expand)
        
        self.atmo_btn = QPushButton("🌤")
        self.atmo_btn.setObjectName("controlBtn")
        self.atmo_btn.setToolTip("氛围效果")
        self.atmo_btn.setStyleSheet("""
            QPushButton {
                border: none;
                background: rgba(255,255,255,0.05);
                font-size: 20px;
                padding: 10px;
                border-radius: 25px;
                color: white;
            }
            QPushButton:hover {
                background-color: rgba(255,255,255,0.15);
            }
        """)
        self.atmo_btn.clicked.connect(self.show_atmo_menu)
        
        btn_layout.addWidget(self.prev_btn)
        btn_layout.addWidget(self.play_btn)
        btn_layout.addWidget(self.next_btn)
        btn_layout.addWidget(self.volume_widget)
        btn_layout.addWidget(self.expand_btn)
        btn_layout.addWidget(self.atmo_btn)
        
        control_layout.addLayout(btn_layout)
        bg_layout.addWidget(control_bar)
        
        bottom_widget = QWidget()
        bottom_widget.setStyleSheet("background: transparent;")
        bottom_layout = QVBoxLayout(bottom_widget)
        
        title_layout = QHBoxLayout()
        title_label = QLabel("本地音乐")
        title_label.setStyleSheet("font-size: 16px; font-weight: bold; color: white; background: transparent;")
        title_layout.addWidget(title_label)
        title_layout.addStretch()
        
        self.refresh_btn = QPushButton("🔄 刷新")
        self.refresh_btn.setStyleSheet("""
            QPushButton {
                padding: 8px 16px;
                border: 1px solid rgba(255,255,255,0.2);
                border-radius: 4px;
                background-color: rgba(255,255,255,0.05);
                color: white;
            }
            QPushButton:hover {
                background-color: rgba(255,255,255,0.15);
                border-color: rgba(255,255,255,0.3);
            }
        """)
        self.refresh_btn.clicked.connect(self.refresh_music_list)
        self.refresh_btn.setEnabled(False)
        title_layout.addWidget(self.refresh_btn)
        
        self.add_folder_btn = QPushButton("📁 选择文件夹")
        self.add_folder_btn.setStyleSheet("""
            QPushButton {
                padding: 8px 16px;
                border: 1px solid rgba(255,255,255,0.2);
                border-radius: 4px;
                background-color: rgba(255,255,255,0.05);
                color: white;
            }
            QPushButton:hover {
                background-color: rgba(255,255,255,0.15);
                border-color: rgba(255,255,255,0.3);
            }
        """)
        self.add_folder_btn.clicked.connect(self.select_folder)
        title_layout.addWidget(self.add_folder_btn)
        
        self.show_hidden_btn = QPushButton("👁 显示已隐藏")
        self.show_hidden_btn.setStyleSheet("""
            QPushButton {
                padding: 8px 16px;
                border: 1px solid rgba(255,255,255,0.2);
                border-radius: 4px;
                background-color: rgba(255,255,255,0.05);
                color: white;
            }
            QPushButton:hover {
                background-color: rgba(255,255,255,0.15);
                border-color: rgba(255,255,255,0.3);
            }
        """)
        self.show_hidden_btn.clicked.connect(self.toggle_show_hidden)
        self.show_hidden_btn.setVisible(False)
        title_layout.addWidget(self.show_hidden_btn)
        
        bottom_layout.addLayout(title_layout)
        
        self.music_table = QTableWidget()
        self.music_table.setColumnCount(3)
        self.music_table.setHorizontalHeaderLabels(["歌名", "歌手", ""])
        self.music_table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.music_table.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.music_table.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents)
        self.music_table.setAlternatingRowColors(False)
        self.music_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.music_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.music_table.doubleClicked.connect(self.play_selected_song)
        self.music_table.setStyleSheet("""
            QTableWidget {
                border: none;
                background: transparent;
            }
            QTableWidget::item {
                padding: 8px;
                background: transparent;
                color: rgba(255,255,255,0.8);
            }
            QTableWidget::item:selected {
                background-color: rgba(255,255,255,0.12);
                color: white;
            }
            QHeaderView::section {
                background-color: rgba(255,255,255,0.05);
                padding: 8px;
                border: none;
                border-bottom: 1px solid rgba(255,255,255,0.1);
                font-weight: bold;
                color: rgba(255,255,255,0.6);
            }
        """)
        bottom_layout.addWidget(self.music_table)
        
        bg_layout.addWidget(bottom_widget, 1)
        main_layout.addWidget(self.bg_container)
        
        self.atmosphere = AtmosphereWidget(self)
        self.atmosphere.setGeometry(0, 0, self.width(), self.height())
        self.atmosphere.raise_()
        
    def show_atmo_menu(self):
        menu = QMenu(self)
        menu.setStyleSheet("""
            QMenu {
                background: rgba(30,30,50,0.9);
                color: white;
                border: 1px solid rgba(255,255,255,0.1);
                border-radius: 8px;
                padding: 5px;
            }
            QMenu::item {
                padding: 8px 20px;
                border-radius: 4px;
            }
            QMenu::item:selected {
                background: rgba(255,255,255,0.1);
            }
        """)
        
        off_action = QAction("☀️ 关闭", self)
        off_action.triggered.connect(self.turn_off_atmosphere)
        menu.addAction(off_action)
        menu.addSeparator()
        
        rain_action = QAction("🌧️ 下雨", self)
        rain_action.triggered.connect(self.turn_on_rain)
        menu.addAction(rain_action)
        
        snow_action = QAction("❄️ 下雪", self)
        snow_action.triggered.connect(self.turn_on_snow)
        menu.addAction(snow_action)
        
        pos = self.atmo_btn.mapToGlobal(QPoint(0, self.atmo_btn.height()))
        menu.exec_(pos)
        
    def turn_on_rain(self):
        self.atmosphere.stop()
        self.atmosphere.start_rain()
        self.atmo_btn.setText("🌧️")
        
    def turn_on_snow(self):
        self.atmosphere.stop()
        self.atmosphere.start_snow()
        self.atmo_btn.setText("❄️")
        
    def turn_off_atmosphere(self):
        self.atmosphere.stop()
        self.atmo_btn.setText("🌤")
        
    def resizeEvent(self, event):
        super().resizeEvent(event)
        if self.background_pixmap:
            self.bg_label.setGeometry(0, 0, self.bg_container.width(), self.bg_container.height())
            self.update_background()
        self.atmosphere.setGeometry(0, 0, self.width(), self.height())
    
    def toggle_expand(self):
        self.is_expanded = not self.is_expanded
        if self.is_expanded:
            if self.current_index >= 0 and self.current_index < len(self.music_list):
                music = self.music_list[self.current_index]
                self.expand_panel.update_info(
                    music['title'],
                    music['artist'],
                    music.get('album', ''),
                    music.get('cover'),
                    self.current_lyrics
                )
            self.expand_panel.show_panel()
            self.expand_btn.setText("⛶ ✕")
        else:
            self.expand_panel.hide_panel()
            self.expand_btn.setText("⛶")
    
    def setup_menu(self):
        menubar = self.menuBar()
        menubar.setStyleSheet("""
            QMenuBar {
                background: transparent;
                color: rgba(255,255,255,0.7);
                border: none;
            }
            QMenuBar::item:selected {
                background: rgba(255,255,255,0.1);
            }
            QMenu {
                background: rgba(30,30,50,0.9);
                color: white;
                border: 1px solid rgba(255,255,255,0.1);
            }
            QMenu::item:selected {
                background: rgba(255,255,255,0.1);
            }
        """)
        file_menu = menubar.addMenu("文件")
        
        open_action = QAction("打开文件夹", self)
        open_action.triggered.connect(self.select_folder)
        file_menu.addAction(open_action)
        
        refresh_action = QAction("刷新列表", self)
        refresh_action.triggered.connect(self.refresh_music_list)
        refresh_action.setShortcut("F5")
        file_menu.addAction(refresh_action)
        
        file_menu.addSeparator()
        
        bg_action = QAction("🎨 更换背景", self)
        bg_action.triggered.connect(self.choose_background)
        file_menu.addAction(bg_action)
        
        clear_bg_action = QAction("🗑 清除背景", self)
        clear_bg_action.triggered.connect(self.clear_background)
        file_menu.addAction(clear_bg_action)
        
        file_menu.addSeparator()
        
        clear_hidden_action = QAction("清空隐藏记录", self)
        clear_hidden_action.triggered.connect(self.clear_hidden_files)
        file_menu.addAction(clear_hidden_action)
        
        exit_action = QAction("退出", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
    
    def choose_background(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "选择背景图片", "",
            "图片文件 (*.png *.jpg *.jpeg *.bmp *.gif)"
        )
        if file_path:
            self.background_pixmap = QPixmap(file_path)
            self.update_background()
    
    def clear_background(self):
        self.background_pixmap = None
        self.bg_label.hide()
        self.bg_container.setStyleSheet("background: #1a1a2e;")
    
    def update_background(self):
        if self.background_pixmap:
            scaled = self.background_pixmap.scaled(
                self.bg_container.width(),
                self.bg_container.height(),
                Qt.KeepAspectRatioByExpanding,
                Qt.SmoothTransformation
            )
            self.bg_label.setPixmap(scaled)
            self.bg_label.setGeometry(0, 0, self.bg_container.width(), self.bg_container.height())
            self.bg_label.show()
            self.bg_container.setStyleSheet("background: transparent;")
        else:
            self.bg_label.hide()
            self.bg_container.setStyleSheet("background: #1a1a2e;")
        
    def apply_style(self):
        style = """
        #controlBtn {
            border: none;
            background: rgba(255,255,255,0.05);
            font-size: 24px;
            padding: 10px;
            border-radius: 25px;
            color: white;
        }
        #controlBtn:hover {
            background-color: rgba(255,255,255,0.15);
        }
        """
        self.setStyleSheet(style)
    
    def set_volume(self, volume):
        if self.player:
            if self.use_vlc:
                self.player.audio_set_volume(volume)
            else:
                self.player.setVolume(volume)
    
    def select_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "选择音乐文件夹")
        if folder:
            self.current_folder = folder
            self.load_music_from_folder(folder)
            self.refresh_btn.setEnabled(True)
    
    def refresh_music_list(self):
        if self.current_folder:
            self.load_music_from_folder(self.current_folder)
            QMessageBox.information(self, "刷新完成", f"已加载 {len(self.music_list)} 首歌曲")
        else:
            QMessageBox.information(self, "提示", "请先选择一个音乐文件夹")
    
    def load_music_from_folder(self, folder):
        self.music_list.clear()
        self.music_table.setRowCount(0)
        self.current_folder = folder
        
        for root, dirs, files in os.walk(folder):
            for file in files:
                if file.lower().endswith('.mp3'):
                    file_path = os.path.join(root, file)
                    if file_path in self.hidden_files:
                        continue
                    
                    try:
                        tags = ID3(file_path)
                        title = os.path.splitext(file)[0]
                        artist = "未知歌手"
                        album = ""
                        cover_data = None
                        lyrics = None
                        
                        if 'TIT2' in tags:
                            title = str(tags['TIT2'])
                        if 'TPE1' in tags:
                            artist = str(tags['TPE1'])
                        if 'TALB' in tags:
                            album = str(tags['TALB'])
                        
                        for tag in tags.values():
                            if isinstance(tag, APIC):
                                cover_data = tag.data
                                break
                        
                        lrc_path = os.path.splitext(file_path)[0] + '.lrc'
                        lrc_lyrics = None
                        if os.path.exists(lrc_path):
                            lrc_lyrics = parse_lrc_file(lrc_path)
                            if lrc_lyrics and len(lrc_lyrics) > 0:
                                print(f"✅ 从LRC文件读取歌词: {os.path.basename(lrc_path)} ({len(lrc_lyrics)}行)")
                                lyrics = lrc_lyrics
                        
                        if not lyrics or len(lyrics) == 0:
                            embedded = extract_embedded_lyrics(tags)
                            if embedded:
                                lines = embedded.split('\n')
                                for line in lines:
                                    line = line.strip()
                                    if line:
                                        lyrics.append({
                                            'time_ms': len(lyrics) * 3000,
                                            'text': line
                                        })
                                print(f"✅ 从嵌入标签读取歌词: {len(lyrics)}行")
                        
                        if not lyrics or len(lyrics) == 0:
                            txt_path = os.path.splitext(file_path)[0] + '.txt'
                            if os.path.exists(txt_path):
                                try:
                                    with open(txt_path, 'r', encoding='utf-8') as f:
                                        content = f.read()
                                        lines = content.split('\n')
                                        for i, line in enumerate(lines):
                                            line = line.strip()
                                            if line:
                                                lyrics.append({
                                                    'time_ms': i * 3000,
                                                    'text': line
                                                })
                                    print(f"✅ 从TXT文件读取歌词: {len(lyrics)}行")
                                except:
                                    pass
                        
                        self.music_list.append({
                            'file_path': file_path,
                            'title': title,
                            'artist': artist,
                            'album': album,
                            'cover': cover_data,
                            'lyrics': lyrics if lyrics else None
                        })
                    except Exception as e:
                        lrc_path = os.path.splitext(file_path)[0] + '.lrc'
                        lrc_lyrics = parse_lrc_file(lrc_path) if os.path.exists(lrc_path) else None
                        self.music_list.append({
                            'file_path': file_path,
                            'title': os.path.splitext(file)[0],
                            'artist': "未知歌手",
                            'album': "",
                            'cover': None,
                            'lyrics': lrc_lyrics
                        })
        
        self.update_music_list()
        self.add_folder_btn.setText(f"📁 已加载 {len(self.music_list)} 首歌曲")
        
        if len(self.hidden_files) > 0:
            self.show_hidden_btn.setVisible(True)
            self.show_hidden_btn.setText(f"👁 显示已隐藏 ({len(self.hidden_files)})")
        else:
            self.show_hidden_btn.setVisible(False)
    
    def update_music_list(self):
        self.music_table.setRowCount(len(self.music_list))
        for i, music in enumerate(self.music_list):
            self.music_table.setItem(i, 0, QTableWidgetItem(music['title']))
            self.music_table.setItem(i, 1, QTableWidgetItem(music['artist']))
            
            delete_btn = QPushButton("✕")
            delete_btn.setStyleSheet("""
                QPushButton {
                    background-color: transparent;
                    border: none;
                    color: rgba(255,255,255,0.4);
                    font-size: 16px;
                    padding: 4px 8px;
                }
                QPushButton:hover {
                    color: rgba(255,70,70,0.8);
                    background-color: rgba(255,70,70,0.1);
                    border-radius: 4px;
                }
            """)
            delete_btn.setCursor(Qt.PointingHandCursor)
            delete_btn.clicked.connect(lambda checked, row=i: self.hide_song(row))
            self.music_table.setCellWidget(i, 2, delete_btn)
    
    def hide_song(self, row):
        if row < 0 or row >= len(self.music_list):
            return
        music = self.music_list[row]
        file_path = music['file_path']
        self.hidden_files.add(file_path)
        self.save_hidden_files()
        self.music_list.pop(row)
        if self.current_index == row:
            if self.player:
                self.player.stop()
            self.current_index = -1
            self.song_info_label.setText("未播放")
            self.artist_info_label.setText("")
            self.play_btn.setText("▶")
            self.is_playing = False
        elif self.current_index > row:
            self.current_index -= 1
        self.update_music_list()
        self.add_folder_btn.setText(f"📁 已加载 {len(self.music_list)} 首歌曲")
        if len(self.hidden_files) > 0:
            self.show_hidden_btn.setVisible(True)
            self.show_hidden_btn.setText(f"👁 显示已隐藏 ({len(self.hidden_files)})")
    
    def toggle_show_hidden(self):
        if not hasattr(self, 'show_hidden_dialog'):
            self.show_hidden_dialog = QDialog(self)
            self.show_hidden_dialog.setWindowTitle("已隐藏的歌曲")
            self.show_hidden_dialog.resize(500, 400)
            self.show_hidden_dialog.setStyleSheet("""
                QDialog {
                    background: rgba(30,30,50,0.95);
                    color: white;
                }
            """)
            layout = QVBoxLayout()
            info_label = QLabel("以下歌曲已被隐藏，不会在列表中显示")
            info_label.setStyleSheet("color: rgba(255,255,255,0.6); padding: 10px;")
            layout.addWidget(info_label)
            self.hidden_list = QListWidget()
            self.hidden_list.setStyleSheet("""
                QListWidget {
                    background: transparent;
                    color: white;
                    border: 1px solid rgba(255,255,255,0.1);
                }
                QListWidget::item:selected {
                    background: rgba(255,255,255,0.1);
                }
            """)
            layout.addWidget(self.hidden_list)
            btn_layout = QHBoxLayout()
            restore_all_btn = QPushButton("恢复全部")
            restore_all_btn.setStyleSheet("""
                QPushButton {
                    padding: 8px 16px;
                    border: 1px solid rgba(255,255,255,0.2);
                    border-radius: 4px;
                    background-color: rgba(255,255,255,0.05);
                    color: white;
                }
                QPushButton:hover {
                    background-color: rgba(255,255,255,0.15);
                }
            """)
            restore_all_btn.clicked.connect(self.restore_all_hidden)
            btn_layout.addWidget(restore_all_btn)
            btn_layout.addStretch()
            close_btn = QPushButton("关闭")
            close_btn.setStyleSheet("""
                QPushButton {
                    padding: 8px 16px;
                    border: 1px solid rgba(255,255,255,0.2);
                    border-radius: 4px;
                    background-color: rgba(255,255,255,0.05);
                    color: white;
                }
                QPushButton:hover {
                    background-color: rgba(255,255,255,0.15);
                }
            """)
            close_btn.clicked.connect(self.show_hidden_dialog.accept)
            btn_layout.addWidget(close_btn)
            layout.addLayout(btn_layout)
            self.show_hidden_dialog.setLayout(layout)
        
        self.hidden_list.clear()
        for file_path in self.hidden_files:
            file_name = os.path.basename(file_path)
            item = QListWidgetItem(file_name)
            item.setData(Qt.UserRole, file_path)
            self.hidden_list.addItem(item)
        self.hidden_list.itemDoubleClicked.connect(self.restore_single_hidden)
        self.show_hidden_dialog.exec_()
    
    def restore_single_hidden(self, item):
        file_path = item.data(Qt.UserRole)
        if file_path in self.hidden_files:
            self.hidden_files.remove(file_path)
            self.save_hidden_files()
            row = self.hidden_list.row(item)
            self.hidden_list.takeItem(row)
            if len(self.hidden_files) == 0:
                self.show_hidden_btn.setVisible(False)
            else:
                self.show_hidden_btn.setText(f"👁 显示已隐藏 ({len(self.hidden_files)})")
            QMessageBox.information(self, "恢复成功", f"已恢复歌曲：{item.text()}\n点击「刷新」按钮即可显示在列表中。")
    
    def restore_all_hidden(self):
        if len(self.hidden_files) == 0:
            return
        reply = QMessageBox.question(self, "确认恢复", f"确定要恢复所有 {len(self.hidden_files)} 首隐藏的歌曲吗？", QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.hidden_files.clear()
            self.save_hidden_files()
            self.hidden_list.clear()
            self.show_hidden_btn.setVisible(False)
            QMessageBox.information(self, "恢复成功", "已恢复所有隐藏的歌曲\n点击「刷新」按钮即可显示在列表中。")
    
    def clear_hidden_files(self):
        if len(self.hidden_files) == 0:
            QMessageBox.information(self, "提示", "没有隐藏的歌曲记录")
            return
        reply = QMessageBox.question(self, "确认清空", f"确定要清空所有 {len(self.hidden_files)} 条隐藏记录吗？", QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.hidden_files.clear()
            self.save_hidden_files()
            self.show_hidden_btn.setVisible(False)
            QMessageBox.information(self, "清空成功", "已清空所有隐藏记录\n点击「刷新」按钮即可显示在列表中。")
    
    def play_selected_song(self):
        current_row = self.music_table.currentRow()
        if current_row >= 0 and current_row < len(self.music_list):
            self.current_index = current_row
            self.play_song(self.current_index)
    
    def play_song(self, index):
        if index < 0 or index >= len(self.music_list):
            return
        
        music = self.music_list[index]
        file_path = music['file_path']
        
        if not self.player:
            QMessageBox.warning(self, "错误", "没有可用的播放器")
            return
        
        if self.use_vlc and self.vlc_instance:
            media = self.vlc_instance.media_new(file_path)
            self.player.set_media(media)
            self.player.play()
        else:
            url = QUrl.fromLocalFile(file_path)
            self.player.setMedia(QMediaContent(url))
            self.player.play()
        
        self.is_playing = True
        self.play_btn.setText("⏸")
        
        self.song_info_label.setText(music['title'])
        self.artist_info_label.setText(music['artist'])
        
        lyrics = music.get('lyrics')
        self.current_lyrics = lyrics if isinstance(lyrics, list) and len(lyrics) > 0 else []
        
        print(f"🎵 播放: {music['title']} - 歌词行数: {len(self.current_lyrics)}")
        
        if self.is_expanded:
            self.expand_panel.update_info(
                music['title'],
                music['artist'],
                music.get('album', ''),
                music.get('cover'),
                self.current_lyrics
            )
        
        self.music_table.selectRow(index)
        self.setWindowTitle(f"{music['title']} - 音乐播放器")
    
    def play_pause(self):
        if self.current_index < 0:
            if len(self.music_list) > 0:
                self.current_index = 0
                self.play_song(0)
            return
        
        if not self.player:
            return
        
        if self.is_playing:
            self.player.pause()
            self.is_playing = False
            self.play_btn.setText("▶")
        else:
            self.player.play()
            self.is_playing = True
            self.play_btn.setText("⏸")
    
    def prev_song(self):
        if len(self.music_list) == 0:
            return
        self.current_index = (self.current_index - 1) % len(self.music_list)
        self.play_song(self.current_index)
    
    def next_song(self):
        if len(self.music_list) == 0:
            return
        self.current_index = (self.current_index + 1) % len(self.music_list)
        self.play_song(self.current_index)
    
    def update_progress(self):
        if self.is_playing and self.player:
            try:
                if self.use_vlc:
                    length = self.player.get_length()
                    position = self.player.get_time()
                else:
                    length = self.player.duration()
                    position = self.player.position()
                    if length > 0:
                        position = int(position * length)
                if length > 0 and position >= 0:
                    self.progress_slider.setValue(int(position / length * 1000))
                    self.current_time_label.setText(self.format_time(position))
                    self.total_time_label.setText(self.format_time(length))
                    
                    if self.is_expanded:
                        self.expand_panel.update_lyric_highlight(position)
            except:
                pass
    
    def set_position(self, value):
        if not self.player:
            return
        try:
            if self.use_vlc:
                length = self.player.get_length()
                if length > 0:
                    position = int(value / 1000 * length)
                    self.player.set_time(position)
            else:
                length = self.player.duration()
                if length > 0:
                    position = int(value / 1000 * length)
                    self.player.setPosition(position)
        except:
            pass
    
    def format_time(self, ms):
        seconds = ms // 1000
        minutes = seconds // 60
        seconds = seconds % 60
        return f"{minutes:02d}:{seconds:02d}"


def main():
    print("启动音乐播放器...")
    app = QApplication(sys.argv)
    app.setApplicationName("音乐播放器")
    
    # 设置图标
    icon_path = os.path.join(get_base_dir(), "icon.ico")
    if os.path.exists(icon_path):
        app.setWindowIcon(QIcon(icon_path))
    
    print("创建主窗口...")
    player = MusicPlayer()
    print("显示窗口...")
    player.show()
    player.raise_()
    print("进入事件循环...")
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()