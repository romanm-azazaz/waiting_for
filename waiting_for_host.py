import argparse
import os
import socket
import subprocess
import time

red = '\033[31m'
turquoise = '\033[36m'

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', default=False, help='Target host')
    parser.add_argument('--port', default=False, help='Target port')
    parser.add_argument('--timeout', default=False, help='Timeout in seconds')
    parser.add_argument('--call_command', default=False, help='Execute command with args after the test finishes')
    script_arg = parser.parse_args()
    return script_arg

def check_host(host, port):
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = client.connect_ex((host, port))
        client.close()
        if result == 0: return True
        else: return False
    except socket.gaierror:
        print(f'Name or service {host}:{port} not known')
    except Exception as e:
        print(e)

def call_command(command):
    subprocess.call(f'{command}', shell=True)

def main():
    while True:
        print(f'{red} Check host ... ')
        if check_host(HOST, PORT): break
        else: time.sleep(TIMEOUT)

    print(f'{turquoise} Call command ...')
    call_command(CALL_COMMAND)

if __name__ == '__main__':
    script_arg = create_parser()

    HOST = script_arg.host
    PORT = int(script_arg.port)
    TIMEOUT = int(script_arg.timeout)
    CALL_COMMAND = script_arg.call_command

    main()

