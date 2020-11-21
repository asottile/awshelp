import sys

if sys.platform == 'win32':  # pragma: win32 no cover
    import subprocess

    def execvp(cmd: str, args: 'list[str]') -> int:
        return subprocess.call(args)
else:  # pragma: posix no cover
    from os import execvp


def main() -> int:
    if '-h' not in sys.argv and '--help' not in sys.argv:
        return execvp('aws', sys.argv)

    print('awshelp: aws does not like --help, but I got you!', file=sys.stderr)
    cmd = ['aws']
    for arg in sys.argv[1:3]:
        if arg.startswith('-'):
            break
        else:
            cmd.append(arg)
    cmd.append('help')
    return execvp(cmd[0], cmd)


if __name__ == '__main__':
    exit(main())
