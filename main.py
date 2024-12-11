import os
import re
import requests

# Регулярное выражение для поиска гиперссылок вида <a href="...">...</a>
pattern = r'<a\s+href=["\'](.+?)["\'].*?>.*?</a>'

def find_links(html):
    """Функция для поиска всех гиперссылок в HTML-коде."""
    matches = re.findall(pattern, html, re.DOTALL)
    return matches

def main():
    """Основная функция программы."""
    while True:
        choice = input('Выберите источник данных:\n'
                       '1. Ввести HTML-код вручную\n'
                       '2. Загрузить файл\n'
                       '3. Указать URL\n'
                       '4. Выход\n'
                       'Ваш выбор: ')
        
        if choice == '1':
            html = input('Введите HTML-код: ')
            links = find_links(html)
            if links:
                print('Найденные ссылки:')
                for link in links:
                    print(link)
            else:
                print('Ссылки не найдены.')

        elif choice == '2':
            file_name = input('Укажите имя файла (в текущей папке): ')
            file_path = os.path.join(os.getcwd(), file_name)
            try:
                with open(file_path, encoding='utf-8') as f:
                    html = f.read()
                    links = find_links(html)
                    if links:
                        print('Найденные ссылки:')
                        for link in links:
                            print(link)
                    else:
                        print('Ссылки не найдены.')
            except FileNotFoundError:
                print('Файл не найден. Попробуйте снова.')

        elif choice == '3':
            url = input('Введите URL: ')
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    html = response.text
                    links = find_links(html)
                    if links:
                        print('Найденные ссылки:')
                        for link in links:
                            print(link)
                    else:
                        print('Ссылки не найдены.')
                else:
                    print(f'Ошибка при запросе страницы: статус-код {response.status_code}.')
            except requests.exceptions.RequestException as e:
                print(f'Ошибка при запросе страницы: {e}.')

        elif choice == '4':
            break

        else:
            print('Неверный выбор. Попробуйте еще раз.')

if __name__ == '__main__':
    main()