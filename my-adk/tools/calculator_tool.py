def calculate(expression: str) -> str:
    """
    간단한 수식을 계산합니다.
    예: "125 * 36", "(3 + 5) / 2"
    """
    try:
        return str(eval(expression))
    except Exception as e:
        return f"계산 오류: {e}"