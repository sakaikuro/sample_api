# coding: utf-8
from flask import Flask, request, render_template
import time
import requests
import mysql.connector

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/post", methods=["POST"])
def post():
    # 推論APIにリクエスト
    image_path = request.form["image_path"]
    request_timestamp = round(time.time())  # UNIX時間
    url = "http://test_api:5002/"
    payload = {"image_path": image_path}
    r = requests.post(url, payload)
    r = r.json()
    response_timestamp = round(time.time())  # UNIX時間
    success = r["success"]
    message = r["message"]
    if success == "true":
        class_label = r["estimated_data"]["class"]
        confidence = r["estimated_data"]["confidence"]
    else:
        class_label = "NULL"
        confidence = "NULL"

    # データベースに保存
    db_connect = mysql.connector.connect(
        host="test_mysql",
        port="3306",
        user="root",
        password="root",
        database="ai",
        auth_plugin='mysql_native_password'
    )
    db_curs = db_connect.cursor()
    sql = f"""
    INSERT INTO ai_analysis_log(
        image_path,
        success,
        message,
        class,
        confidence,
        request_timestamp,
        response_timestamp
    ) VALUES (
        "{image_path}",
        "{success}",
        "{message}",
        {class_label},
        {confidence},
        {request_timestamp},
        {response_timestamp}
    )
    """
    db_curs.execute(sql)
    db_connect.commit()
    db_connect.close()

    return render_template(
        "index.html", message=message, class_label=class_label, confidence=confidence
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
