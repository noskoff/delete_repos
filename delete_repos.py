import requests

# Замените TOKEN на ваш персональный токен доступа
GITHUB_TOKEN = "YOUR_PERSONAL_ACCESS_TOKEN"
USERNAME = "YOUR_GITHUB_USERNAME"

# Базовый URL API
BASE_URL = "https://api.github.com"

# Заголовки для аутентификации
HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

# Получение списка всех репозиториев
def get_repositories():
    repos = []
    url = f"{BASE_URL}/user/repos"
    while url:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()

        repos.extend(response.json())

        # Пагинация: если есть ссылка на следующую страницу, будем продолжать
        url = response.links.get("next", {}).get("url")
    
    return repos

# Удаление репозиториев
def delete_repository(repo_owner, repo_name):
    url = f"{BASE_URL}/repos/{repo_owner}/{repo_name}"
    response = requests.delete(url, headers=HEADERS)
    if response.status_code == 204:
        print(f"Репозиторий {repo_name} удалён.")
    else:
        print(f"Не удалось удалить {repo_name}: {response.status_code} {response.json()}")

def main():
    print("Получение списка репозиториев...")
    repositories = get_repositories()

    if not repositories:
        print("У вас нет репозиториев для удаления.")
        return

    print(f"Найдено {len(repositories)} репозиториев.")

    for repo in repositories:
        repo_name = repo['name']
        delete_repository(USERNAME, repo_name)

if __name__ == "__main__":
    main()
