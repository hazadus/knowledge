Добавить SSH-ключ [https://www.youtube.com/watch?v=QF4ZF857m44&t=1706s](https://www.youtube.com/watch?v=QF4ZF857m44&t=1706s)
`cat /Users/hazadus/.ssh/timeweb/timeweb.pub | pbcopy` (копирует вывод в буфер обмена)
```Python
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCldpOoimHbMVOc0OP5MIyRc+NGqVj5g6q/Fg2ERbz6vgXmkDyQBFdCPVX1g13weUS/PaUdwxvbWnydtBUYTIBFK+aKM54RgqPW/oTzS1eef6hGjNd7LTezUVf1gNNwMbEDPaUjcZNYpc6ekX6h8bmtJdBAvVAzdslAjR2ZhRVxYNEr2MbIuNcnUYU0JbE8OESzUp/W8lRil/VW/PLcLTMkxCYCqVmllfz0laQEqpz3hDSKUaqQodEUcP8cLHTgnOyxUNDj9oGEk7jlFjSRM5Hi6ltLDUmp3rPs/s2r13hAE5aoPcXcr9xFlRWGOnwIRLTRXgIeX90zokgzeN2ZJwACX9zLeCxgIhWfCuNuMYyUq12sGZSo8IC9PpV86X9wAxGvCMoRPma0FUxMaxC0GqPdreMDwnXrmFDm+iLuzz4NvFvETklPVf8ipoWqqd+3KGWBkbR0LchFGl9i/CoX1RvI20xr6nzccImZKrcR1rmH6WhliqdxZd676iGL4KV0qYs= hazadus@MacBook-Air-Alexander.local
```
```Bash
ssh-keyscan host | ssh-keygen -lf -
# credits: https://unix.stackexchange.com/questions/126908/get-ssh-server-key-fingerprint
```