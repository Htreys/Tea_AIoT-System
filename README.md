# 基于实时图像处理技术的茶叶病害监测物联网系统描述文档

## 功能描述
### （1）算法描述
本项目采用基于深度学习的卷积神经网络（CNN）模型进行茶叶病虫害的识别和分类。首先，通过摄像头实时捕捉茶叶叶片的图像，并将图像进行预处理，包括缩放、裁剪和归一化等操作，以满足模型输入的要求。接着，将预处理后的图像输入到预先训练好的CNN模型中，模型通过多层卷积、池化和全连接层对图像特征进行提取和学习，最后通过Softmax层输出每个类别的概率分布，从而实现对茶叶病虫害的自动识别和分类。为了提高模型的识别准确性，我们在训练阶段采用了大量标注好的茶叶病虫害图像数据进行监督学习，并通过数据增强、模型正则化等技术防止过拟合，确保模型具有良好的泛化能力。
### （2）工程展示页面功能描述
工程展示界面是一个基于Vue.js框架开发的前端应用，主要包括以下功能：
1. 实时视频流展示：界面中嵌入了一个视频播放器，能够实时显示从摄像头捕捉到的茶叶叶片图像，为用户提供直观的监测体验。
2. 预测结果展示：在视频流的下方，展示了深度学习模型对当前帧图像的预测结果，包括病虫害的类别和相应的置信度，帮助用户快速了解茶叶的健康状况。
3. 参数展示：在界面的右侧，展示了一些相关的参数和设置选项，如摄像头的分辨率、帧率等，用户可以根据需要进行调整。
4. 历史记录：界面还提供了一个历史记录功能，用户可以查看过去一段时间内的监测结果和相关参数，方便进行数据分析和回溯。
5. 报警与通知：当系统检测到严重的病虫害时，会通过界面弹窗或发送邮件等方式及时通知用户，帮助用户采取相应的防治措施。
通过这个展示界面，用户可以实时监控茶叶的健康状况，快速识别和处理病虫害问题，提高茶叶的产量和品质。

## 技术描述
### （1）技术栈描述
1. **深度学习框架**: TensorFlow和Keras
   - 用于构建和训练深度学习模型，进行茶叶病虫害的分类识别。
2. **编程语言**: Python
   - 用于编写深度学习模型、数据预处理、模型训练和结果预测的脚本。
3. **前端框架**: Vue.js
   - 用于构建用户界面，展示实时监测的视频流和模型的预测结果。
4. **后端框架**: Flask
   - 用于搭建服务端，处理前端发送的来的视频数据帧，并调用深度学习模型进行预测，并将结果返回给前端。
5. **数据库**: SQLite（或其他轻量级数据库）
   - 用于存储历史监测数据，为用户提供数据分析的基础。
6. **消息传递协议**: MQTT
   - 用于实现设备间的通信，将监测数据发送到服务器，也可用于实现报警机制。
### （2）技术设计
1. **深度学习模型设计**:
   - 使用卷积神经网络（CNN）进行图像分类。
   - 采用数据增强技术来增加训练数据的多样性，提高模型的泛化能力。
   - 使用迁移学习，基于预训练的大型网络（如ResNet或VGG）进行微调，提高训练效率和模型性能。
2. **数据预处理**:
   - 对采集到的茶叶图像进行裁剪、缩放和归一化等预处理操作，使其符合模型输入的要求。
3. **实时监测与预测**:
   - 利用摄像头实时捕捉茶叶图像，并将图像发送到服务器。
   - 服务器接收图像数据，调用深度学习模型进行预测，并将结果返回给前端展示。
4. **前端展示**:
   - 使用Vue.js构建单页面应用（SPA），实时展示视频流和预测结果。
   - 提供用户友好的界面，展示实时监测的视频流、模型的预测结果以及相关参数设置。
5. **后端服务**:
   - 使用Flask搭建后端服务器，处理前端的请求，调用深度学习模型进行预测，并管理数据库。
   - 提供RESTful API，供前端调用。
6. **数据库设计**:
   - 存储历史监测数据，包括图像、预测结果和时间戳等信息。
   - 提供数据查询接口，供用户进行数据分析。
7. **通信与报警**:
   - 使用MQTT协议实现设备间的通信。
   - 当检测到严重的病虫害时，通过MQTT协议发送报警消息，及时通知用户。
通过这套技术栈和技术设计，项目实现了茶叶病虫害的实时监测和分类识别，提供了直观的前端展示界面，并具备数据存储和分析的能力，为用户提供了一个全面、高效、易用的病虫害监测解决方案。
### （3）项目架构图
![image](https://github.com/Htreys/Tea_AIoT-System/assets/135318117/684851c4-5ead-40b2-8c77-c99a0ed5d583)


## 效果展示及描述
展示页面效果图：<br />![image.png](https://cdn.nlark.com/yuque/0/2023/png/32406294/1699006690159-b7107c03-77c8-4ba6-8275-f3ebf55710a2.png#averageHue=%232f3a4b&clientId=ud024216f-1a6d-4&from=paste&height=617&id=u7ca14c0a&originHeight=1080&originWidth=1821&originalType=binary&ratio=1.75&rotation=0&showTitle=false&size=1915669&status=done&style=none&taskId=u733bb92d-d46a-4715-b6c6-035888ed373&title=&width=1040.5714285714287)
1. **实时视频流展示区域**：
   - 视频播放器的位置显著，用户能够轻松查看实时图像。
   - 视频可以提供非常直观的用户体验。
2. **预测结果区域**：
   - “bird eye spot”旁边的百分比数值（78.766%）清晰展示了模型对于当前图像的预测结果和置信度，对于用户了解茶叶病害情况很有帮助。
3. **参数展示区域**：
   - 提供了调整摄像头设置的滑块（如分辨率和帧率），这让用户可以根据需要调整，非常贴心。
   - 显示计时器，可能是表示从监测开始到当前的时间，这样的实时数据对于监控来说非常有用。
4. **病害识别指标条**：
   - 以条形图的形式展示各种病害的发生次数，用户可以一目了然地看出哪种病害的发生的可能性最高，并及时做出决策来杜绝病害。
5. **整体风格和布局**：
   - 界面风格统一，蓝黑色基调符合工业和技术应用的通常设计。
   - 布局合理，各功能区的分布均衡，遵循了“F”形阅读规律。
6. **界面风格**：
   - 确保了界面的响应性，以便在不同尺寸的屏幕和设备上都有良好的显示效果。
   - 考虑用户操作的流程，确保从用户角度出发，简化操作步骤，提升用户体验。
