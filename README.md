# puppet-prometheus-graphite-exporter
A configuration for graphite-exporter to export Puppet server metrics in Prometheus

## The problem
Puppet servers only export metrics in graphite format, if you want
to export this metrics to be retrieved by Prometheus scrapes you need to use
[graphite-exporter](https://github.com/prometheus/graphite_exporter). There are no plans
to implement a prometheus endpoint in the puppet (from: https://tickets.puppetlabs.com/browse/SERVER-2713).

The default configuration of `graphite-exporter` will export also the name of the
machine (ideally it shouldn't be inside the name of the metric) and also the
format of some metrics (like the experimental puppetdb ones, or the http_puppet_v3)
require some formatting to have a readable name in prometheus.

## The solution
Just use `config.yaml`  with `--graphite.mapping-config="/etc/graphite_exporter/config.yaml"`.
If you are using puppet to configure the exporter you can put the following:

Hiera configuration:
```yaml
# if you are using: https://github.com/theforeman/puppet-puppet
puppet::server_metrics_graphite_enable: true
puppet::server_metrics_graphite_host: localhost
puppet::server_metrics_graphite_port: 9109
puppet::server_metrics_graphite_interval: 60 # seconds
...

prometheus::graphite_exporter::options: >-
  --graphite.mapping-config="/etc/graphite_exporter/config.yaml"
prometheus::graphite_exporter::scrape_port: 9108
```

And in your manifest:

```puppet
...
include ::prometheus::graphite_exporter

file {'/etc/graphite_exporter/config.yaml':
    source => 'puppet:///...'
    owner  => 'graphite-exporter',
    group  => 'graphite-exporter',
    mode   => '0644',
    notify => Service['graphite-exporter'],
}
...
```

## How the configuration file is generated

You can run the generate python script and pipe the output of that script into
a file.

```console
$ python3 generate.py > config.yaml
```

The paths inside the script are the whisper files generated in graphite after
enabling the graphite monitoring in the puppet server.

## Metrics generated

These are the metrics you will see in your exporter when you scrape:

```
puppetlabs_http_active_histo_count 0
puppetlabs_http_active_histo_max 0
puppetlabs_http_active_histo_mean 0
puppetlabs_http_active_histo_min 0
puppetlabs_http_active_histo_p50 0
puppetlabs_http_active_histo_p75 0
puppetlabs_http_active_histo_p95 0
puppetlabs_http_active_histo_stddev 0
puppetlabs_http_active_requests_count 0
puppetlabs_http_puppet_v3_catalog_percentage NaN
puppetlabs_http_puppet_v3_catalog_requests_count 0
puppetlabs_http_puppet_v3_catalog_requests_max 0
puppetlabs_http_puppet_v3_catalog_requests_mean 0
puppetlabs_http_puppet_v3_catalog_requests_min 0
puppetlabs_http_puppet_v3_catalog_requests_p50 0
puppetlabs_http_puppet_v3_catalog_requests_p75 0
puppetlabs_http_puppet_v3_catalog_requests_p95 0
puppetlabs_http_puppet_v3_catalog_requests_stddev 0
puppetlabs_http_puppet_v3_environment_classes_percentage NaN
puppetlabs_http_puppet_v3_environment_classes_requests_count 0
puppetlabs_http_puppet_v3_environment_classes_requests_max 0
puppetlabs_http_puppet_v3_environment_classes_requests_mean 0
puppetlabs_http_puppet_v3_environment_classes_requests_min 0
puppetlabs_http_puppet_v3_environment_classes_requests_p50 0
puppetlabs_http_puppet_v3_environment_classes_requests_p75 0
puppetlabs_http_puppet_v3_environment_classes_requests_p95 0
puppetlabs_http_puppet_v3_environment_classes_requests_stddev 0
puppetlabs_http_puppet_v3_environments_percentage NaN
puppetlabs_http_puppet_v3_environments_requests_count 0
puppetlabs_http_puppet_v3_environments_requests_max 0
puppetlabs_http_puppet_v3_environments_requests_mean 0
puppetlabs_http_puppet_v3_environments_requests_min 0
puppetlabs_http_puppet_v3_environments_requests_p50 0
puppetlabs_http_puppet_v3_environments_requests_p75 0
puppetlabs_http_puppet_v3_environments_requests_p95 0
puppetlabs_http_puppet_v3_environments_requests_stddev 0
puppetlabs_http_puppet_v3_file_bucket_file_percentage NaN
puppetlabs_http_puppet_v3_file_bucket_file_requests_count 0
puppetlabs_http_puppet_v3_file_bucket_file_requests_max 0
puppetlabs_http_puppet_v3_file_bucket_file_requests_mean 0
puppetlabs_http_puppet_v3_file_bucket_file_requests_min 0
puppetlabs_http_puppet_v3_file_bucket_file_requests_p50 0
puppetlabs_http_puppet_v3_file_bucket_file_requests_p75 0
puppetlabs_http_puppet_v3_file_bucket_file_requests_p95 0
puppetlabs_http_puppet_v3_file_bucket_file_requests_stddev 0
puppetlabs_http_puppet_v3_file_content_percentage NaN
puppetlabs_http_puppet_v3_file_content_requests_count 0
puppetlabs_http_puppet_v3_file_content_requests_max 0
puppetlabs_http_puppet_v3_file_content_requests_mean 0
puppetlabs_http_puppet_v3_file_content_requests_min 0
puppetlabs_http_puppet_v3_file_content_requests_p50 0
puppetlabs_http_puppet_v3_file_content_requests_p75 0
puppetlabs_http_puppet_v3_file_content_requests_p95 0
puppetlabs_http_puppet_v3_file_content_requests_stddev 0
puppetlabs_http_puppet_v3_file_metadata_percentage NaN
puppetlabs_http_puppet_v3_file_metadata_requests_count 0
puppetlabs_http_puppet_v3_file_metadata_requests_max 0
puppetlabs_http_puppet_v3_file_metadata_requests_mean 0
puppetlabs_http_puppet_v3_file_metadata_requests_min 0
puppetlabs_http_puppet_v3_file_metadata_requests_p50 0
puppetlabs_http_puppet_v3_file_metadata_requests_p75 0
puppetlabs_http_puppet_v3_file_metadata_requests_p95 0
puppetlabs_http_puppet_v3_file_metadata_requests_stddev 0
puppetlabs_http_puppet_v3_file_metadatas_percentage NaN
puppetlabs_http_puppet_v3_file_metadatas_requests_count 0
puppetlabs_http_puppet_v3_file_metadatas_requests_max 0
puppetlabs_http_puppet_v3_file_metadatas_requests_mean 0
puppetlabs_http_puppet_v3_file_metadatas_requests_min 0
puppetlabs_http_puppet_v3_file_metadatas_requests_p50 0
puppetlabs_http_puppet_v3_file_metadatas_requests_p75 0
puppetlabs_http_puppet_v3_file_metadatas_requests_p95 0
puppetlabs_http_puppet_v3_file_metadatas_requests_stddev 0
puppetlabs_http_puppet_v3_node_percentage NaN
puppetlabs_http_puppet_v3_node_requests_count 0
puppetlabs_http_puppet_v3_node_requests_max 0
puppetlabs_http_puppet_v3_node_requests_mean 0
puppetlabs_http_puppet_v3_node_requests_min 0
puppetlabs_http_puppet_v3_node_requests_p50 0
puppetlabs_http_puppet_v3_node_requests_p75 0
puppetlabs_http_puppet_v3_node_requests_p95 0
puppetlabs_http_puppet_v3_node_requests_stddev 0
puppetlabs_http_puppet_v3_report_percentage NaN
puppetlabs_http_puppet_v3_report_requests_count 0
puppetlabs_http_puppet_v3_report_requests_max 0
puppetlabs_http_puppet_v3_report_requests_mean 0
puppetlabs_http_puppet_v3_report_requests_min 0
puppetlabs_http_puppet_v3_report_requests_p50 0
puppetlabs_http_puppet_v3_report_requests_p75 0
puppetlabs_http_puppet_v3_report_requests_p95 0
puppetlabs_http_puppet_v3_report_requests_stddev 0
puppetlabs_http_puppet_v3_static_file_content_percentage NaN
puppetlabs_http_puppet_v3_static_file_content_requests_count 0
puppetlabs_http_puppet_v3_static_file_content_requests_max 0
puppetlabs_http_puppet_v3_static_file_content_requests_mean 0
puppetlabs_http_puppet_v3_static_file_content_requests_min 0
puppetlabs_http_puppet_v3_static_file_content_requests_p50 0
puppetlabs_http_puppet_v3_static_file_content_requests_p75 0
puppetlabs_http_puppet_v3_static_file_content_requests_p95 0
puppetlabs_http_puppet_v3_static_file_content_requests_stddev 0
puppetlabs_http_total_requests_count 0
puppetlabs_http_total_requests_max 0
puppetlabs_http_total_requests_mean 0
puppetlabs_http_total_requests_min 0
puppetlabs_http_total_requests_p50 0
puppetlabs_http_total_requests_p75 0
puppetlabs_http_total_requests_p95 0
puppetlabs_http_total_requests_stddev 0
puppetlabs_jruby_borrow_count_count 0
puppetlabs_jruby_borrow_retry_count_count 0
puppetlabs_jruby_borrow_timeout_count_count 0
puppetlabs_jruby_borrow_timer_count 0
puppetlabs_jruby_borrow_timer_max 0
puppetlabs_jruby_borrow_timer_mean 0
puppetlabs_jruby_borrow_timer_min 0
puppetlabs_jruby_borrow_timer_p50 0
puppetlabs_jruby_borrow_timer_p75 0
puppetlabs_jruby_borrow_timer_p95 0
puppetlabs_jruby_borrow_timer_stddev 0
puppetlabs_jruby_free_jrubies_histo_count 1332
puppetlabs_jruby_free_jrubies_histo_max 3
puppetlabs_jruby_free_jrubies_histo_mean 3
puppetlabs_jruby_free_jrubies_histo_min 3
puppetlabs_jruby_free_jrubies_histo_p50 3
puppetlabs_jruby_free_jrubies_histo_p75 3
puppetlabs_jruby_free_jrubies_histo_p95 3
puppetlabs_jruby_free_jrubies_histo_stddev 0
puppetlabs_jruby_lock_held_timer_count 0
puppetlabs_jruby_lock_held_timer_max 0
puppetlabs_jruby_lock_held_timer_mean 0
puppetlabs_jruby_lock_held_timer_min 0
puppetlabs_jruby_lock_held_timer_p50 0
puppetlabs_jruby_lock_held_timer_p75 0
puppetlabs_jruby_lock_held_timer_p95 0
puppetlabs_jruby_lock_held_timer_stddev 0
puppetlabs_jruby_lock_wait_timer_count 0
puppetlabs_jruby_lock_wait_timer_max 0
puppetlabs_jruby_lock_wait_timer_mean 0
puppetlabs_jruby_lock_wait_timer_min 0
puppetlabs_jruby_lock_wait_timer_p50 0
puppetlabs_jruby_lock_wait_timer_p75 0
puppetlabs_jruby_lock_wait_timer_p95 0
puppetlabs_jruby_lock_wait_timer_stddev 0
puppetlabs_jruby_num_free_jrubies 3
puppetlabs_jruby_num_jrubies 3
puppetlabs_jruby_request_count_count 0
puppetlabs_jruby_requested_jrubies_histo_count 1332
puppetlabs_jruby_requested_jrubies_histo_max 0
puppetlabs_jruby_requested_jrubies_histo_mean 0
puppetlabs_jruby_requested_jrubies_histo_min 0
puppetlabs_jruby_requested_jrubies_histo_p50 0
puppetlabs_jruby_requested_jrubies_histo_p75 0
puppetlabs_jruby_requested_jrubies_histo_p95 0
puppetlabs_jruby_requested_jrubies_histo_stddev 0
puppetlabs_jruby_return_count_count 0
puppetlabs_jruby_wait_timer_count 0
puppetlabs_jruby_wait_timer_max 0
puppetlabs_jruby_wait_timer_mean 0
puppetlabs_jruby_wait_timer_min 0
puppetlabs_jruby_wait_timer_p50 0
puppetlabs_jruby_wait_timer_p75 0
puppetlabs_jruby_wait_timer_p95 0
puppetlabs_jruby_wait_timer_stddev 0
puppetlabs_memory_heap_committed 3.670016e+09
puppetlabs_memory_heap_init 3.670016e+09
puppetlabs_memory_heap_max 3.670016e+09
puppetlabs_memory_heap_used 5.19258112e+08
puppetlabs_memory_non_heap_committed 2.56520192e+08
puppetlabs_memory_non_heap_init 7.667712e+06
puppetlabs_memory_non_heap_max -1
puppetlabs_memory_non_heap_used 2.35856424e+08
puppetlabs_memory_total_committed 3.926536192e+09
puppetlabs_memory_total_init 3.677683712e+09
puppetlabs_memory_total_max 3.670015999e+09
puppetlabs_memory_total_used 7.55114536e+08
puppetlabs_num_cpus 4
puppetlabs_uptime 6.678066e+06
```
