import time


class UrTube:

    def __init__(self):
        self.users = {}
        self.videos = {}
        self.current_user = None

    def log_in(self, nickname, password):
        self.nickname = str(nickname)
        self.password = hash(password)
        if self.nickname in self.users.keys() and self.password == self.users[self.nickname]['password']:
            self.current_user = self.nickname
        else:
            print('Такой пользователь не зарегистрирован')

    def register(self, nickname, password, age):
        self.nickname = str(nickname)
        self.password = hash(password)
        self.age = int(age)
        if self.nickname not in self.users.keys():
            self.users[str(nickname)] = {'password': hash(password), 'age': int(age)}
            ur.log_in(nickname, password)
        else:
            print(f'Пользователь {nickname} уже существует')

    def log_out(self):
        self.current_user = None

    def add(self, *video):
        self.video = video
        for i in self.video:
            self.videos[i.title] = {'duration': i.duration, 'time_now': i.time_now, 'adult_mode': i.adult_mode}

    def get_videos(self, search):
        self.search = str(search)
        list_video = []
        for i in self.videos.keys():
            if self.search.lower() in str(i).lower():
                list_video.append(i)
        return list_video

    def watch_video(self, movie_title):
        self.movie_title = str(movie_title)
        for i in self.videos.keys():
            if self.movie_title != str(i):
                continue
            if self.movie_title == str(i):
                if self.current_user is None:
                    print('Войдите в аккаунт, чтобы смотреть видео')
                elif self.current_user == self.nickname and self.users[self.nickname]['age'] < 18:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                else:
                    for j in range(self.videos.get(i)['time_now'], self.videos.get(i)['duration'] + 1):
                        time.sleep(1)
                        Video.time_now = j
                        print(j, '', end='')
                    time.sleep(1)
                    Video.time_now = 0
                    print('Конец видео')
                    time.sleep(1)


class Video:
    """
    Класс видео, содержащий атрибуты: заголвок, продолжительность, секунда остановки, продолжительность
    """
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.time_now = time_now
        self.title = str(title)
        self.duration = duration
        self.adult_mode = bool(adult_mode)


class User:
    """
    Класс пользователя, содержащий атрибуты: логин, пароль, возраст
    """
    def __init__(self, nickname, password, age):
        self.nickname = str(nickname)
        self.password = hash(password)
        self.age = int(age)


if __name__ == '__main__':
    ur = UrTube()
    user = User(input('Введите логин: '), input('Введите пароль: '), input('Введите возраст: '))
    ur.register(user.nickname, user.password, user.age)


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
