from flask import Flask, request, jsonify
import base64
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/upload", methods=["POST"])
def upload_image():
    data = request.get_json()
    image_data = data["image"]

    if not image_data.startswith("data:image"):
        return jsonify({"message": "Invalid image format"}), 400

    header, encoded = image_data.split(",", 1)
    image_bytes = base64.b64decode(encoded)

    file_path = os.path.join(UPLOAD_FOLDER, "photo.png")
    with open(file_path, "wb") as f:
        f.write(image_bytes)

    return jsonify({"message": "Image saved successfully!"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
