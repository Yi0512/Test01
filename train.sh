#!/bin/bash
# 花卉分类训练脚本（Bash版本）

set -e

echo "🚀 开始花卉分类训练..."
echo "=================================================="

# 检查必要文件
if [ ! -f "./flower_config.yaml" ]; then
    echo "❌ 错误：找不到 flower_config.yaml"
    exit 1
fi

if [ ! -d "./PaddleClas" ]; then
    echo "❌ 错误：找不到 PaddleClas 目录"
    echo "请先克隆：git clone https://github.com/PaddlePaddle/PaddleClas.git"
    exit 1
fi

# 检查数据集
if [ ! -d "./dataset/train" ]; then
    echo "⚠️  警告：找不到训练数据集"
    echo "请创建目录结构并放入图片"
    exit 1
fi

# 进入 PaddleClas 目录
cd PaddleClas

# 执行训练
echo "📋 配置文件：flower_config.yaml"
echo "=================================================="

python tools/train.py -c ../flower_config.yaml

echo "=================================================="
echo "✅ 训练完成！"
echo "模型已保存到：output/MobileNetV3_small_x1_0/"
