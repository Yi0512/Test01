# 花卉图像分类项目 - 使用指南

## 📁 项目结构

```
Test01/
├── README.md                    # 项目说明（详细版）
├── USAGE.md                     # 本文件（快速使用）
├── flower_config.yaml           # 训练配置文件
│
├── 🐍 Python 脚本
├── train.py                     # 训练脚本
├── eval.py                      # 评估脚本
├── infer.py                     # 推理脚本
├── quick_start.py               # 一键快速开始
│
├── 🔧 Shell 脚本
├── train.sh                     # 训练（Shell版）
├── eval.sh                      # 评估（Shell版）
├── infer.sh                     # 推理（Shell版）
│
├── 📂 数据目录（需要自己创建）
├── dataset/
│   ├── train/
│   │   ├── rose/               # 玫瑰训练集
│   │   ├── sunflower/          # 向日葵训练集
│   │   └── tulip/              # 郁金香训练集
│   └── val/
│       ├── rose/               # 玫瑰验证集
│       ├── sunflower/          # 向日葵验证集
│       └── tulip/              # 郁金香验证集
│
└── output/                      # 训练输出（自动生成）
```

---

## 🚀 快速开始（3种方式）

### 方式一：使用 Python 脚本（推荐小白）

```bash
# 1. 训练
python train.py

# 2. 评估
python eval.py --model ./output/MobileNetV3_small_x1_0/best_model

# 3. 预测单张图片
python infer.py --image ./dataset/val/rose/sample.jpg

# 4. 批量预测整个文件夹
python infer.py --image ./dataset/val/
```

### 方式二：使用 Shell 脚本（Linux/Mac）

```bash
# 1. 训练
bash train.sh

# 2. 评估
bash eval.sh ./output/MobileNetV3_small_x1_0/best_model

# 3. 推理
bash infer.sh ./dataset/val/rose/sample.jpg ./output/MobileNetV3_small_x1_0/best_model
```

### 方式三：使用快速开始脚本（全自动，最简单）

```bash
# 交互式菜单
python quick_start.py
```

输出：
```
请选择操作：
1. 🚀 训练模型
2. 📊 评估模型
3. 🖼️  图片分类
4. 📈 启动可视化（VisualDL）
5. 🔄 完整流程（训练 → 评估 → 预测）

请输入选项（1-5）：
```

---

## 📊 详细命令参考

### 训练命令

**基础训练：**
```bash
python train.py
```

**自定义参数训练（不修改配置文件）：**
```bash
cd PaddleClas
python tools/train.py \
  -c ../flower_config.yaml \
  -o Global.epochs=50 \
  -o TRAIN.batch_size=32 \
  -o Optimizer.lr.learning_rate=0.001
cd ..
```

### 评估命令

**评估最佳模型：**
```bash
python eval.py
```

**评估指定模型：**
```bash
python eval.py --model ./output/MobileNetV3_small_x1_0/latest
```

### 推理命令

**单张图片：**
```bash
python infer.py --image ./test_image.jpg
```

**批量预测：**
```bash
python infer.py --image ./dataset/val/
```

**自定义模型：**
```bash
python infer.py \
  --image ./test_image.jpg \
  --model ./output/MobileNetV3_small_x1_0/best_model
```

**显示 Top-K 结果：**
```bash
python infer.py --image ./test_image.jpg --top-k 3
```

---

## 📈 可视化训练过程

```bash
# 启动 VisualDL
visualdl --logdir=./PaddleClas/output --port 8040

# 打开浏览器访问：http://localhost:8040
```

可以看到：
- 📈 准确率曲线
- 📉 损失函数曲线
- ⏱️ 训练速度

---

## 🎯 参数调整指南

### 训练太慢？

```yaml
# 在 flower_config.yaml 中改
Global:
  epochs: 10          # 减少轮数
  
TRAIN:
  batch_size: 32      # 增大批大小
```

### 准确率不高？

```yaml
Global:
  epochs: 50          # 增加轮数
  
Optimizer:
  lr:
    learning_rate: 0.001  # 降低学习率
```

### 没有 GPU？

```yaml
Global:
  device: 'cpu'       # 改为 CPU（会很慢）
```

### 需要更准确的模型？

```yaml
Arch:
  name: ResNet50_vd   # 改为更强的模型
  # 其他选项: EfficientNetB0, ResNet101_vd 等
```

---

## 📚 输出文件说明

训练完成后，会生成：

```
output/MobileNetV3_small_x1_0/
├── best_model/                    # ⭐ 最佳模型（推荐使用）
│   ├── model.pdmodel              # 模型结构
│   ├── model.pdiparams            # 模型权重
│   └── model.pdiparams.info       # 模型信息
│
├── latest/                        # 最新模型（最后一个 epoch）
│   ├── model.pdmodel
│   ├── model.pdiparams
│   └── model.pdiparams.info
│
└── train.log                      # 训练日志
```

---

## ❓ 常见问题

### Q: 找不到 PaddleClas 怎么办？
```bash
git clone https://github.com/PaddlePaddle/PaddleClas.git
cd PaddleClas
pip install -r requirements.txt
cd ..
```

### Q: 数据集如何组织？
目录结构必须是：
```
dataset/
├── train/
│   ├── class1/
│   │   ├── image1.jpg
│   │   └── image2.jpg
│   └── class2/
│       └── image3.jpg
└── val/
    ├── class1/
    │   └── image4.jpg
    └── class2/
        └── image5.jpg
```

### Q: 怎样知道训练好了？
看最后一行输出，准确率 > 90% 就可以了。

### Q: 模型可以转移到别的项目吗？
可以！使用 `./output/MobileNetV3_small_x1_0/best_model` 文件夹即可。

---

## 🔗 更多资源

- 📖 [完整说明](./README.md)
- 📖 [PaddleClas 官方文档](https://github.com/PaddlePaddle/PaddleClas)
- 🎓 [深度学习教程](https://www.paddlepaddle.org.cn/tutorials)

---

**需要帮助？** 查看 README.md 中的常见问题部分。
