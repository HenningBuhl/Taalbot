# Taalbot

!!!EVERYTHING IS UNDER CONSTRUCTION!!!

## Table of Contents

## Introduction

## Getting Started

### Installation

Python version 3.10
    install requirements

### Testing Locally

Run from root dir:
    pytest --cov=src/

## Workflow

The dev branch is used for development (has github action for tests). [merge allowed from feature branches]
The experimental branch automatically deploys the experimental (test) version of the bot (actual discord bot). [merge allowed from dev branches, even if tests are red]
The main branch automatically deploys the actual, real bot. [merge allowed from dev branch if tests are green]

## Planned Features

- Rewrite bot functions
  - [TODO] Redo old functions
  - [DONE] New folder structure
  - [TODO] decouple bot <-> server interactions (roles names etc.) in the most convenient manner
- Write tests
  - [DONE] Use dpytest (https://dpytest.readthedocs.io/en/latest/tutorials/using_pytest.html)
  - [TODO] Test commands end to end
  - [DONE] Coverage %
- Build ci pipeline
  - [TODO] All secrets with env vars and with GitHub secrets!
  - [TODO] Docker-compose + Docker image to dockerhub
  - [DONE] Run tests on dev branch
  - [TODO] Deploy stable and experimental version on respective branch merges

## Contributing

## License
