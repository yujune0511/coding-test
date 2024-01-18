import math
import numpy as np
import matplotlib.pyplot as plt



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



class EngineerCalculator(Calculator):
    def __init__(self):
        """
        EngineerCalculator 클래스의 생성자입니다.
        Calculator 클래스의 생성자를 호출하여 기본적인 초기화를 수행합니다.
        """
        super().__init__()

    def calculate_trigonometric(self, func, angle):
        """
        삼각함수(sin, cos, tan)를 계산하는 메서드입니다.

        Parameters:
            func (str): 삼각함수 종류 ('sin', 'cos', 'tan')
            angle (float): 각도 (라디안)

        Returns:
            float: 계산 결과
        """
        if func == 'sin':
            return math.sin(angle)
        elif func == 'cos':
            return math.cos(angle)
        elif func == 'tan':
            return math.tan(angle)

    def calculate_factorial(self, n):
        """
        팩토리얼을 계산하는 메서드입니다. (재귀 방식)

        Parameters:
            n (int): 팩토리얼을 계산할 정수

        Returns:
            int: 계산 결과
        """
        if n == 0 or n == 1:
            return 1
        else:
            return n * self.calculate_factorial(n - 1)

    def calculate_matrix(self, matrix1, matrix2):
        """
        행렬 곱셈을 계산하는 메서드입니다.

        Parameters:
            matrix1 (numpy.ndarray): 첫 번째 행렬
            matrix2 (numpy.ndarray): 두 번째 행렬

        Returns:
            numpy.ndarray: 행렬 곱셈 결과
        """
        return np.dot(matrix1, matrix2)

    def plot_graph(self, x_values, y_values, title, xlabel, ylabel):
        """
        주어진 x, y 값으로 그래프를 작성하는 메서드입니다.

        Parameters:
            x_values (list): x 축 값들
            y_values (list): y 축 값들
            title (str): 그래프 제목
            xlabel (str): x 축 레이블
            ylabel (str): y 축 레이블
        """
        plt.plot(x_values, y_values)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.show()

# Example usage:
engineer_calculator = EngineerCalculator()

# 삼각함수 계산
angle_rad = math.radians(45)  # 45도를 라디안으로 변환
print(f"sin(45도): {engineer_calculator.calculate_trigonometric('sin', angle_rad)}")
print(f"cos(45도): {engineer_calculator.calculate_trigonometric('cos', angle_rad)}")
print(f"tan(45도): {engineer_calculator.calculate_trigonometric('tan', angle_rad)}")

# 행렬 곱셈 계산
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])
result_matrix = engineer_calculator.calculate_matrix(matrix1, matrix2)
print(f"행렬 곱셈 결과:\n{result_matrix}")

# 팩토리얼 계산
print(f"5! = {engineer_calculator.calculate_factorial(5)}")

# 그래프 작성
x_values = np.linspace(0, 2 * np.pi, 100)
y_values = np.sin(x_values)
engineer_calculator.plot_graph(x_values, y_values, "Sin Function", "Angle (radians)", "sin(x)")
