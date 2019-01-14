logId=`date +%Y-%m-%d-%H%M`
pid_file=run.pid
nohup python run.py 2>&1 >run.$logId.log &

echo $logId >>${pid_file}
echo $! >> ${pid_file}