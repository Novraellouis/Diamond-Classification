from flask import Flask, render_template, request
from keras.models import load_model
from PIL import Image
import numpy as np

app = Flask(__name__)

# Load your Keras model here
model = load_model('model/proyek_model.h5')  # Ganti dengan path menuju model Anda
class_names = ['cushion', 'emerald', 'heart', 'marquise', 'oval', 'pear', 'princess', 'round']  # Ganti dengan nama kelas Anda

# Fungsi untuk melakukan prediksi dari gambar yang diunggah
def predict(image):
    # Praproses gambar untuk mempersiapkan input model
    img = Image.open(image)
    img = img.resize((256, 256))  # Sesuaikan dengan ukuran input model
    img = np.array(img) / 255.0  # Normalisasi
    img = np.expand_dims(img, axis=0)

    # Lakukan prediksi menggunakan model
    prediction = model.predict(img)
    predicted_class = np.argmax(prediction)
    result = class_names[predicted_class]

    return result, prediction

# Hitung akurasi dari prediksi
def calculate_accuracy(predictions, true_class_index):
    predicted_class = np.argmax(predictions)
    accuracy = 1 if predicted_class == true_class_index else 0
    return accuracy

@app.route('/')
def upload_file():
    return render_template('index.html')  # Ganti dengan nama file HTML Anda

@app.route('/uploader', methods=['POST'])
def upload_image():
    if request.method == 'POST':
        f = request.files['file']
        result, predictions = predict(f)
        true_class_index = 0  # Ganti dengan indeks kelas yang benar dari gambar yang diunggah
        accuracy = calculate_accuracy(predictions, true_class_index)

        return f'Predicted class: {result}<br>Accuracy: {accuracy}'

if __name__ == '__main__':
    app.run(debug=True)
