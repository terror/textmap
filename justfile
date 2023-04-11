set dotenv-load

export EDITOR := 'nvim'

alias f := fmt
alias r := run

default:
  just --list

all: forbid fmt-check

deploy:
  railway up

forbid:
  ./bin/forbid

fmt:
  isort . && yapf --in-place --recursive .
  prettier --write .

fmt-check:
  isort -c . && yapf --diff --recursive .
  prettier --check .

run:
  python3 app.py
