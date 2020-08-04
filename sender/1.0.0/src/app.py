import asyncio
import os
from walkoff_app_sdk.app_base import AppBase

class sender(AppBase):
    __version__ = "1.0.0"
    app_name = "sender"  # this needs to match "name" in api.yaml
    def __init__(self, redis, logger, console_logger=None):

        super().__init__(redis, logger, console_logger)

    async def tcpsender(self,ip,speed,start_time="2018-08-11 13:41:11",end_time="2018-08-11 13:41:41",log_path="/var/log/appsimulation/traffic_gen.log"):
        fp = open('/home/config/post_info.json', 'w')
        fp.write('{\n"cmd_info":{\n"cmd":"start"\n},\n"task_info":{\n"log_path":"')
        fp.write(log_path)
        fp.write('",\n"start_time":"')
        fp.write(start_time)
        fp.write('",\n"end_time":"')
        fp.write(end_time)
        fp.write('"\n},\n"behavior_conf":{\n"SERVERTYPE":"')
        fp.write('tcpsender')
        fp.write('",\n"IPADDR":"')
        fp.write(ip)
        fp.write('",\n"send_Constant":"')
        fp.write(speed)
        fp.write('",\n"size_Cauchy1":"500",\n"size_Cauchy2":"1"\n}\n}\n')
        os.system('./tra_docker_make/run.sh')
        return a+"tcpsender finished!"
    async def udpsender(self,ip,speed,start_time="2018-08-11 13:41:11",end_time="2018-08-11 13:41:41",log_path="/var/log/appsimulation/traffic_gen.log"):
        fp = open('/home/config/post_info.json', 'w')
        fp.write('{\n"cmd_info":{\n"cmd":"start"\n},\n"task_info":{\n"log_path":"')
        fp.write(log_path)
        fp.write('",\n"start_time":"')
        fp.write(start_time)
        fp.write('",\n"end_time":"')
        fp.write(end_time)
        fp.write('"\n},\n"behavior_conf":{\n"SERVERTYPE":"')
        fp.write('udpsender')
        fp.write('",\n"IPADDR":"')
        fp.write(ip)
        fp.write('",\n"send_Constant":"')
        fp.write(speed)
        fp.write('",\n"size_Cauchy1":"500",\n"size_Cauchy2":"1"\n}\n}\n')
        os.system('./tra_docker_make/run.sh')
        return "udpsender finished!"
    async def httpsender(self,ip,speed,start_time="2018-08-11 13:41:11",end_time="2018-08-11 13:41:41",log_path="/var/log/appsimulation/traffic_gen.log"):
        fp = open('/home/config/post_info.json', 'w')
        fp.write('{\n"cmd_info":{\n"cmd":"start"\n},\n"task_info":{\n"log_path":"')
        fp.write(log_path)
        fp.write('",\n"start_time":"')
        fp.write(start_time)
        fp.write('",\n"end_time":"')
        fp.write(end_time)
        fp.write('"\n},\n"behavior_conf":{\n"SERVERTYPE":"')
        fp.write('httpsender')
        fp.write('",\n"IPADDR":"')
        fp.write(ip)
        fp.write('",\n"send_Constant":"')
        fp.write(speed)
        fp.write('",\n"size_Cauchy1":"500",\n"size_Cauchy2":"1"\n}\n}\n')
        os.system('./tra_docker_make/run.sh')
        return "httpsender finished!"
    async def icmpsender(self,ip,speed,start_time="2018-08-11 13:41:11",end_time="2018-08-11 13:41:41",log_path="/var/log/appsimulation/traffic_gen.log"):
        fp = open('/home/config/post_info.json', 'w')
        fp.write('{\n"cmd_info":{\n"cmd":"start"\n},\n"task_info":{\n"log_path":"')
        fp.write(log_path)
        fp.write('",\n"start_time":"')
        fp.write(start_time)
        fp.write('",\n"end_time":"')
        fp.write(end_time)
        fp.write('"\n},\n"behavior_conf":{\n"SERVERTYPE":"')
        fp.write('icmpsender')
        fp.write('",\n"IPADDR":"')
        fp.write(ip)
        fp.write('",\n"send_Constant":"')
        fp.write(speed)
        fp.write('",\n"size_Cauchy1":"500",\n"size_Cauchy2":"1"\n}\n}\n')
        os.system('./tra_docker_make/run.sh')
        return "icmpsender finished!"
    async def ftpsender(self,ip,speed,start_time="2018-08-11 13:41:11",end_time="2018-08-11 13:41:41",log_path="/var/log/appsimulation/traffic_gen.log"):
        fp = open('/home/config/post_info.json', 'w')
        fp.write('{\n"cmd_info":{\n"cmd":"start"\n},\n"task_info":{\n"log_path":"')
        fp.write(log_path)
        fp.write('",\n"start_time":"')
        fp.write(start_time)
        fp.write('",\n"end_time":"')
        fp.write(end_time)
        fp.write('"\n},\n"behavior_conf":{\n"SERVERTYPE":"')
        fp.write('ftpsender')
        fp.write('",\n"IPADDR":"')
        fp.write(ip)
        fp.write('",\n"send_Constant":"')
        fp.write(speed)
        fp.write('",\n"size_Cauchy1":"500",\n"size_Cauchy2":"1"\n}\n}\n')
        os.system('./tra_docker_make/run.sh')
        return "ftpsender finished!"
    async def smtpsender(self,ip,speed,start_time="2018-08-11 13:41:11",end_time="2018-08-11 13:41:41",log_path="/var/log/appsimulation/traffic_gen.log"):
        fp = open('/home/config/post_info.json', 'w')
        fp.write('{\n"cmd_info":{\n"cmd":"start"\n},\n"task_info":{\n"log_path":"')
        fp.write(log_path)
        fp.write('",\n"start_time":"')
        fp.write(start_time)
        fp.write('",\n"end_time":"')
        fp.write(end_time)
        fp.write('"\n},\n"behavior_conf":{\n"SERVERTYPE":"')
        fp.write('smtpsender')
        fp.write('",\n"IPADDR":"')
        fp.write(ip)
        fp.write('",\n"send_Constant":"')
        fp.write(speed)
        fp.write('",\n"size_Cauchy1":"500",\n"size_Cauchy2":"1"\n}\n}\n')
        os.system('./tra_docker_make/run.sh')
        return "smtpsender finished!"
    async def rtpsender(self,ip,speed,start_time="2018-08-11 13:41:11",end_time="2018-08-11 13:41:41",log_path="/var/log/appsimulation/traffic_gen.log"):
        fp = open('/home/config/post_info.json', 'w')
        fp.write('{\n"cmd_info":{\n"cmd":"start"\n},\n"task_info":{\n"log_path":"')
        fp.write(log_path)
        fp.write('",\n"start_time":"')
        fp.write(start_time)
        fp.write('",\n"end_time":"')
        fp.write(end_time)
        fp.write('"\n},\n"behavior_conf":{\n"SERVERTYPE":"')
        fp.write('rtpsender')
        fp.write('",\n"IPADDR":"')
        fp.write(ip)
        fp.write('",\n"send_Constant":"')
        fp.write(speed)
        fp.write('",\n"size_Cauchy1":"500",\n"size_Cauchy2":"1"\n}\n}\n')
        os.system('./tra_docker_make/run.sh')
        return "rtpsender finished!"


if __name__ == "__main__":
    asyncio.run(sender.run(), debug=True)
