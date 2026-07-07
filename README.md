# 🌹 花卉图像分类项目（PaddleClas）

基于 PaddleClas 的花卉图像分类深度学习项目，**小白友好**，开箱即用！

## 📋 项目简介

本项目使用 **PaddleClas 框架**实现花卉图像三分类：
- 🌹 **玫瑰（Rose）**
- 🌻 **向日葵（Sunflower）**
- 🌷 **郁金香（Tulip）**

适合以下人群学习：
- 🎓 初学者入门深度学习
- 🔬 学生完成课设
- 👨‍💼 工程师快速原型验证

## 🚀 快速开始（5分钟）

### 1️⃣ 环境准备

```bash
# 克隆项目
git clone https://github.com/Yi0512/Test01.git
cd Test01

# 创建虚拟环境（可选但推荐）
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
venv\Scripts\activate  # Windows

# 安装 PaddlePaddle（GPU版本，推荐）
python -m pip install paddlepaddle-gpu -i https://mirror.baidu.com/pypi/simple

# 或 CPU版本（无需GPU）
python -m pip install paddlepaddle -i https://mirror.baidu.com/pypi/simple

# 克隆 PaddleClas 框架
git clone https://github.com/PaddlePaddle/PaddleClas.git

# 安装依赖
cd PaddleClas
pip install -r requirements.txt
cd ..
```

### 2️⃣ 准备数据

创建数据集目录结构：

```bash
mkdir -p dataset/train/{rose,sunflower,tulip}
mkdir -p dataset/val/{rose,sunflower,tulip}
```

