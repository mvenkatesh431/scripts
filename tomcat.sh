#!/bin/bash
# description: Tomcat Start Stop Restart
#
processname: tomcat
# chkconfig: 234 20 80

JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk-1.8.0.45-28.b13.el6_6.x86_64/jre/
export JAVA_HOME  
PATH=$JAVA_HOME/bin:$PATH
export PATH  
CATALINA_HOME=/usr/share/apache-tomcat-8.0.24

case $1 in
start)
sh $CATALINA_HOME/bin/startup.sh
;;
stop)
sh $CATALINA_HOME/bin/shutdown.sh
;;
restart)
sh $CATALINA_HOME/bin/shutdown.sh
sh $CATALINA_HOME/bin/startup.sh
;;
esac
exit 0

