def fibonacci(n):
    """
    フィボナッチ数列のn番目の値を計算する関数
    
    Args:
        n (int): 計算したい項の位置（1以上の整数）
    
    Returns:
        int: フィボナッチ数列のn番目の値
    """
    if n <= 0:
        raise ValueError("nは1以上の整数を指定してください")
    elif n == 1 or n == 2:
        return 1
    else:
        a, b = 1, 1
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b

def print_fibonacci_sequence(n):
    """
    フィボナッチ数列のn項目までを表示する関数
    
    Args:
        n (int): 表示したい項数（1以上の整数）
    """
    if n <= 0:
        raise ValueError("nは1以上の整数を指定してください")
    
    print(f"フィボナッチ数列の最初の{n}項:")
    for i in range(1, n + 1):
        print(f"{i}番目: {fibonacci(i)}")

if __name__ == "__main__":
    # 使用例: 最初の10項を表示
    try:
        print_fibonacci_sequence(10)
    except ValueError as e:
        print(f"エラー: {e}")
