class Results:
    def __init__(self, victories, draws, losses):
        self.victories = victories
        self.draws = draws
        self.losses = losses

class Football(Results):
    def __init__(self, victories, draws, losses):
        super().__init__(victories, draws, losses)

    def number_of_wins(self, victories):
        return f"Футбольных побед: {victories}"

    def number_of_draws(self, draws):
        return f"Футбольных ничьих: {draws}"

    def number_of_losses(self, losses):
        return f"Футбольных поражений: {losses}"

    def total_points(self):
        total_points = 3 * self.victories + self.draws
        return f"Общее количество очков: {total_points}"
        
class Hockey(Results):
    def __init__(self, victories, draws, losses):
        super().__init__(victories, draws, losses)

    def number_of_wins(self, victories):
        return f"Хоккейных побед: {victories}"

    def number_of_draws(self, draws):
        return f"Хоккейных ничьих: {draws}"

    def number_of_losses(self, losses):
        return f"Хоккейных поражений: {losses}"

    def total_points(self):
        total_points = 2 * self.victories + self.draws
        return f"Общее количество очков: {total_points}"

football_team = Football(2, 2, 2)
hockey_team = Hockey(2, 2, 2)

for team in (football_team, hockey_team):
    print(team.number_of_wins(2))
    print(team.number_of_draws(2))
    print(team.number_of_losses(2))
    print(team.total_points())