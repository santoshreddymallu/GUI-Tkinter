import io
import webbrowser
import requests
from tkinter import *
from urllib.request import urlopen
from PIL import ImageTk, Image
from datetime import datetime

class NewsApp:

    def __init__(self):
        today = datetime.now().strftime('%Y-%m-%d')

        # Fetch today's headlines from NewsAPI
        try:
            response = requests.get(
                f'https://newsapi.org/v2/top-headlines?country=in&from={today}&to={today}&sortBy=publishedAt&apiKey=07ce6431517e45c5b04b589c36e5bed6'
            )
            self.data = response.json()
            self.articles = self.data.get('articles', [])
        except:
            self.articles = []

        # Use sample news if no API articles found
        if not self.articles:
            self.articles = self.get_sample_news()

        self.index = 0
        self.root = Tk()
        self.setup_gui()
        self.load_news_item(self.index)
        self.root.mainloop()

    def setup_gui(self):
        self.root.title("Today's News - India")
        self.root.geometry('350x600')
        self.root.resizable(False, False)
        self.root.configure(background='black')

    def clear_screen(self):
        for widget in self.root.pack_slaves():
            widget.destroy()

    def load_news_item(self, index):
        self.clear_screen()

        article = self.articles[index]

        # Load image
        try:
            img_url = article['urlToImage']
            raw_data = urlopen(img_url).read()
        except:
            img_url = 'https://www.hhireb.com/wp-content/uploads/2019/08/default-no-img.jpg'
            raw_data = urlopen(img_url).read()

        image = Image.open(io.BytesIO(raw_data)).resize((350, 250))
        photo = ImageTk.PhotoImage(image)

        img_label = Label(self.root, image=photo, bg='black')
        img_label.image = photo
        img_label.pack()

        # Title
        title = Label(
            self.root,
            text=article.get('title', 'No Title'),
            bg='black',
            fg='white',
            wraplength=330,
            justify='center',
            font=('verdana', 14, 'bold')
        )
        title.pack(pady=(10, 15))

        # Description
        description = Label(
            self.root,
            text=article.get('description', 'No description available.'),
            bg='black',
            fg='white',
            wraplength=330,
            justify='center',
            font=('verdana', 11)
        )
        description.pack(pady=(0, 15))

        # Buttons
        btn_frame = Frame(self.root, bg='black')
        btn_frame.pack(pady=20)

        if index > 0:
            Button(btn_frame, text='⟨ Prev', width=10, command=lambda: self.load_news_item(index - 1)).pack(side=LEFT, padx=5)

        Button(btn_frame, text='Read More', width=12, command=lambda: self.open_article(article['url'])).pack(side=LEFT, padx=5)

        if index < len(self.articles) - 1:
            Button(btn_frame, text='Next ⟩', width=10, command=lambda: self.load_news_item(index + 1)).pack(side=LEFT, padx=5)

    def open_article(self, url):
        webbrowser.open(url)

    def get_sample_news(self):
        return [
            {
                "title": "India wins series against England 3-2",
                "description": "India clinched the ODI series 3-2 with a thrilling win in the final match at Wankhede.",
                "urlToImage": "https://images.moneycontrol.com/static-mcnews/2023/01/Indian-Cricket-Team-770x433.jpg",
                "url": "https://www.espncricinfo.com/series/india-vs-england-2024-25-1379367"
            },
            {
                "title": "ISRO to launch Chandrayaan-4 in 2025",
                "description": "ISRO announced plans for its next lunar mission, aiming for a south pole landing.",
                "urlToImage": "https://cdn.zeebiz.com/sites/default/files/2023/08/23/253916-chandrayaan-3-landing.jpg",
                "url": "https://www.isro.gov.in/"
            },
            {
                "title": "India lifts T20 World Cup 2024 trophy!",
                "description": "India defeats Australia in a thrilling final to win the T20 World Cup 2024.",
                "urlToImage": "https://cricfit.com/wp-content/uploads/2024/06/India-T20-World-Cup-2024.jpg",
                "url": "https://www.icc-cricket.com/"
            }
        ]


# Run the app
NewsApp()
