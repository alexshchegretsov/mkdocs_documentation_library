1. mkdocs new wiki - создание проекта под названием wiki
2. cd  wiki - переход в папку проекта
3. конфигурация yml файла
4. mkdocs serve - запуск сервера
5. mkdocs build - собираем проект для публикации в html


```
site_name: spb_tut django 2 course


nav:
    - Home: index.md
    - Markdown tutorial: tutorial/markdown_tutor/how_to_markdown.md
    - About: about.md
    - Settings project: settings/settings_project.md


theme:
    readthedocs


markdown_extensions:
    - toc:
        permalink: True

dev_addr:
    127.0.0.1:8001


```
