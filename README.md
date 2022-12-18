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
The experimental branch automatically deploys the experimental (test) version of the bot (actual discord bot). [merge allowed from dev branches]
The main branch automatically deploys the actual bot. [merge allowed from dev branch if tests are green + restrict permissions for that!]

## Planned Features

- Rewrite bot functions
  - Stateless
  - Specification?
  - Good folder structure
  - no unnecessary files/classes/utils etc.
  - decouple bot <-> server interactions (roles names etc.) in the most convenient manner
- Write tests
  - Use dpytest (https://dpytest.readthedocs.io/en/latest/tutorials/using_pytest.html)
  - Test commands end to end
  - Coverage %
- Build ci pipeline
  - All secrets with env vars and with GitHub secrets!
  - Docker-compose + Docker image to dockerhub
  - Run tests on dev branch
  - Deploy stable and experimental version on respective branch merges

## Credit

## Contributing

## Conventions

## License