**下载免费图片资源：**
- [Unsplash](https://unsplash.com) - 搜索 "rose flower"
- [Pexels](https://www.pexels.com) - 搜索 "sunflower"
- [Pixabay](https://pixabay.com) - 搜索 "tulip"

**最小数据集要求：**
- 训练集：每类 20-50 张
- 验证集：每类 5-10 张

### 3️⃣ 开始训练

```bash
cd PaddleClas

# 执行训练
python tools/train.py -c ../flower_config.yaml

# 或指定GPU设备
CUDA_VISIBLE_DEVICES=0 python tools/train.py -c ../flower_config.yaml
```

训练过程会输出：
```
[2024-01-15 10:30:45] epoch: 1/20, step: 1/50, loss: 1.234, acc: 0.40
[2024-01-15 10:31:05] epoch: 1/20, step: 10/50, loss: 0.890, acc: 0.68
...
[2024-01-15 10:35:00] epoch: 2/20, best_acc: 0.75, save best model
```

### 4️⃣ 实时监控（可选）

**新开一个终端**运行：

```bash
visualdl --logdir=./PaddleClas/output --port 8040
```

访问：`http://localhost:8040` 查看训练曲线

### 5️⃣ 评估模型

```bash
cd PaddleClas

python tools/eval.py \
  -c ../flower_config.yaml \
  -o Global.pretrained_model=../output/MobileNetV3_small_x1_0/best_model
```

### 6️⃣ 预测使用

**预测单张图片：**

```bash
cd PaddleClas

python tools/infer.py \
  -c ../flower_config.yaml \
  -o Global.pretrained_model=../output/MobileNetV3_small_x1_0/best_model \
  -o Infer.infer_imgs=../dataset/val/rose/sample.jpg
```

输出示例：
```
class_id:0, probability:0.95, class_name:rose
```

**批量预测：**

```bash
python tools/infer.py \
  -c ../flower_config.yaml \
  -o Global.pretrained_model=../output/MobileNetV3_small_x1_0/best_model \
  -o Infer.infer_imgs=../dataset/val/
```

## 📁 项目结构

```
Test01/
├── README.md                          # 本文件
├── flower_config.yaml                 # 训练配置文件
├── train.sh                           # 训练脚本（可选）
├── dataset/                           # 数据集目录
│   ├── train/
│   │   ├── rose/                      # 玫瑰训练集
│   │   ├── sunflower/                 # 向日葵训练集
│   │   └── tulip/                     # 郁金香训练集
│   └── val/
│       ├── rose/                      # 玫瑰验证集
│       ├── sunflower/                 # 向日葵验证集
│       └── tulip/                     # 郁金香验证集
├── PaddleClas/                        # PaddleClas 框架（git clone下载）
└── output/                            # 训练输出（自动生成）
    └── MobileNetV3_small_x1_0/
        ├── best_model/                # ⭐ 最佳模型
        └── latest/
```

## 🔧 配置文件说明

修改 `flower_config.yaml` 中的参数：

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `epochs` | 训练轮数 | 20 |
| `batch_size` | 批大小 | 16 |
| `learning_rate` | 学习率 | 0.01 |
| `device` | 计算设备 | gpu |
| `warmup_epochs` | 预热轮数 | 2 |
| `CLASS_NUM` | 分类数 | 3 |

## 🎯 快速调整

**加快训练（如果太慢）：**
```bash
python tools/train.py \
  -c ../flower_config.yaml \
  -o Global.epochs=10 \
  -o TRAIN.batch_size=32
```

**提高精度（如果效果不好）：**
```bash
python tools/train.py \
  -c ../flower_config.yaml \
  -o Global.epochs=50 \
  -o Optimizer.lr.learning_rate=0.001
```

**使用更强的模型（更慢但更准）：**
编辑 `flower_config.yaml`，改：
```yaml
Arch:
  name: ResNet50_vd  # 比 MobileNetV3 更强
```

## ❓ 常见问题

### Q: 我没有 GPU 怎么办？
**A:** 修改配置文件：
```yaml
Global:
  device: 'cpu'
```
训练会慢 10-50 倍，但可以正常工作。

### Q: 怎样知道训练效果好不好？
**A:** 看验证集准确率（acc）：
- \> 90%：不错 ✅
- \> 95%：很优秀 🎉
- \< 70%：可能数据太少或参数需调整

### Q: 数据太少会怎样？
**A:** 会过拟合。解决方法：
1. 收集更多数据
2. 减小 epoch 数
3. 降低学习率
4. 用更轻量的模型（MobileNetV3）

### Q: 如何加快训练速度？
**A:** 
1. 使用 GPU（10-50 倍快）
2. 增大 batch_size（但会降低精度）
3. 用轻量级模型（MobileNetV3）

### Q: 训练过程中出错怎么办？
**A:** 检查以下几点：
1. 数据路径是否正确？
2. 数据格式是否为 jpg/png？
3. 是否安装了所有依赖？
4. GPU 内存是否充足？

## 📚 下一步学习

完成基础训练后，可以尝试：

- ✅ **增加数据量** → 每类 100+ 张图片，提高准确率
- ✅ **调参优化** → 改学习率、batch_size、优化器等
- ✅ **更换模型** → ResNet50、EfficientNet 等
- ✅ **数据增强** → 启用 mixup、cutmix 等
- ✅ **模型部署** → 转为 ONNX、TensorRT、移动端格式
- ✅ **迁移学习** → 用 ImageNet 预训练模型，加速收敛

## 🔗 相关资源

- 📖 [PaddleClas 官方文档](https://github.com/PaddlePaddle/PaddleClas)
- 📖 [PaddlePaddle 官网](https://www.paddlepaddle.org.cn/)
- 📖 [花卉数据集](https://www.kaggle.com/datasets/alxmamaev/flowers-recognition)

## 💡 提示

- 👉 建议先用 CPU 测试流程是否正常，再用 GPU 大规模训练
- 👉 保存好训练日志，方便后续分析
- 👉 定期查看 VisualDL 可视化，及时调整参数

## 📝 许可证

MIT License

## 🤝 贡献

欢迎 PR 和 Issue！

---

**有问题？**
1. 检查 [PaddleClas 官方 Issue](https://github.com/PaddlePaddle/PaddleClas/issues)
2. 查看训练日志 `output/train.log`
3. 在本仓库提交 Issue

**祝你学习愉快！** 🎉
