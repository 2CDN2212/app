import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
)
from PyQt5.QtGui import QPixmap
import webbrowser
from PyQt5.QtCore import Qt

# 筋肉部位ごとの筋トレ方法のリンクと画像パス
MUSCLE_WORKOUT_DATA = {
    "回鍋肉": {"url": "https://delishkitchen.tv/recipes/147726740259602726", "image": "C:\\Users\\81704\\Downloads\\回鍋肉.png"},
"カルボナーラ": {"url": "https://www.nichireifoods.co.jp/media/28762/", "image": "C:\\Users\\81704\\Downloads\\カルボナーラ.png"},
    "おにぎり": {"url": "https://oceans-nadia.com/recipe_list/2271", "image": "C:\\Users\\81704\\Downloads\\おにぎり.png"},
    "北京ダック": {"url": "https://oceans-nadia.com/user/146865/recipe/372722", "image": "C:\\Users\\81704\\Downloads\\北京ダック.png"}
}

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("マイレシピ")
        self.setGeometry(100, 100, 500, 600)
        
        layout = QVBoxLayout()
        
        # 筋肉画像のラベル
        self.image_label = QLabel(self)
        layout.addWidget(self.image_label, alignment=Qt.AlignTop)  # 中央上部に配置
        self.update_image_and_url("回鍋肉")  # デフォルト画像を設定

        # ボタンで筋肉部位を切り替える
        self.next_button = QPushButton("次の料理")
        self.next_button.clicked.connect(self.next_muscle)
        layout.addWidget(self.next_button)

        # 検索ボタン
        self.search_button = QPushButton("レシピを見る")
        self.search_button.clicked.connect(self.open_workout_url)
        layout.addWidget(self.search_button)

        self.setLayout(layout)

        # 筋肉部位のリストと現在のインデックス
        self.muscles = list(MUSCLE_WORKOUT_DATA.keys())
        self.current_index = 0

    def update_image_and_url(self, muscle):
        """選択された筋肉の画像とURLを更新"""
        self.current_muscle = muscle
        pixmap = QPixmap(MUSCLE_WORKOUT_DATA[muscle]["image"])
        self.image_label.setPixmap(pixmap.scaled(500, 500))  # 画像をリサイズ

    def next_muscle(self):
        """次の筋肉を表示"""
        self.current_index = (self.current_index + 1) % len(self.muscles)
        self.update_image_and_url(self.muscles[self.current_index])

    def open_workout_url(self):
        """選択された筋肉のURLを開く"""
        url = MUSCLE_WORKOUT_DATA[self.current_muscle]["url"]
        webbrowser.open(url)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())
