문제1
Calculator 클래스:
__init__ 메서드: 클래스의 초기화를 담당하며, 연산자와 피연산자를 저장할 스택을 초기화합니다.
__del__ 메서드: 클래스의 소멸자로, 현재는 아무 동작도 하지 않습니다.
is_operator 메서드: 주어진 문자가 연산자인지 여부를 확인하는 메서드입니다.
calculate 메서드: 주어진 연산자와 피연산자를 사용하여 계산을 수행하는 메서드입니다.
evaluate_expression 메서드: 주어진 수식을 평가하여 결과를 반환합니다. 이 때, 괄호 처리와 기본적인 계산을 수행합니다.

문제2
EngineerCalculator 클래스 (상속받음):
__init__ 메서드: 부모 클래스 Calculator의 생성자를 호출하여 초기화를 수행합니다.
calculate_trigonometric 메서드: 삼각함수(sin, cos, tan)를 계산하는 메서드로, math 모듈을 사용합니다.
calculate_factorial 메서드: 팩토리얼을 계산하는 메서드로, 재귀 방식을 사용합니다.
calculate_matrix 메서드: 두 행렬의 곱셈을 계산하는 메서드로, numpy 모듈을 사용합니다.
plot_graph 메서드: 주어진 x, y 값으로 그래프를 작성하는 메서드로, matplotlib을 사용합니다.
예시 사용:
삼각함수 계산: calculate_trigonometric 메서드를 사용하여 sin(45도), cos(45도), tan(45도) 값을 계산합니다.
행렬 곱셈 계산: calculate_matrix 메서드를 사용하여 두 행렬의 곱셈을 계산합니다.
팩토리얼 계산: calculate_factorial 메서드를 사용하여 5의 팩토리얼을 계산합니다.
그래프 작성: plot_graph 메서드를 사용하여 사인 함수의 그래프를 작성하고 출력합니다.
