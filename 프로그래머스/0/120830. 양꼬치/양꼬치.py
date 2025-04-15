def solution(n, k):
    s = (k - (n // 10)) * 2000
    a = 12000 * n
    b = a + s
    
    return b