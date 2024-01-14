# kumaone

[![Hatch project](https://img.shields.io/badge/%F0%9F%A5%9A-Hatch-4051b5.svg)](https://github.com/pypa/hatch)
[![PyPI - Version](https://img.shields.io/pypi/v/kumaone.svg)](https://pypi.org/project/kumaone)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/kumaone.svg)](https://pypi.org/project/kumaone)

-----

**Table of Contents**

- [Virtualenv](#virtualenv)
- [Installation](#installation)
- [License](#license)
- [Features](#features)

## Virtualenv

- Install `pipenv` from [here](https://pipenv.pypa.io/en/latest/installation/)

- Activate virtual environment

  ```shell
  pipenv shell
  ```

  > if there are no virtual environment available (e.g. first use), a virtual environment will be created and activated
    automatically.

- Install dependencies

  To install dependencies with `pipenv` use the following command

  ```shell
  pipenv install
  ```

  To install `dev` dependencies use `--dev` flag

  ```shell
  pipenv install --dev
  ```

## Installation

```shell
pip install kumaone
```

## Installation (Dev)

```shell
pip install -e .
```

## License

`kumaone` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.

## To Do List

### Info

- [x] Show information about `kumaone`

### Configuration

- [x] Show `uptime kuma` configuration (default/custom paths)
- [x] Create `uptime kuma` configuration (default/custom path)
- [x] Delete `uptime kuma` configuration
- [ ] Edit `uptime kuma` configuration

### Monitors

- Supported Monitor types (tested)
  - [x] HTTP
  - [x] JSON_QUERY
  - [x] PING
- [x] List all monitors. `groups` and `processes` also.
- [x] Bulk `add` monitors from file(s)
- [x] Bulk `delete` monitors from file(s)
- [ ] Add Single monitor from `inline` dictionary data
- [x] Delete Single Monitor by name

### Status Page

- [x] List all `staus page`(s)
- [x] See details of a `single status page`
- [x] Add a new `status page`
- [x] Add status pages from file(s)
- [x] Delete status page
- [x] Delete status page from file(s)

### Notification

- Supported notification providers (tested)
  - [x] Rocket.Chat
  - [x] Slack
  - [x] MS Teams
  - [x] Webhook
- [x] List all `notification`(s)
- [x] See details of a `single notification` by name/id.
- [ ] Add new notification (interactive)
- [x] Add notifications from single file.
- [ ] Delete notification by name/id.
- [ ] Delete notifications from single file.

### Maintenance

TBA

### Incident

TBA

### Change Password

- [ ] Change password from CLI
- [ ] Update password in `kumaone` config

### Cleanup

- [ ] Clear heartbeats
- [ ] Clear statistics
- [ ] Clear events

### Backlog

- [ ] Don't stop the program if one monitor process runs into error
- [ ] Add debug logs for methods
