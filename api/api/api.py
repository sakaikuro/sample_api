# coding: utf-8
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/", methods=["POST"])
def post_json():
    try:
        image_path = request.form["image_path"]
        assert image_path == "/image/d03f1d36ca69348c51aa/c413eac329e1c0d03/test.jpg"
        # 【実装】image_pathを元にストレージから画像を取得
        # 【実装】取得した画像を推論
        class_label = 3
        confidence = 0.8683

        result = {
            "success": "true",
            "message": "success",
            "estimated_data": {"class": class_label, "confidence": confidence},
        }
        return jsonify(result)

    except Exception:
        result = {"success": "false", "message": "Error:E50012", "estimated_data": {}}
        return jsonify(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
