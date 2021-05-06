# aws-lightsail-network-metrics

## Usage
```
$ git clone https://...
$ cd aws-lightsail-network-metrics
$ pip install boto3

$ ./aws-lightsail-network-metrics.py 
./aws-lightsail-network-metrics.py [lightsail_instance_name]

$ ./$ ./aws-lightsail-network-metrics.py example-instance-name
# lightsail_instance_name = example-instance-name
lightsail_instance_total_network_out_bytes 178144198
lightsail_instance_total_network_out_percent 0.016202
lightsail_instance_total_network_in_bytes 202146405
lightsail_instance_byte_per_month_alloocated 1099511627776

# for Prometheus Pushgateway
$ ./aws-lightsail-network-metrics.py example-instance-name | curl --data-binary @- http://pushgateway:9091/metrics/job/lightsail_network_metrics/instance/example-instance-name

$ crontab -e
*/3 * * * * $HOME/work/aws-lightsail-network-metrics/aws-lightsail-network-metrics.py example-instance-name | curl --data-binary @- http://pushgateway:9091/metrics/job/lightsail_network_metrics/instance/example-instance-name >/dev/null 2>&1

```

## Copyright and license
Copyright (c) 2021 yoggy

Released under the [MIT license](LICENSE.txt)
