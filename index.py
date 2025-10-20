from flask import Flask
app = Flask(__name__) # __name__ Flask裡的套件，代表目前執行的模組，若該程式為主程式，則 name = main

@app.route("/") # @為函式的裝飾 (Decorator)：以函式為基礎，提供附加的功能
def home():
    return "Hello Flask"

@app.route("/test") #代表我們要處理的網站路徑
def test():
    return "Test Flask"

# if __name__ == "__main__": # 如果以主程式執行
#     app.run() # 立刻啟動伺服器