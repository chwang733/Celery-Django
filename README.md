Installation
1. create a virutal environment
>> python -m venv my_venv
>> cd my_venv
>> source bin/activate

2. copy the testbench-celery folder under your virtual environment (e.g. my_venv/testbench-celery)

3. Install all packages
>> cd testbench-celery
>> pip install -r requirements.txt

4. Install redis on macOS
>> brew install redis
>> brew services start redis
>> redis-cli ping

5. Properly setup your SSH 
There is a remote SSH task setup in celery, so you need to properly setup your SSH
- follow a tutorial to create your private/public key pairs
- you might have to install ssh server to accept incoming SSH
- create authorized_keys file 
>> cat id_rsa.pub >> authorized_keys

Try to ssh yourusername@yourmachinename "ls -l" If you can login and see the output of ls -l. You are good to go

6. copy the /testbench-celery/test.sh to your home directory
>> chmod +x test.sh  

7. Create a super user 
>> python manage.py createsuperuser

8. You are ready to run the django web and celery
Open 3 separated command windows and execute the following commands in each window (make sure you activate the venv and cd testbench-celery )
>> python manage.py runserver
>> celery -A celerytest.celery worker -l INFO
>> celery -A celerytest beat -l INFO

9. Open a browser and navigate to http://localhost:8000/admin/ You shall see some celery tables
Open the "periodic tasks" and modify the arguments of the job( at the bottom. click show to display). Modify the 1st argument to your machine's name
This job is scheduled to run every minute to invoke a remote SSH script and dump the output into celery. You can open tasks ( in /admin/) to see the execution results