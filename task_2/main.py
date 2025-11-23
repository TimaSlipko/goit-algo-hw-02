from collections import deque

def is_palindrome(text):
    normalized = ''.join(text.lower().split())
    
    if len(normalized) <= 1:
        return True
    
    dq = deque(normalized)
    
    while len(dq) > 1:
        left = dq.popleft()
        right = dq.pop()
        
        if left != right:
            return False
    
    return True


def main():
    tests = [
        "A man a plan a canal Panama",
        "race car",
        "Was it a car or a cat I saw",
        "hello",
        "12321",
        "12345",
        "Козак з казок",
        "Дід і дід",
        ""
    ]
    
    for test in tests:
        result = is_palindrome(test)
        print(f"{test} - {result}")

if __name__ == "__main__":
    main()