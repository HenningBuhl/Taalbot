# Taalbot

!!!EVERYTHING IS UNDER CONSTRUCTION!!!

## Table of Contents

## Introduction

## Getting Started

### Installation

Python version 3.10
    install requirements

### Testing the Bot Locally

Run tests locally:
    navigate to test directory
    Windows: py -m pytest
    Linux: python3 -m pytest

## Workflow


The dev branch is used for development (has github action for tests). [merge allowed from feature branches]
The main branch contains the latest clean version of the bot (no actions). [merge allowed from dev branche]
The experimental branch automatically deploys the experimental (test) version of the bot (actual discord bot). [merge allowed from dev/main branches]
The release branch automatically deploys the actual bot. [merge allowed from main branche]

## Credit

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
  - Deploy release and dev version on respective branch merges

## Contributing

## Conventions

## License
