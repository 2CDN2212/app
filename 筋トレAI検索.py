import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QRadioButton, QPushButton, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import openai
import webbrowser

# OpenAI APIキーを設定
openai.api_key = 'YOUR_API_KEY'

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("マイ筋トレメニューポータル")
        self.setGeometry(100, 100, 400, 500)
        
        main_layout = QVBoxLayout()
        self.label = QLabel("選択した筋肉部位の筋トレ方法を表示します。")
        main_layout.addWidget(self.label)

        self.image_label = QLabel(self)
        pixmap = QPixmap("C:\\Users\\81704\\Downloads\\筋肉.png")  # 画像のパスを指定
        self.image_label.setPixmap(pixmap)
        main_layout.addWidget(self.image_label)

        # ラジオボタンを左、中央、右に分けるためのレイアウト
        grid_layout = QGridLayout()
        self.radio_buttons = []

        # 左列
        left_muscles = ["胸鎖乳突筋","大胸筋", "上腕二頭筋", "前鋸筋", "外腹斜筋", "腹直筋", "内転筋群", "大腿四頭筋", "前脛骨筋"]
        for i, muscle in enumerate(left_muscles):
            radio_button = QRadioButton(muscle)
            self.radio_buttons.append(radio_button)
            grid_layout.addWidget(radio_button, i, 0)

        # 中央列
        center_muscles = ["僧帽筋", "三角筋", "広背筋", "前腕伸筋群", "前腕屈筋群", "下腿三頭筋",]
        for i, muscle in enumerate(center_muscles):
            radio_button = QRadioButton(muscle)
            self.radio_buttons.append(radio_button)
            grid_layout.addWidget(radio_button, i, 1)

        # 右列
        right_muscles = ["棘下筋", "上腕三頭筋", "脊柱起立筋", "大臀筋", "ハムストリングス",]
        for i, muscle in enumerate(right_muscles):
            radio_button = QRadioButton(muscle)
            self.radio_buttons.append(radio_button)
            grid_layout.addWidget(radio_button, i, 2)

        main_layout.addLayout(grid_layout)

        # 検索ボタン
        self.search_button = QPushButton("表示")
        self.search_button.clicked.connect(self.display_workout_url)
        main_layout.addWidget(self.search_button)

        self.result_label = QLabel("")
        main_layout.addWidget(self.result_label)

        self.setLayout(main_layout)

    def display_workout_url(self):
        # 選択された筋肉部位を取得
        selected_muscle = None
        for radio_button in self.radio_buttons:
            if radio_button.isChecked():
                selected_muscle = radio_button.text()
                break
        
        if not selected_muscle:
            self.result_label.setText("筋肉部位を選択してください。")
            return

        # OpenAI APIを使用して検索クエリを送信
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"{selected_muscle}の筋トレ方法を教えてください。",
            max_tokens=100
        )

        # 取得した結果を表示
        url = response.choices[0].text.strip()
        if "http" in url:
            self.result_label.setText(f'<a href="{url}">筋トレ方法: {url}</a>')
            self.result_label.setTextFormat(Qt.RichText)
            self.result_label.setTextInteractionFlags(Qt.TextBrowserInteraction)
            self.result_label.setOpenExternalLinks(True)
        else:
            self.result_label.setText(f"筋トレ方法: {url}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())
