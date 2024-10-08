import instaloader


def insta_connect(username, password):
    """Коннектимся к инстаграмму.

    Args:
        username (str): Логин.
        password (str): Пароль.

    Returns:
        InstaLoader: Объект соединения.
    """
    Loader = instaloader.Instaloader()
    try:
        Loader.login(user=username, passwd=password)
    except instaloader.exceptions.TwoFactorAuthRequiredException:
        verification_code = input('Введите код подтверждения: ')
        Loader.two_factor_login(verification_code)
    return Loader
