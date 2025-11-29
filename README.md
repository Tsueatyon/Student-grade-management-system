# Project1
1, Student Grade Management System

http://54.172.200.184/

Username:admin

Password admin#1234


This project is designed to help teachers manage their students' grades in a more efficient way. Teachers can login with their teacher account and manage students grade information. Both teacher account information and student account information can be add,delete and edit after login.

• Load-tested full-stack Vue 3 + Flask student grade management system using Postman Collection Runner:
  handled 100 concurrent virtual users with 4,224 requests at 61 req/sec, 80 ms average response time,
  < 190 ms p99 latency, and 0% error rate on a single $8/month AWS t3.micro instance (Nginx + gevent + MySQL)

In this project, I developed three front-end web pages, routers,and back-end APIs.
There is a login page and after logged in authorized visitors can add, delete, and edit information of teacher's accounts and student account. Users can only login to the system with information from the teacher's account page.

The front-end page provides an interface for users to use and present data. For front-end development, I used Vue as framework. Used HTML,CSS, and JAVASCRIPT to develop front-end page. To make the web page more pleasing-to-the-eye and make it easier to develop, I introduced UI tools from iView. Used Vue-Router to jump between multiple web pages.Used axios to send data to backedend,and interact with back-end API by HTTP protocol in the structure of JSON. Used NMP to manage dependencies. 

Back-end is responsible for managing data, executing logic, and send processed data back to the front-end. Backend code is written in Python3. Used flase_sqlalchemy to operate database. As well as Flask_cors and genvent from Flask framework. I adpted Mysql as database. Deployed the project on AWS. Used nginx for frontend deployment.

Development tools: Pycharm, Postman and chrome

<img width="1282" height="937" alt="image" src="https://github.com/user-attachments/assets/7a2a8fa4-b41f-4716-9d4b-bd4471aa8832" />
