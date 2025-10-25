# functions-from-zero
live training

[![Python application test with Github Actions](https://github.com/Yaribar/functions-from-zero/actions/workflows/main.yml/badge.svg)](https://github.com/Yaribar/functions-from-zero/actions/workflows/main.yml)

### To call Microservice

something like this

'''
curl -X 'POST' \
  'https://wretched-spooky-fishsticks-7r6xwrq5795cj5q-8080.app.github.dev/wiki' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Microsoft"
}'
'''

### Build container

`docker build .`
`docker image ls`

### Run container

something like this

`docker run -p 127.0.0.1:8080:8080 69c576b986bb`

### Invoke POST request

run `invoke.sh`

## References

