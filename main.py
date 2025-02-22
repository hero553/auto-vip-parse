import sys
import webbrowser
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, 
                           QVBoxLayout, QHBoxLayout, QWidget, QLineEdit, QMessageBox)
from PyQt6.QtCore import Qt

class VideoPlayer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('视频播放器')
        self.setGeometry(100, 100, 600, 200)
        
        # 创建主窗口部件和布局
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout()
        
        # 创建按钮布局
        button_layout = QHBoxLayout()
        
        # 创建视频平台按钮
        iqiyi_btn = QPushButton('爱奇艺')
        tencent_btn = QPushButton('腾讯视频')
        youku_btn = QPushButton('优酷视频')
        
        # 添加按钮到布局
        button_layout.addWidget(iqiyi_btn)
        button_layout.addWidget(tencent_btn)
        button_layout.addWidget(youku_btn)
        
        # 创建输入框和播放按钮
        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText('请输入视频链接')
        play_btn = QPushButton('播放VIP视频')
        
        # 连接按钮信号
        iqiyi_btn.clicked.connect(lambda: self.open_website('https://www.iqiyi.com'))
        tencent_btn.clicked.connect(lambda: self.open_website('https://v.qq.com'))
        youku_btn.clicked.connect(lambda: self.open_website('https://www.youku.com'))
        play_btn.clicked.connect(self.play_video)
        
        # 添加所有部件到主布局
        layout.addLayout(button_layout)
        layout.addWidget(self.url_input)
        layout.addWidget(play_btn)
        
        main_widget.setLayout(layout)
    
    def open_website(self, url):
        webbrowser.open(url)
    
    def play_video(self):
        url = self.url_input.text().strip()
        if not url:
            QMessageBox.warning(self, '警告', '请输入播放链接！')
            return
            
        # 验证URL是否来自支持的视频平台
        supported_platforms = [
            'iqiyi.com',
            'v.qq.com',
            'youku.com'
        ]
        
        if not any(platform in url.lower() for platform in supported_platforms):
            QMessageBox.warning(self, '警告', '请输入爱奇艺、腾讯视频或优酷视频的链接！')
            return
            
        # 拼接解析接口URL
        vip_parse_url = f'https://jx.xmflv.com/?url={url}'
        webbrowser.open(vip_parse_url)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    player = VideoPlayer()
    player.show()
    sys.exit(app.exec())