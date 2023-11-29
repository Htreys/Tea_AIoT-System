from flask import Flask, request, jsonify
from flask_cors import CORS
from tensorflow.keras.models import load_model
from tensorflow.nn import softmax
import numpy as np
from PIL import Image
import io

app = Flask(__name__)
# CORS(app, resources={r"/api/*": {"origins": ["http://localhost:8080", "http://127.0.0.1:8080"]}})
CORS(app, resources={r"/api/*": {"origins": "*"}})  # 允许所有源

model = load_model('/Users/liuzhaolong/Desktop/tea_disease_model')
class_names = ['Anthracnose', 'algal leaf', 'bird eye spot', 'brown blight', 'gray light', 'healthy', 'red leaf spot', 'white spot']


# 修改了路由前缀，确保它与前端代理配置一致
@app.route('/api/predict', methods=['POST'])
def predict():
    img_file = request.files['frame']
    if img_file:
        # 将图像文件读入为 PIL Image 对象
        img = Image.open(io.BytesIO(img_file.read()))

        # 确保图像只有三个通道（RGB）
        if img.mode != 'RGB':
            img = img.convert('RGB')

        # 进行图像预处理
        img = img.resize((224, 224))  # 假设您的模型需要 180x180 图像大小
        img_array = np.array(img)
        img_array = img_array / 255.0  # 归一化图像数据
        img_array = np.expand_dims(img_array, axis=0)  # 添加 batch 维度

        # 进行预测
        predictions = model.predict(img_array)
        pred_class = np.argmax(predictions, axis=1)
        # confidence = np.max(predictions)
        confidence = np.max(softmax(predictions, axis=1))

        # 获取类别名称
        label = class_names[pred_class[0]] if confidence >= 0.5 else 'none leaf'

        # 返回预测结果
        return jsonify({'class': label, 'confidence': float(confidence)})

    else:
        return jsonify({'error': 'No frame received'}), 400

    @app.route('/api/predict', methods=['GET'])
    def predict_get():
        return jsonify({"message": "Please use POST request to send data."})


if __name__ == '__main__':
    app.run(debug=True)
