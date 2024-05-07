import subprocess
 
commands = [
    "sudo apt update",
    "sudo apt upgrade",
    "sudo apt install python3.10",
    "python3.10 --version",
    "sudo apt-get install git",
    "sudo apt-get install python3-dev",
    "sudo apt-get install python3-setuptools python3-pip",
    "sudo apt-get install virtualenv",
    "sudo apt install python3.10-venv",
    "sudo apt-get install software-properties-common",
    "dpkg -l | grep -e mysql -e mariadb",
    "sudo apt install mariadb-server", 
    "sudo /usr/bin/expect /home/senkathir/Documents/mysql_secure_install.expect",
    "sudo apt-get install libmysqlclient-dev",
    "sudo nano /etc/mysql/mariadb.conf.d/50-server.cnf",
    "sudo apt-get install redis-server",
    "sudo apt install curl",
    "curl https://raw.githubusercontent.com/creationix/nvm/master/install.sh | bash",
    "source ~/.profile",
    "nvm install 18",
    "sudo apt-get install npm",
    "sudo npm install -g yarn",
    "sudo apt-get install xvfb libfontconfig wkhtmltopdf",
    "sudo -H pip3 install frappe-bench",
    "bench --version",
    "bench init frappe-bench --frappe-branch version-15 --python python3.10 --verbose",
    "cd frappe-bench/",
    "bench start"

]
for command in commands:
    if command.startswith("sudo nano"):
        # If the command is to open Nano, handle it separately
        process = subprocess.Popen(command, shell=True)
        process.communicate(input=b'\x1B:wq\n')  # Send the save and exit command to Nano
        process.wait()  # Wait for Nano to finish
    else:
        # For other commands, just execute them
        subprocess.run(command, shell=True)





























