[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/asottile/awshelp/master.svg)](https://results.pre-commit.ci/latest/github/asottile/awshelp/master)

awshelp
=======

awshelp forwards arguments to `aws` unless `-h` or `--help` are present

### install + setup

```bash
pip install awshelp
alias aws=awshelp
```

### motivation

I am sick and tired of:

**awscli 1.x**

```console
$ aws s3 --help

Unknown options: --help
```

**awscli 2.x**

```console
$ aws s3 --help
usage: aws [-h] [--profile PROFILE] [--debug]

optional arguments:
  -h, --help         show this help message and exit
  --profile PROFILE
  --debug
```

### in action

```console
$ aws s3 cp --help | head -10
awshelp: aws does not like --help, but I got you!
CP()                                                                      CP()



NAME
       cp -

DESCRIPTION
       Copies a local file or S3 object to another location locally or in S3.
```

it even works if you have arguments!

```console
$ aws s3 cp foo bar --help | head -10
awshelp: aws does not like --help, but I got you!
CP()                                                                      CP()



NAME
       cp -

DESCRIPTION
       Copies a local file or S3 object to another location locally or in S3.
```
