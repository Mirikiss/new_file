


class Worker(Persen):

    def __init__(self, id_namber, ferst_name, last_name, age, second_name):
        super().__init__(ferst_name, last_name, second_name)
        self.id_namber = id_namber
        self_lvl = list(map(int, id_namber))%7

