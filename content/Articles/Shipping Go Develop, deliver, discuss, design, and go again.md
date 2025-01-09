# Shipping Go: Develop, deliver, discuss, design, and go again

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/media/reader/parsed_document_assets/235355838/Tu5F2oczG3H7sE7TkVH6zmlSM2ZPNGapfg7MDqUv_T0-cove_4XoSs9f.png)

## Metadata
- Author: [[Joel Holmes]]
- Full Title: Shipping Go: Develop, deliver, discuss, design, and go again
- Category: #articles
- Document Tags: [[devops]] [[go]] 
- Summary: The text discusses a flexible approach to product development that emphasizes documentation, testing, and automation to ensure quality and efficiency. It encourages teams to configure applications dynamically rather than creating separate test products, which can hinder productivity. The overall goal is to streamline the development process and make it easier for teams to collaborate and maintain code quality.
- URL: https://readwise.io/reader/document_raw_content/235355838

## Highlights
- // Arrange rr := httptest.NewRecorder() req, _ := http.NewRequest("GET", "/hello", nil) handler := http.HandlerFunc(rest.TranslateHandler) // Act handler.ServeHTTP(rr, req) // Assert if rr.Code != http.StatusOK { ❼ t.Errorf(`expected status 200 but received %d`, rr.Code) } ([View Highlight](https://read.readwise.io/read/01jcnbmb742v1sjnavh1xkx60n))
    - Note: Интересный и практичный пример тестирования хэндлера эндпоинта.
- test: name: Test Application runs-on: ubuntu-latest steps: - name: Set up Go 1.x uses: actions/setup-go@v2 ([View Highlight](https://read.readwise.io/read/01jcnbvx37rbkczsntezqh38sb))
    - Note: Пример запуска тестов в GitHub Action.
## New highlights added December 19, 2024 at 2:22 PM
- As a developer, you can have insight into how your code works; as an operations member, you have insight into how it should run. There will be operations members who have a better understanding of how a project should be deployed, and they can guide you through the solution or provide examples or modules for you to use. There will be developers who will be able to help enhance and build deployments and pipelines to make their products run efficiently. ([View Highlight](https://read.readwise.io/read/01jf9wdgrvmnxk46rydkvatdqr))

- Code reviews seem to be a slow and cumbersome process when you are just trying to get work done. But I can assure you that they are not. They provide an excellent way of teaching others and informing your team about what you are changing. Even while working alone on a project, I find myself creating pull requests for myself. This helps me review what has changed and can help me identify bugs and problems. This is like reviewing a paper you’ve written and finding mistakes and glaring problems that you missed in the initial draft. ([View Highlight](https://read.readwise.io/read/01jfa5ajy9yzxq1kxmvym1xbxz))
    - Tags: [[outline]] 

- Limit reviews to 300 lines of code (including test code). ([View Highlight](https://read.readwise.io/read/01jfa5e6597k77bbmr19hsyk3g))

- The author Stephen King says that the first step to becoming a good writer is to become an active reader. I believe that the same holds for developers. To become a better developer, you need to read more code. As a team, this allows more senior developers to show younger developers different techniques and ways to write code and solve problems. For younger developers, it becomes a way to show senior developers new techniques and solutions to problems. ([View Highlight](https://read.readwise.io/read/01jfa5h0cr242rxg7s4x8xm997))

- t others as you want to be treated. 2. Check your ego at the door.
  3. Don’t waste others’ time with bad code.
  4. Learn from feedback, and try not to repeat mistakes.
  5. Take discussions offline instead of going back and forth in comments.
  6. Keep an open mind as to what others are doing.
  7. Make sure it works. ([View Highlight](https://read.readwise.io/read/01jfa5k5d0kenvzhp2nk054vga))

- Reviews should be a priority because they are considered work in progress (WIP). ([View Highlight](https://read.readwise.io/read/01jfa6cbmrv57afr4z547n3z30))

- c/e ([View Highlight](https://read.readwise.io/read/01jfa7ax4ga2vy62kr2a42yzjy))

- We will set our pipeline to enforce checks before the merge button is allowed to be pushed. ([View Highlight](https://read.readwise.io/read/01jfa7m2j0c5hbn60cd3dq6jm8))
    - Note: Настройка Action для проверки форматирования в PR.

- We should add this to our pipeline so that we can do the checks. ([View Highlight](https://read.readwise.io/read/01jfa7vxjqtxymxbrgehcffcxp))
    - Note: Настройка Action для запуска go vet.

- Create a file called scripts/hooks/pre-commit, and add the code in the following listing. ([View Highlight](https://read.readwise.io/read/01jfaac325azsmt3tzh7b3adyx))
    - Note: Настройка git pre-commit hook.

- The first reason is to underline the importance of creating interfaces early in development instead of doing it later. ([View Highlight](https://read.readwise.io/read/01jfc8w0d3j9bax6tvn61h7mab))

- Now we need to pass values to these variables through our build command. The information we are passing is the most recent tag information, the hash, and the build date. ([View Highlight](https://read.readwise.io/read/01jfce78vas7aw5ncacf11qke0))
    - Note: Вставляем версию, хэш, дату сборки при компиляции.

- . We can automate this process by using a tool that will look at the commit messages we make and add them to the body of the release. ([View Highlight](https://read.readwise.io/read/01jfcedy7sy05xjve7vjt1bgw4))
    - Note: Автоматизация создания changelog.


## New highlights added December 27, 2024 at 11:36 PM
- Situations like flaky tests, long build times, frequent build failures, and dependency timeouts can be the result of poorly written tests, a slow build server, a bad development environment, and the need for artifact caching. But you will not know that these problems are there or how they should be prioritized if you aren’t gathering metrics and talking to your team. ([View Highlight](https://read.readwise.io/read/01jfm9j6cx17czm60b96jyp9zz))




----
📂 [[Articles]] | Последнее изменение: 27.12.2024 23:36