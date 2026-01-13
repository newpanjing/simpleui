#!/usr/bin/env zsh
echo 'delete cache'
find . -type d -name "__pycache__" -exec rm -rf {} +
echo 'release django-simpleui...'
rm -rf dist/*
python3 setup.py sdist

cd dist
# 循环处理匹配的文件
# 匹配规则: django-simpleui 开头 且 .tar.gz 结尾
for old_file in django-simpleui-*.tar.gz; do
    
    # 防止没有匹配文件时 old_file 变成字符串本身
    [ -e "$old_file" ] || continue
    
    # 构造新文件名：将第一个 "django-simpleui" 替换为 "django_simpleui"
    # 注意：只替换前面的包名，版本号后的 .tar.gz 保持不变
    new_file=$(echo "$old_file" | sed 's/django-simpleui/django_simpleui/')
    
    if [ "$old_file" != "$new_file" ]; then
        echo "🔄 正在重命名: $old_file -> $new_file"
        mv "$old_file" "$new_file"
    fi
done

cd ..

echo "✅ rename done."

twine upload dist/*

echo 'release django-simpleui success.'

echo 'release simpleui...'
rm -rf dist/*
python3 setup2.py sdist
twine upload dist/*

echo 'release simpleui success.'