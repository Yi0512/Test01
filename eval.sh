#!/bin/bash
# 花卉分类评估脚本（Bash版本）

set -e

MODEL="${1:-./output/MobileNetV3_small_x1_0/best_model}"

echo "📊 开始评估模型..."
echo "=================================================="
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

if [ ! -d "$MODEL" ]; then
    echo "❌ 错误：模型不存在：$MODEL"
    exit 1
fi

# 进入 PaddleClas 目录
cd PaddleClas

# 执行评估
python tools/eval.py -c ../flower_config.yaml -o Global.pretrained_model=../$MODEL

echo "=================================================="
echo "✅ 评估完成！"
