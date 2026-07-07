#!/bin/bash
# 花卉分类推理脚本（Bash版本）

IMAGE_PATH="${1:-.}"
MODEL="${2:-./output/MobileNetV3_small_x1_0/best_model}"

echo "🖼️  开始图片分类..."
echo "=================================================="
echo "图片路径：$IMAGE_PATH"
echo "模型：$MODEL"

# 检查必要文件
if [ ! -f "./flower_config.yaml" ]; then
    echo "❌ 错误：找不到 flower_config.yaml"
    exit 1
fi

if [ ! -d "./PaddleClas" ]; then
    echo "❌ 错误：找不到 PaddleClas 目录"
    exit 1
fi

if [ ! -e "$IMAGE_PATH" ]; then
    echo "❌ 错误：图片路径不存在：$IMAGE_PATH"
    exit 1
fi

if [ ! -d "$MODEL" ]; then
    echo "❌ 错误：模型不存在：$MODEL"
    exit 1
fi

# 进入 PaddleClas 目录
cd PaddleClas

# 执行推理
python tools/infer.py \
    -c ../flower_config.yaml \
    -o Global.pretrained_model=../$MODEL \
    -o Infer.infer_imgs=../$IMAGE_PATH

echo "=================================================="
echo "✅ 推理完成！"
