import instaloader


def get_users_info(Loader, target, followers_count):
    """Получаем данные по пользователям.

    Args:
        Loader (InstaLoader): Объект коннекта к инстаграмму.
        target (str): Аккаунт с которого тащим информацию.
        followers_count (int): Сколько подписчиков тянем.

    Returns:
        list: Список пользователей.
    """
    result = []
    user_data = {}
    profile = instaloader.Profile.from_username(Loader.context, target)
    followers = profile.get_followers()
    for i, follower in enumerate(followers):
        user_data = {
            'username': follower.username,
            'followees': follower.followees,
            'followers': follower.followers,
            'mediacount': follower.mediacount,
            'biography': follower.biography,
            'full_name': follower.full_name,
        }
        result.append(user_data)
        if i == followers_count - 1:
            return result
