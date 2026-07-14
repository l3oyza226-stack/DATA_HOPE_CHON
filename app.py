import os
from flask import Flask, render_template

app = Flask(__name__)

@app.after_request
def add_no_cache(response):
    # ป้องกันเบราว์เซอร์ Cache ไฟล์ HTML เพื่อให้โหลดเวอร์ชันล่าสุดเสมอ
    if response.content_type and 'text/html' in response.content_type:
        response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '0'
    return response

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)