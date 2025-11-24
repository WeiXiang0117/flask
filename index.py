from flask import Flask
from flask import request # 載入 Request 物件
from urllib.parse import unquote
# __name__ Flask裡的套件，代表目前執行的模組，若該程式為主程式，則 name = main
# 可以設定靜態檔案處理
app = Flask(
    __name__,
    static_folder="public", # 將 static 資料夾改名成 public
    static_url_path="/www"
    ) 


# @為函式的裝飾 (Decorator)：以函式為基礎，提供附加的功能
# 建立路徑 / 對應的處理函式
@app.route("/") # 用來回應 / 的處理函式
def home():
    # print("請求的方法", request.method)
    # print("通訊的協定", request.scheme)
    # print("主機的名稱", request.host)
    # print("路徑", request.path)
    # print("完整的網址", request.url)
    # print("瀏覽器和作業系統", request.headers.get("user-agent")) # 利用 request 裡的 header 屬性來呼叫底下的 get 方法，以取得 user-agent
    # print("使用者語言偏好", request.headers.get("accept-language"))
    # print("從哪裡導向這裡的網址", request.headers.get("referrer"))
    # 根據使用者語言偏好來決定呈現什麼內容
    lang = request.headers.get("accept-language")
    if(lang.startswith("en")):            
        return "Hello Flask" 
    else:
        return "您好，歡迎光臨"

# 建立路徑 /data 對應的處理函式
@app.route("/data")
def handleData(): # 函式名稱沒有固定，僅需寫在裝飾器下方
    return "My Data"

# 建立路徑 /test 對應的處理函式
@app.route("/test") #代表我們要處理的網站路徑
def test():
    return "Test Flask"

# 建立動態路由：建立路徑 /user/使用者名稱 對應的處理函式
@app.route("/user/<username>") # <名字可自訂>
def handleUsername(username):
    username = unquote(username, encoding="utf-8") # 利用 unquote 解決中文編碼問題
    if username == "偉翔":
        return "歡迎回家 " + username
    else:
        return "Hello " + username

# 啟動本機伺服器，可以用 port 來指定開啟埠號
if __name__ == "__main__": # 如果以主程式執行
    app.run(port=3000,debug=True) # 立刻啟動伺服器，此為做測試使用