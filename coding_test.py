class Calculator:
    """스택을 구현하는 클래스"""
    def __init__(self):
        """스택 초기화"""
        self.items = []

    def push(self, item):
        """스택에 요소 추가"""
        self.items.append(item)

    def pop(self):
        """스택에서 요소 제거"""
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        """스택이 비어 있는지 확인"""
        return len(self.items) == 0

    def peek(self):
        """스택의 맨 위 요소 확인"""
        if not self.is_empty():
            return self.items[-1]

def perform_operation(operator, operand1, operand2):
    """주어진 연산자로 두 피연산자를 계산하는 함수"""
    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    elif operator == '*':
        return operand1 * operand2
    elif operator == '/':
        if operand2 != 0:
            return operand1 / operand2
        else:
            raise ValueError("0으로 나눌 수 없습니다.")

def calculate_expression(expression):
    """
    후위 표기법으로 표현된 수식을 계산하는 함수

    Parameters:
    - expression (str): 후위 표기법으로 표현된 수식

    Returns:
    - 결과값 (float 또는 int): 계산 결과

    Raises:
    - ValueError: 유효하지 않은 수식이거나 0으로 나누기 시도한 경우
    """
    operand_stack = Calculator()
    operator_stack = Calculator()

    operators = set(['+', '-', '*', '/'])
    open_parentheses = set(['(', '[', '{'])
    close_parentheses = set([')', ']', '}'])
    parentheses_pairs = {')': '(', ']': '[', '}': '{'}

    try:
        for token in expression.split():
            if token.isdigit():
                operand_stack.push(int(token))
            elif token in operators:
                operator_stack.push(token)
            elif token in open_parentheses:
                operator_stack.push(token)
            elif token in close_parentheses:
                open_parenthesis = parentheses_pairs[token]
                while operator_stack.peek() != open_parenthesis:
                    operator = operator_stack.pop()
                    operand2 = operand_stack.pop()
                    operand1 = operand_stack.pop()
                    result = perform_operation(operator, operand1, operand2)
                    operand_stack.push(result)
                operator_stack.pop()  # 열린 괄호를 제거
            else:
                raise ValueError("수식에 유효하지 않은 토큰이 있습니다: {}".format(token))

        while not operator_stack.is_empty():
            operator = operator_stack.pop()
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()
            result = perform_operation(operator, operand1, operand2)
            operand_stack.push(result)

        if operand_stack.is_empty() or not operator_stack.is_empty():
            raise ValueError("유효하지 않은 수식입니다.")

        return operand_stack.pop()

    except (ValueError, IndexError, KeyError):
        raise ValueError("유효하지 않은 수식입니다.")


