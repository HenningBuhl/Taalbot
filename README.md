# Taalbot

!!!EVERYTHING IS UNDER CONSTRUCTION!!!

## Table of Contents

## Introduction

## Getting Started

### Repo Setup

### Server Setup

Create two folders ("taalbot", "taalbot-experimental") in user dir on server
Install git
Install docker
Setup private key (save in GitHub Secret "HOST_SSH_PRIVATE_KEY") [https://github.com/appleboy/ssh-action#setting-up-ssh-key]
Create docker user group to GitHub Actions can use docker?

### Installation

Python version 3.10
    install requirements

### Testing Locally

Run from root dir:
    pytest --capture=sys --cov=src/

## Workflow

The dev branch is used for development (has github action for tests). [merge allowed from feature branches]
The experimental branch automatically deploys the experimental (test) version of the bot (actual discord bot). [merge allowed from dev branches, even if tests are red]
The main branch automatically deploys the actual, real bot. [merge allowed from dev branch if tests are green]

## Planned Features

- Rewrite bot functions
  - [TODO] Redo old functions
  - [DONE] New folder structure
  - [TODO] decouple bot <-> server interactions (roles names etc.) in the most convenient manner
  - [TODO] revamp logging (locally and on guild)
- Write tests
  - [DONE] Use dpytest (https://dpytest.readthedocs.io/en/latest/tutorials/using_pytest.html)
  - [TODO] Test commands end to end
  - [DONE] Coverage %
- Build ci pipeline
  - [TODO] All secrets with env vars and with GitHub secrets!
  - [TODO] Docker-compose + Docker image to dockerhub
  - [DONE] Run tests on dev branch
  - [TODO] Deploy main and experimental version on respective branch merges/commits

## Contributing

## License
