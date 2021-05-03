
from pexpect import pxssh
from datetime import datetime
from colorama import init, Fore, Back, Style
import sys
import time



class UbiSsh():
        
    success = []
    failed = []

    def __init__(self):
        try:
            self.log_file = open('log.txt','a')
            self.err_file = open('log_error.txt','a')
            ip = ''
            name = ''
            host_banner = ''
            conn = pxssh.pxssh()
        except:
            print('Log file not found')
        pass
    
    def __del__(self):
        self.log_file.close()

    def sshConn(self,target,usr,passwd):
        self.ssh = pxssh.pxssh(timeout=30)
        try:
            init(autoreset=True)
            if self.ssh.login(target,usr,passwd):
                now = datetime.now()
                host_banner_cmd = 'uname -a'
                self.ssh.sendline(host_banner_cmd)
                self.ssh.prompt()
                print(Fore.GREEN+'[+] New Connection to {}'.format(target))
                self.host_banner = self.ssh.before.decode('utf-8').strip(host_banner_cmd).strip()
                print('\t-> ', self.host_banner)
                self.log_file.write('{}- Login Successful on {}\n'.format(now,target))
                self.success.append(target)
                self.ip=target
                self.conn = self.ssh
                return self.ssh
            else:
                raise Exception('Bad register')
        except Exception as err:
            now = datetime.now()
            print(Fore.RED+'[+] No Connection to {} | {}'.format(target,err))
            self.failed.append(target)
            self.log_file.write('{}- {} on {} \n'.format(now,err,target))
            return None
    
    def sshClose(self,conn):
        try:
            self.conn.close()
            print(Fore.RED+'[-]' + Fore.WHITE+' Session {} closed'.format(self.ip))
        except Exception as err:
            print(err)

    def sshStats(self):
        return self.success,self.failed

    def sshCmd(self,cmd):
        try:
            self.conn.sendline(cmd)
            self.conn.prompt(timeout=120)
            output = self.conn.before.decode('utf-8').strip(cmd)
            separator=Fore.WHITE+'-----------------------------------------------------------------------------------------------------------'
            print(separator)
            print(Fore.GREEN+'{} - {}'.format(self.ip,self.host_banner))
            print(separator)
            print(output)
        except Exception as ex:
            print('Something went wrong... ')
            now = datetime.now()
            self.log_file.write('{}- {} on {} \n'.format(now,ex,self))