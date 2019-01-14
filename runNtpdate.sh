hosts='ntp1.aliyun.com ntp2.aliyun.com ntp3.aliyun.com ntp4.aliyun.com cn.pool.ntp.org'
for i in $hosts
do
	echo $i
	ntpdate $i
done
