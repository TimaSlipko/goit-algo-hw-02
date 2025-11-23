def is_symmetrical(text):
    left_symbols = []
    right_symbols = []

    compliance_check = {"(": ")", "{": "}", "[": "]"}
    for k, v in compliance_check.items():
        left_symbols.append(k)
        right_symbols.append(v)

    symbols = left_symbols+right_symbols

    stack = []

    for c in text:
        if c not in symbols:
            continue

        if c in left_symbols:
            stack.append(c)
        else:
            if not len(stack):
                return False
            
            last_symbol = stack.pop()
            if compliance_check[last_symbol] != c:
                return False

    return not len(stack)
        
def main():
    tests = [
        "( ){[ 1 ]( 1 + 3 )( ){ }}",
        "( 23 ( 2 - 3);",
        "( 11 }"
        "",
        "{ } )"
    ]
    
    for test in tests:
        result = is_symmetrical(test)
        print(f"{test} - {result}")

if __name__ == "__main__":
    main()