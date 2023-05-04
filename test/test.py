from app.calculator import Calculator

class TestCalculator:
    def setup(self):
        self.calculator = Calculator

    #Создаем тест "Сложение прошло успешно"
    def test_adding_success(self):
        assert self.calculator.adding(self, 1,1) == 2     
        
    # Создаем тест "Вычитание"
    def test_subtract_success(self):
        assert self.calculator.subtract(self,6,3) == 3

    # Создаем тест "Умножение"
    def test_multiply_success(self):
        assert self.calculator.multiply(self, 6, 3) == 18

    #Создаем тест "Деление"
    def test_division_success(self):
        assert self.calculator.division(self, 6, 3) == 2

    #Возведение в степень
    def test_power_success(self):
        assert self.calculator.power(self, 2,3) == 8

    def teardown(self):
        print('Выполнение метода Teardown')
