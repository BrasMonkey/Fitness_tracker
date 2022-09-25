# создать шаблон класса для каждой активности где (action: int, duration: float, weigth: int)
class Training:
    def __init__(self, name):
        self.name = name
        self.m_in_km = 1000

    # расчёт дистанции, которую пользователь преодолел за тренировку:get_distance();
    # Один шаг — 0.65 метра, один гребок при плавании — 1.38 метра.
    @property
    def get_distance(self):
        return self.steps * 0.65 / self.m_in_km

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
        return f"Тип тренировки: {self.code};\nДлительность: {self.w_time} ч.;\nДистанция: {self.get_distance} км;\nСр. скорость: {self.get_mean_speed} км/ч;\nПотрачено ккал: {self.get_calories}."


class Running(Training):
    def get_data(self, data_list):
        self.code = data_list[0]
        self.steps, self.w_time, self.weigth = map(int, data_list[1])

    # running (18 * средняя_скорость - 20) * вес_спортсмена / M_IN_KM * время_тренировки_в_минутах
    @property
    def get_calories(self):
        return (18 * self.get_mean_speed - 20) * self.weigth / self.m_in_km * (self.w_time * 60)

workout = Running("RUN")
data_list=('RUN', [15000, 1, 75])
workout.get_data(data_list)
print(workout.get_info())
# LEN_STEP — расстояние, которое спортсмен преодолевает за один шаг или гребок.

# SportsWalking (0.035 * вес + (средняя_скорость**2 // рост) * 0.029 * вес) * время_тренировки_в_минутах
# Swimming length_pool — длина бассейна в метрах; count_pool — сколько раз пользователь переплыл бассейн.
# av-speed длина_бассейна * count_pool / M_IN_KM / время_тренировки  kkal (средняя_скорость + 1.1) * 2 * вес
# class InfoMessage Свойства класса InfoMessage: training_type— имя класса тренировки;
# duration — длительность тренировки в часах; distance— дистанция в километрах, которую преодолел пользователь за время тренировки;
# speed— средняя скорость, с которой двигался пользователь; calories— количество килокалорий, которое израсходовал пользователь за время тренировки.
# метод get_message(), который возвращает строку сообщения:

