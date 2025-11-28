from flask import Flask
from flask import request # 載入 Request 物件
from flask import redirect # 載入 Redirect 函式
from flask import render_template # 載入 render_template 函式
from flask import session # 從 flask 套件載入 session 函式，接著還要多設定 secret key
from urllib.parse import unquote
import json
# __name__ Flask裡的套件，代表目前執行的模組，若該程式為主程式，則 name = main
# 可以設定靜態檔案處理
app = Flask(
    __name__,
    static_folder="public", # 將 static 資料夾改名成 public
    static_url_path="/"
    ) 
# 因應 session 的建立，設定 session 密鑰，為一個任意字串，但不能讓其他人知道
app.secret_key= "any string but secret"

# @為函式的裝飾 (Decorator)：以函式為基礎，提供附加的功能
# 同時使用 GET 與 POST ，方法，建立路徑 / 對應的處理函式，而不寫 methods 則預設 GET 方法
@app.route("/", methods=["GET","POST"]) # 用來回應 / 的處理函式
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
    # lang = request.headers.get("accept-language")
    # if(lang.startswith("en")): 
    #     # 將使用者依據語言作一個目錄的導向 
    #     return redirect("/en/")
    # else:
    #     # 將使用者依據語言作一個目錄的導向 
    #     return redirect("/zh/")
    # 直接看 templates 資料夾底下檔案，所以直接輸入檔案名稱，也可帶入變數資料
    return render_template("index.html")

#利用 GET 方法要求字串 Query String 提供彈性
@app.route("/caculate", methods=["GET"])
def getSum(): # min+ (min+1)+(min+2)+(min+3)+...+max
    minNumber = request.args.get("min",1) # 預設值為1
    minNumber = int(minNumber)
    maxNumber = request.args.get("max",1) # 預設值為100
    maxNumber = int(maxNumber) # 要將資料型別作轉換，因為輸入的是字串
    result = 0
    for n in range(minNumber,maxNumber+1):
        result += n
    return render_template("result.html", finalResult = str(result))

# 使用 GET 方法處理路徑 /hello?name=使用者名字
# 應用 session
@app.route("/hello")
def hello():
    name = request.args.get("name", " ") 
    session["username"] = name # session["欄位名稱"] = 資料
    return "你好, " + name

# 使用 GET 方法處理路徑 /talk
@app.route("/talk")
def talk():
    name = session["username"]
    return name + ", 很高興認識你"

# 利用 POST 方法處理路徑 /show 的對應函式
@app.route("/show", methods=["POST"])
def show():
    name = request.form["name"]
    return "歡迎光臨, " + name

# 處理路徑 page
@app.route("/page")
def  page():
    return render_template("page.html")

# 建立 Application 物件，設定靜態檔案的路徑處理


# 針對導向過來的語言網址
@app.route("/en/")
def index_english():
    # 利用 json.dumps()將字典資料轉換成字串並傳送到前端
    return json.dumps({
            "status":"ok",
            "text":"Hello Flask"
            })
@app.route("/zh/")
def index_chinese():
    return json.dumps({
            "status":"ok",
            "text":"您好，歡迎光臨"
            }, ensure_ascii=False) # 指示不要使用 ASCII 編碼處理中文


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