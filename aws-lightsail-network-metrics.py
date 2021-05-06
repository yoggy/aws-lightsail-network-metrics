#!/usr/bin/python3
import sys
import boto3
import json
from datetime import datetime
from dateutil.relativedelta import relativedelta
from pprint import pprint

def usage():
  print("%s [lightsail_instance_name]" % __file__)
  exit(0)

if len(sys.argv) == 1:
  usage()

target_name = sys.argv[1]

lightsail = boto3.client('lightsail')

instances = lightsail.get_instances()
n = datetime.now()
st = datetime(n.year, n.month, 1)
et = st + relativedelta(months=2)
t = int((et - st).total_seconds())

for i in instances['instances']:
  name = i['name']
  if name == target_name:
    total_network_out = 0
    total_network_in = 0
    gb_per_month_allocated = 0
    byte_per_month_allocated = 0

    try:
      rv = lightsail.get_instance_metric_data(instanceName=name, metricName='NetworkOut', period=t, startTime=st, endTime=et, unit='Bytes', statistics=['Sum'])
      total_network_out = rv['metricData'][0]['sum']
    except:
      pass

    try:
      rv = lightsail.get_instance_metric_data(instanceName=name, metricName='NetworkIn', period=t, startTime=st, endTime=et, unit='Bytes', statistics=['Sum'])
      total_network_in = rv['metricData'][0]['sum']
    except:
      pass

    try:
      gb_per_month_allocated = i['networking']['monthlyTransfer']['gbPerMonthAllocated']
      byte_per_month_allocated = gb_per_month_allocated * 1024 * 1024 * 1024
    except:
      pass

    print("# lightsail_instance_name = %s" % target_name)
    print("lightsail_instance_total_network_out_bytes %d" % total_network_out)
    print("lightsail_instance_total_network_out_percent %f" % (total_network_out / float(byte_per_month_allocated) * 100))
    print("lightsail_instance_total_network_in_bytes %d" % total_network_in)
    print("lightsail_instance_byte_per_month_alloocated %d" % (byte_per_month_allocated))
