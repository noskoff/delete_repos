1. Генерация личного токена доступа (Personal Access Token)
1. Зайдите в свой аккаунт на GitHub.
2. Перейдите в Settings → Developer settings → Personal Access Tokens → Tokens (classic).
3. Нажмите на Generate new token (classic).
4. Включите необходимые разрешения, такие как:
   - repo (доступ ко всем вашему репозиториям).
5. Сохраните токен, он понадобится далее.
6. Скопируйте репозиторий к себе
7. В файле delete_repos.py Замените YOUR_PERSONAL_ACCESS_TOKEN и YOUR_GITHUB_USERNAME в скрипте на свои данные.
8. Запустите скрипт: python delete_repos.py
