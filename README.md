# フィボナッチ数列計算プログラム

このプロジェクトは、フィボナッチ数列を計算するPythonプログラムを提供します。

## 機能

- フィボナッチ数列のn番目の値を計算
- 指定した項数までのフィボナッチ数列を表示
- エラーハンドリング機能付き

## 使用方法

1. リポジトリをクローン:
```bash
git clone https://github.com/KosukeHatauchi/test1.git
cd test1
```

2. Pythonファイルを実行:
```bash
python fibonacci.py
```

3. または、自分のコードでインポートして使用:
```python
from fibonacci import fibonacci, print_fibonacci_sequence

# n番目のフィボナッチ数を計算
result = fibonacci(10)
print(f'10番目のフィボナッチ数: {result}')

# 最初のn項を表示
print_fibonacci_sequence(10)
```

## 出力例

```
フィボナッチ数列の最初の10項:
1番目: 1
2番目: 1
3番目: 2
4番目: 3
5番目: 5
6番目: 8
7番目: 13
8番目: 21
9番目: 34
10番目: 55
```

## エラーハンドリング

不適切な入力（0以下の数値）に対しては、適切なエラーメッセージが表示されます：

```python
try:
    fibonacci(0)  # ValueError が発生
except ValueError as e:
    print(f'エラー: {e}')
```

## ライセンス

このプロジェクトはMITライセンスの下で公開されています。