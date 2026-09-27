import numpy as np

def chebyshev_nodes_sorted(a: float, b: float, n: int) -> np.ndarray:
    """
    Sinh n mốc Chebyshev loại 1 trên đoạn [a, b] theo thứ tự tăng dần.
    Độ phức tạp: O(n) thời gian, O(n) bộ nhớ.
    Đảm bảo tính đối xứng số học tuyệt đối.
    """
    if a >= b:
        raise ValueError("Yêu cầu a < b.")
    if n <= 0:
        raise ValueError("Số mốc n phải là số nguyên dương.")

    m = 0.5 * (a + b)
    print(m)
    r = 0.5 * (b - a)
    print(r)

    # Khởi tạo mảng kết quả
    x = np.empty(n, dtype=np.float64)
    half = n // 2
    print(half)
    # Tính nửa đầu các góc theta: k = 0, 1, ..., half - 1
    k = np.arange(half, dtype=np.float64)
    theta = (2.0 * k + 1.0) * np.pi / (2.0 * n)
    c = np.cos(theta)

    # Gán đối xứng
    x[:half] = m - r * c
    x[n - half:][::-1] = m + r * c

    # Nếu n lẻ, gán mốc chính giữa bằng chính xác trung điểm
    if n % 2 == 1:
        x[half] = m

    return x
print(chebyshev_nodes_sorted(-1, 1, 9))
print(chebyshev_nodes_sorted(3, 6, 12)) 