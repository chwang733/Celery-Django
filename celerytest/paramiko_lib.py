import paramiko
 
def paramiko_remoteshell(hostname, command):
    print('running')
    try:
        port = '22'
         
        # created client using paramiko
        client = paramiko.SSHClient()
         
        # here we are loading the system
        # host keys
        client.load_system_host_keys()
         
        # connecting paramiko using host
        # name and password
        client.connect(hostname, port=22, username='chihchungwang')
         
        # below line command will actually
        # execute in your remote machine
        (stdin, stdout, stderr) = client.exec_command(command, get_pty=True)
         
        # redirecting all the output in cmd_output
        # variable
        cmd_output = stdout.read()
        # print('log printing: ', command, cmd_output)
        exit_code = stdout.channel.recv_exit_status()

        cmd_err = ""
        if exit_code != 0:
            cmd_err =stderr.read()
            # print('error printing: ', command, cmd_err)
        
        ret = { "exit_code" : exit_code, "stdinfo": str(cmd_output), "stderror": str(cmd_err)}

        return ret
        
    finally:
        client.close()

# print(paramiko_remoteshell('lg-ubuntu', './test.sh'))
