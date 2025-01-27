# (1) Асинхронный SQLAlchemy 2: простой пошаговый гайд по настройке, моделям, связям и миграциям с использованием Alembic

![rw-book-cover](https://habrastorage.org/getpro/habr/upload_files/354/914/58d/35491458d86edb2f225e584e6a7f53df.jpg)

## Metadata
- Author: [[Хабр]]
- Full Title: (1) Асинхронный SQLAlchemy 2: простой пошаговый гайд по настройке, моделям, связям и миграциям с использованием Alembic
- Category: #articles
- Document Tags: [[alembic]] [[outline]] [[Outline]] [[sqlalchemy]] 
- Summary: Эта статья предлагает пошаговое руководство по настройке асинхронного SQLAlchemy и использованию Alembic для управления миграциями базы данных. Модели описывают таблицы и связи, что упрощает работу с данными и позволяет эффективно управлять изменениями. В статье также рассматриваются основные принципы работы с различными типами данных и связями между таблицами.
- URL: https://habr.com/ru/companies/amvera/articles/849836/

## Highlights
- # Связь один-ко-многим с Comment comments: Mapped[list["Comment"]] = relationship( "Comment", back_populates="post", cascade="all, delete-orphan" ) ([View Highlight](https://read.readwise.io/read/01jekejacz24t76s1v61fasvnx))

- post_id: Mapped[int] = mapped_column(ForeignKey('posts.id')) ([View Highlight](https://read.readwise.io/read/01jekevgwy8weer9p329pqyyrq))

- AsyncAttrs: Позволяет создавать асинхронные модели, что улучшает производительность при работе с асинхронными операциями. ([View Highlight](https://read.readwise.io/read/01je8bhs9hp0c6rn0n41njx1gp))

- Enum из модуля enum в Python используется для создания перечислений, которые представляют собой набор именованных значений. Это позволяет определять типы данных с ограниченным набором возможных значений. ([View Highlight](https://read.readwise.io/read/01je8c87mkn28a59r0bv94b09t))

- В SQLAlchemy технология `relationship` позволяет настраивать и управлять связями между таблицами. В случае связи один-к-одному между таблицами `User` и `Profile` настройка выглядит следующим образом: ([View Highlight](https://read.readwise.io/read/01je8cekwdje5tzvgwdx8rma1s))

- `cascade="all, delete-orphan"`: Эта настройка в модели `User` указывает, что все посты, связанные с пользователем, должны быть удалены, если удаляется сам пользователь. ([View Highlight](https://read.readwise.io/read/01je8cj4dpt20h7n6dzqhxxpfr))

- Для начала работы с Alembic, нам нужно выполнить его инициализацию с поддержкой асинхронного взаимодействия с базой данных. Это можно сделать с помощью следующей команды: ([View Highlight](https://read.readwise.io/read/01je8cm8pyd47eh7x1yr84jv6w))
    - Note: Добавить ссылку сюда в заметку про alembic

- Когда вы используете Alembic для управления миграциями, нужно учитывать несколько важных особенностей, связанных с типами данных ENUM в PostgreSQL. Давайте разберемся с двумя основными проблемами и способами их решения. ([View Highlight](https://read.readwise.io/read/01je8cs6xzgvvp6vne8wfecpxy))

- **Совет:** Всегда указывайте `create_type=False` для колонок с ENUM, чтобы избежать конфликтов при повторных миграциях. ([View Highlight](https://read.readwise.io/read/01je8ct2racd71nvedwtfrstrb))

- Если вам нужно обновить базу данных не до самой последней версии, а до конкретной миграции, можно указать идентификатор (ID) нужной миграции. Например: ([View Highlight](https://read.readwise.io/read/01je8cw0a1bangdx93banja582))

- Откат на одну версию назад
  Чтобы откатить миграцию на одну версию назад, используйте следующую команду: ([View Highlight](https://read.readwise.io/read/01je8cy00wqvfwrszaw3b4w5wb))



## New highlights added January 21, 2025 at 10:44 AM
- profile: Mapped["Profile"] = relationship( "Profile", back_populates="user", uselist=False, # Ключевой параметр для связи один-к-одному lazy="joined" # Автоматически подгружает profile при запросе user ) ([View Highlight](https://read.readwise.io/read/01jj3segdvwsm1vh8ascex89sx))

- user: Mapped["User"] = relationship( "User", back_populates="profile", uselist=False ) ([View Highlight](https://read.readwise.io/read/01jj3scjk3nx4xja2e9f7t9xzz))



----
📂 [[Articles]] | Последнее изменение: 21.01.2025 10:44