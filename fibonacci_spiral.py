import matplotlib.pyplot as plt
import numpy as np
from fibonacci import fibonacci

def draw_fibonacci_spiral(n):
    """
    フィボナッチスパイラルを描画する関数
    
    Args:
        n (int): フィボナッチ数列の項数（4以上を推奨）
    """
    if n < 2:
        raise ValueError("nは2以上の整数を指定してください")
    
    # フィボナッチ数列を生成
    fib_numbers = [fibonacci(i) for i in range(1, n + 1)]
    
    # プロットの設定
    plt.figure(figsize=(10, 10))
    ax = plt.gca()
    ax.set_aspect('equal')
    
    # 現在の位置と角度を追跡
    current_x = 0
    current_y = 0
    angle = 0
    
    # 各四分円を描画
    for i in range(len(fib_numbers)):
        # 現在のフィボナッチ数を半径として使用
        radius = fib_numbers[i]
        
        # 90度（π/2ラジアン）の弧を描く点を生成
        theta = np.linspace(angle, angle + np.pi/2, 100)
        x = current_x + radius * np.cos(theta)
        y = current_y + radius * np.sin(theta)
        
        # 弧を描画
        plt.plot(x, y, 'b-')
        
        # 次の四分円の開始点を計算
        angle += np.pi/2
        if i % 4 == 0:
            current_x += fib_numbers[i]
        elif i % 4 == 1:
            current_y += fib_numbers[i]
        elif i % 4 == 2:
            current_x -= fib_numbers[i]
        else:
            current_y -= fib_numbers[i]
    
    # グラフの設定
    plt.title('フィボナッチスパイラル')
    plt.grid(True)
    plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)
    plt.axvline(x=0, color='k', linestyle='-', alpha=0.3)
    
    # グラフを表示
    plt.show()

def draw_fibonacci_squares(n):
    """
    フィボナッチ数列に基づく正方形を描画する関数
    
    Args:
        n (int): フィボナッチ数列の項数（4以上を推奨）
    """
    if n < 2:
        raise ValueError("nは2以上の整数を指定してください")
    
    # フィボナッチ数列を生成
    fib_numbers = [fibonacci(i) for i in range(1, n + 1)]
    
    # プロットの設定
    plt.figure(figsize=(10, 10))
    ax = plt.gca()
    ax.set_aspect('equal')
    
    # 現在の位置を追跡
    current_x = 0
    current_y = 0
    
    # 各正方形を描画
    for i in range(len(fib_numbers)):
        size = fib_numbers[i]
        
        if i % 4 == 0:
            # 右に配置
            square = plt.Rectangle((current_x, current_y), size, size,
                                 fill=False, color='blue')
            current_x += size
        elif i % 4 == 1:
            # 上に配置
            square = plt.Rectangle((current_x - size, current_y), size, size,
                                 fill=False, color='blue')
            current_y += size
        elif i % 4 == 2:
            # 左に配置
            square = plt.Rectangle((current_x - size, current_y - size), size, size,
                                 fill=False, color='blue')
            current_x -= size
        else:
            # 下に配置
            square = plt.Rectangle((current_x, current_y - size), size, size,
                                 fill=False, color='blue')
            current_y -= size
        
        ax.add_patch(square)
        # 正方形の中心にフィボナッチ数を表示
        plt.text(current_x - size/2, current_y - size/2, str(size),
                 ha='center', va='center')
    
    # グラフの設定
    plt.title('フィボナッチ正方形')
    plt.grid(True)
    plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)
    plt.axvline(x=0, color='k', linestyle='-', alpha=0.3)
    
    # グラフを表示
    plt.show()

if __name__ == "__main__":
    try:
        # フィボナッチスパイラルと正方形を描画（例：最初の10項）
        n = 10
        draw_fibonacci_spiral(n)
        draw_fibonacci_squares(n)
    except ValueError as e:
        print(f"エラー: {e}")
