# создать шаблон класса для каждой активности где (action: int, duration: float, weigth: int)
class Training:
    def __init__(self, name):
        self.name = name
        self.m_in_km = 1000
        self.code = ""
        self.steps = 0
        self.w_time = 0
        self.weigth = 0
        self.heigth = 0
        self.pools = 0
        self.pool_len = 0

    def get_data(self, data_list):
        self.code = data_list[0]
        self.steps, self.w_time, self.weigth = map(int, data_list[1])

    # расчёт дистанции, которую пользователь преодолел за тренировку:get_distance();
    # Один шаг — 0.65 метра, один гребок при плавании — 1.38 метра.
    @property
    def get_distance(self):
        if self.code != "SWM":
            return self.steps * 0.65 / self.m_in_km
        else:
            return self.steps * 1.38 / self.m_in_km

    # расчёт средней скорости движения во время тренировки:get_mean_speed();
    @property
    def get_mean_speed(self):
        return self.get_distance / self.w_time

    # расчёт количества потраченных калорий за тренировку:get_spent_calories();
    @property
    def get_calories(self):
        pass

    # создание объекта сообщения о результатах тренировки:show_training_info().
    def get_info(self):
        return f"Тип тренировки: {self.name};\nДлительность: {self.w_time} ч.;" \
               f"\nДистанция: {round(self.get_distance,2)} км;" \
               f"\nСр. скорость: {round(self.get_mean_speed, 2)} км/ч;" \
               f"\nПотрачено ккал: {round(self.get_calories, 2)}\n"

class Running(Training):
    # running (18 * средняя_скорость - 20) * вес_спортсмена / M_IN_KM * время_тренировки_в_минутах
    @property
    def get_calories(self):
        coef_calorie1 = 18
        coef_calorie2 = 20
        return (coef_calorie1 * self.get_mean_speed - coef_calorie2) * \
               self.weigth / self.m_in_km * (self.w_time * 60)

class SportsWalking(Training):
    def get_data(self, data_list):
        self.code = data_list[0]
        self.steps, self.w_time, self.weigth, self.height = map(int, data_list[1])

    # SportsWalking (0.035 * вес + (средняя_скорость**2 // рост) * 0.029 * вес) * время_тренировки_в_минутах
    @property
    def get_calories(self):
        coef_calorie1 = 0.035
        coef_calorie2 = 0.029
        return (coef_calorie1 * self.weigth +
                (self.get_mean_speed**2 // self.height) *
                coef_calorie2 * self.weigth) * (self.w_time * 60)

class Swimming(Training):

    def get_data(self, data_list):
        self.code = data_list[0]
        self.steps, self.w_time, self.weigth, self.pool_len, self.pools = map(int, data_list[1])

    @property
    def get_calories(self):
        av_speed = self.pool_len * self.pools / self.m_in_km / self.w_time
        return (av_speed + 1.1)*2*self.weigth

def read_packages(package):
    for element in package:
        i = 0
        if element[0] == "RUN":
            workouti = Running("Running")
            data_list = element
        elif element[0] == "WLK":
            workouti = SportsWalking("Walking")
            data_list = element
        elif element[0] == "SWM":
            workouti = Swimming("Swimming")
            data_list = element

        workouti.get_data(data_list)
        print(workouti.get_info())
        i += 1


read_packages(package=[
    ("SWM", [720, 1, 80, 25, 40]),
    ("RUN", [15000, 1, 75]),
    ("WLK", [9000, 1, 75, 180])
])
