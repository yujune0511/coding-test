class Calculator:
    def __init__(self):
        """
        Calculator 클래스의 생성자입니다.
        연산자와 피연산자를 저장할 스택을 초기화합니다.
        """
        self.operator_stack = []
        self.number_stack = []

    def __del__(self):
        """
        Calculator 클래스의 소멸자입니다.
        현재는 아무 동작도 수행하지 않습니다.
        """
        pass

    def is_operator(self, char):
        """
        주어진 문자가 연산자인지 여부를 확인하는 메서드입니다.

        Parameters:
            char (str): 확인할 문자

        Returns:
            bool: 주어진 문자가 연산자이면 True, 아니면 False
        """
        return char in ['+', '-', '*', '/']

    def calculate(self, operator, operand1, operand2):
        """
        주어진 연산자와 피연산자들을 사용하여 계산을 수행하는 메서드입니다.

        Parameters:
            operator (str): 연산자
            operand1 (int): 피연산자1
            operand2 (int): 피연산자2

        Returns:
            float: 계산 결과
        """
        if operator == '+':
            return operand1 + operand2
        elif operator == '-':
            return operand1 - operand2
        elif operator == '*':
            return operand1 * operand2
        elif operator == '/':
            if operand2 == 0:
                raise ValueError("0으로 나눌 수 없습니다.")
            return operand1 / operand2

    def evaluate_expression(self, expression):
        """
        주어진 수식을 평가하는 메서드입니다.

        Parameters:
            expression (str): 평가할 수식

        Returns:
            float: 수식의 평가 결과

        Raises:
            ValueError: 수식에 오류가 있는 경우 발생
        """
        for char in expression:
            if char.isdigit():
                self.number_stack.append(int(char))
            elif self.is_operator(char):
                self.operator_stack.append(char)
            elif char == '(':
                self.operator_stack.append(char)
            elif char == ')':
                if len(self.operator_stack) == 0 or self.operator_stack[-1] != '(':
                    raise ValueError("괄호의 짝이 맞지 않습니다.")
                while len(self.operator_stack) > 0 and self.operator_stack[-1] != '(':
                    operator = self.operator_stack.pop()
                    operand2 = self.number_stack.pop()
                    operand1 = self.number_stack.pop()
                    result = self.calculate(operator, operand1, operand2)
                    self.number_stack.append(result)
                self.operator_stack.pop()  # '(' 제거

        while len(self.operator_stack) > 0:
            operator = self.operator_stack.pop()
            operand2 = self.number_stack.pop()
            operand1 = self.number_stack.pop()
            result = self.calculate(operator, operand1, operand2)
            self.number_stack.append(result)

        if len(self.number_stack) == 1:
            return self.number_stack[0]
        else:
            raise ValueError("수식이 올바르지 않습니다.")


