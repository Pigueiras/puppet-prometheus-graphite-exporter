metrics = [
'./puppetdb/facts/find/p95.wsp',
'./puppetdb/facts/find/count.wsp',
'./puppetdb/facts/find/min.wsp',
'./puppetdb/facts/find/p50.wsp',
'./puppetdb/resource/search/max.wsp',
'./puppetdb/resource/search/p50.wsp',
'./puppetdb/command/submit/max.wsp',
'./puppetdb/command/submit/p75.wsp',
'./puppetdb/report/process/count.wsp',
'./puppetdb/report/process/stddev.wsp',
'./puppetdb/report/process/min.wsp',
'./puppetdb/report/process/p75.wsp',
'./puppetdb/report/process/p50.wsp',
'./puppetdb/catalog/save/count.wsp',
'./puppetdb/catalog/save/min.wsp',
'./puppetdb/catalog/save/mean.wsp',
'./puppetdb/catalog/save/p50.wsp',
'./functions/stddev.wsp',
'./functions/min.wsp',
'./functions/mean.wsp',
'./compiler/p95.wsp',
'./compiler/find_facts/stddev.wsp',
'./compiler/find_facts/min.wsp',
'./compiler/find_facts/p75.wsp',
'./compiler/find_facts/p50.wsp',
'./compiler/stddev.wsp',
'./compiler/max.wsp',
'./compiler/compile/stddev.wsp',
'./compiler/compile/min.wsp',
'./compiler/find_node/count.wsp',
'./compiler/find_node/stddev.wsp',
'./compiler/find_node/mean.wsp',
'./compiler/find_node/p75.wsp',
'./compiler/min.wsp',
'./compiler/p50.wsp',
'./jruby/free-jrubies-histo/stddev.wsp',
'./jruby/free-jrubies-histo/min.wsp',
'./jruby/free-jrubies-histo/p50.wsp',
'./jruby/lock-wait-timer/p95.wsp',
'./jruby/lock-wait-timer/mean.wsp',
'./jruby/lock-wait-timer/p75.wsp',
'./jruby/borrow-timer/p95.wsp',
'./jruby/borrow-timer/count.wsp',
'./jruby/borrow-timer/max.wsp',
'./jruby/borrow-timer/min.wsp',
'./jruby/borrow-timer/mean.wsp',
'./jruby/borrow-timer/p75.wsp',
'./jruby/borrow-timer/p50.wsp',
'./jruby/num-jrubies.wsp',
'./jruby/request-count/count.wsp',
'./jruby/lock-held-timer/p95.wsp',
'./jruby/lock-held-timer/stddev.wsp',
'./jruby/lock-held-timer/max.wsp',
'./jruby/lock-held-timer/min.wsp',
'./jruby/lock-held-timer/mean.wsp',
'./jruby/lock-held-timer/p75.wsp',
'./jruby/lock-held-timer/p50.wsp',
'./jruby/num-free-jrubies.wsp',
'./jruby/requested-jrubies-histo/max.wsp',
'./jruby/requested-jrubies-histo/p75.wsp',
'./jruby/wait-timer/p95.wsp',
'./jruby/wait-timer/count.wsp',
'./jruby/wait-timer/stddev.wsp',
'./jruby/wait-timer/p75.wsp',
'./jruby/wait-timer/p50.wsp',
'./jruby/return-count/count.wsp',
'./memory/total/committed.wsp',
'./memory/total/used.wsp',
'./memory/heap/init.wsp',
'./memory/heap/committed.wsp',
'./memory/heap/used.wsp',
'./memory/non-heap/used.wsp',
'./http/active-histo/p95.wsp',
'./http/active-histo/count.wsp',
'./http/active-histo/stddev.wsp',
'./http/active-histo/min.wsp',
'./http/active-histo/p75.wsp',
'./http/puppet-v3-node-/*/-percentage.wsp',
'./http/puppet-v3-node-/*/-requests/count.wsp',
'./http/puppet-v3-node-/*/-requests/stddev.wsp',
'./http/puppet-v3-node-/*/-requests/max.wsp',
'./http/puppet-v3-node-/*/-requests/min.wsp',
'./http/puppet-v3-node-/*/-requests/mean.wsp',
'./http/puppet-v3-node-/*/-requests/p50.wsp',
'./http/puppet-v3-file_bucket_file-/*/-requests/count.wsp',
'./http/puppet-v3-file_bucket_file-/*/-requests/stddev.wsp',
'./http/puppet-v3-file_bucket_file-/*/-requests/min.wsp',
'./http/puppet-v3-file_bucket_file-/*/-requests/mean.wsp',
'./http/puppet-v3-file_bucket_file-/*/-requests/p75.wsp',
'./http/puppet-v3-catalog-/*/-requests/count.wsp',
'./http/puppet-v3-catalog-/*/-requests/stddev.wsp',
'./http/puppet-v3-catalog-/*/-requests/min.wsp',
'./http/puppet-v3-catalog-/*/-requests/mean.wsp',
'./http/puppet-v3-catalog-/*/-requests/p50.wsp',
'./http/total-requests/p95.wsp',
'./http/total-requests/mean.wsp',
'./http/puppet-v3-file_metadatas-/*/-requests/p95.wsp',
'./http/puppet-v3-file_metadatas-/*/-requests/stddev.wsp',
'./http/puppet-v3-file_metadatas-/*/-requests/max.wsp',
'./http/puppet-v3-file_metadatas-/*/-requests/p50.wsp',
'./http/active-requests/count.wsp',
'./http/puppet-v3-file_metadata-/*/-requests/count.wsp',
'./http/puppet-v3-file_metadata-/*/-requests/max.wsp',
'./http/puppet-v3-file_metadata-/*/-requests/min.wsp',
'./http/puppet-v3-file_metadata-/*/-requests/p50.wsp',
'./http/puppet-v3-report-/*/-percentage.wsp',
'./http/puppet-v3-report-/*/-requests/mean.wsp',
'./http/puppet-v3-environments-requests/p95.wsp',
'./http/puppet-v3-environments-requests/stddev.wsp',
'./http/puppet-v3-environments-requests/max.wsp',
'./http/puppet-v3-environments-requests/min.wsp',
'./http/puppet-v3-environments-requests/mean.wsp',
'./http/puppet-v3-environment_classes-/*/-requests/count.wsp',
'./http/puppet-v3-environment_classes-/*/-requests/max.wsp',
'./http/puppet-v3-environment_classes-/*/-requests/min.wsp',
'./http/puppet-v3-environment_classes-/*/-requests/p75.wsp',
'./http/puppet-v3-environment_classes-/*/-requests/p50.wsp',
'./http/puppet-v3-static_file_content-/*/-requests/p95.wsp',
'./http/puppet-v3-static_file_content-/*/-requests/count.wsp',
'./http/puppet-v3-static_file_content-/*/-requests/max.wsp',
'./http/puppet-v3-static_file_content-/*/-requests/min.wsp',
'./http/puppet-v3-static_file_content-/*/-requests/p75.wsp',
'./http/puppet-v3-static_file_content-/*/-requests/p50.wsp',
'./http/puppet-v3-file_content-/*/-percentage.wsp',
'./http/puppet-v3-file_content-/*/-requests/p95.wsp',
'./http/puppet-v3-file_content-/*/-requests/stddev.wsp',
'./http/puppet-v3-file_content-/*/-requests/min.wsp',
'./http/puppet-v3-file_content-/*/-requests/mean.wsp',
'./http/puppet-v3-file_content-/*/-requests/p50.wsp',
'./http-client/experimental/with-metric-id/puppetdb/facts/find/full-response/p95.wsp',
'./http-client/experimental/with-metric-id/puppetdb/facts/find/full-response/max.wsp',
'./http-client/experimental/with-metric-id/puppetdb/facts/find/full-response/mean.wsp',
'./http-client/experimental/with-metric-id/puppetdb/facts/find/full-response/p50.wsp',
'./http-client/experimental/with-metric-id/puppetdb/resource/search/full-response/p95.wsp',
'./http-client/experimental/with-metric-id/puppetdb/resource/search/full-response/stddev.wsp',
'./http-client/experimental/with-metric-id/puppetdb/resource/search/full-response/max.wsp',
'./http-client/experimental/with-metric-id/puppetdb/resource/search/full-response/min.wsp',
'./http-client/experimental/with-metric-id/puppetdb/resource/search/full-response/mean.wsp',
'./http-client/experimental/with-metric-id/puppetdb/resource/search/full-response/p50.wsp',
'./http-client/experimental/with-metric-id/puppetdb/command/replace_facts/full-response/p95.wsp',
'./http-client/experimental/with-metric-id/puppetdb/command/replace_facts/full-response/count.wsp',
'./http-client/experimental/with-metric-id/puppetdb/command/replace_facts/full-response/stddev.wsp',
'./http-client/experimental/with-metric-id/puppetdb/command/replace_facts/full-response/p75.wsp',
'./http-client/experimental/with-metric-id/puppetdb/command/replace_facts/full-response/p50.wsp',
'./http-client/experimental/with-metric-id/puppetdb/command/store_report/full-response/count.wsp',
'./http-client/experimental/with-metric-id/puppetdb/command/store_report/full-response/stddev.wsp',
'./http-client/experimental/with-metric-id/puppetdb/command/store_report/full-response/max.wsp',
'./http-client/experimental/with-metric-id/puppetdb/command/store_report/full-response/p75.wsp',
'./http-client/experimental/with-metric-id/puppetdb/command/store_report/full-response/p50.wsp',
'./http-client/experimental/with-metric-id/puppetdb/command/replace_catalog/full-response/p95.wsp',
'./http-client/experimental/with-metric-id/puppetdb/command/replace_catalog/full-response/stddev.wsp',
'./http-client/experimental/with-metric-id/puppetdb/command/replace_catalog/full-response/max.wsp',
'./http-client/experimental/with-metric-id/puppetdb/command/replace_catalog/full-response/mean.wsp',
'./http-client/experimental/with-metric-id/puppetdb/command/replace_catalog/full-response/p75.wsp',
'./http-client/experimental/with-metric-id/puppetdb/command/replace_catalog/full-response/p50.wsp',
'./http-client/experimental/with-metric-id/puppetdb/query/full-response/p95.wsp',
'./http-client/experimental/with-metric-id/puppetdb/query/full-response/count.wsp',
'./http-client/experimental/with-metric-id/puppetdb/query/full-response/stddev.wsp',
'./http-client/experimental/with-metric-id/puppetdb/query/full-response/max.wsp',
'./http-client/experimental/with-metric-id/puppetdb/query/full-response/mean.wsp',
'./http-client/experimental/with-metric-id/puppetdb/query/full-response/p75.wsp',
'./http-client/experimental/with-metric-id/puppetdb/query/full-response/p50.wsp',
'./num-cpus.wsp',
'./uptime.wsp',
'./compiler/compile/count.wsp',
'./compiler/compile/max.wsp',
'./compiler/compile/mean.wsp',
'./compiler/compile/p75.wsp',
'./compiler/compile/p95.wsp',
'./compiler/compile/p50.wsp',
'./compiler/count.wsp',
'./compiler/mean.wsp',
'./compiler/find_node/min.wsp',
'./compiler/find_node/max.wsp',
'./compiler/find_node/p95.wsp',
'./compiler/find_node/p50.wsp',
'./compiler/p75.wsp',
'./compiler/find_facts/count.wsp',
'./compiler/find_facts/max.wsp',
'./compiler/find_facts/mean.wsp',
'./compiler/find_facts/p95.wsp',
'./jruby/borrow-count/count.wsp',
'./jruby/borrow-timer/stddev.wsp',
'./jruby/borrow-retry-count/count.wsp',
'./jruby/lock-held-timer/count.wsp',
'./jruby/requested-jrubies-histo/min.wsp',
'./jruby/requested-jrubies-histo/count.wsp',
'./jruby/requested-jrubies-histo/mean.wsp',
'./jruby/requested-jrubies-histo/stddev.wsp',
'./jruby/requested-jrubies-histo/p95.wsp',
'./jruby/requested-jrubies-histo/p50.wsp',
'./jruby/lock-wait-timer/min.wsp',
'./jruby/lock-wait-timer/count.wsp',
'./jruby/lock-wait-timer/max.wsp',
'./jruby/lock-wait-timer/stddev.wsp',
'./jruby/lock-wait-timer/p50.wsp',
'./jruby/wait-timer/min.wsp',
'./jruby/wait-timer/max.wsp',
'./jruby/wait-timer/mean.wsp',
'./jruby/free-jrubies-histo/count.wsp',
'./jruby/free-jrubies-histo/max.wsp',
'./jruby/free-jrubies-histo/mean.wsp',
'./jruby/free-jrubies-histo/p75.wsp',
'./jruby/free-jrubies-histo/p95.wsp',
'./jruby/borrow-timeout-count/count.wsp',
'./memory/heap/max.wsp',
'./memory/non-heap/max.wsp',
'./memory/non-heap/init.wsp',
'./memory/non-heap/committed.wsp',
'./memory/total/max.wsp',
'./memory/total/init.wsp',
'./http-client/experimental/with-metric-id/puppetdb/command/replace_catalog/full-response/min.wsp',
'./http-client/experimental/with-metric-id/puppetdb/command/replace_catalog/full-response/count.wsp',
'./http-client/experimental/with-metric-id/puppetdb/command/store_report/full-response/min.wsp',
'./http-client/experimental/with-metric-id/puppetdb/command/store_report/full-response/mean.wsp',
'./http-client/experimental/with-metric-id/puppetdb/command/store_report/full-response/p95.wsp',
'./http-client/experimental/with-metric-id/puppetdb/command/replace_facts/full-response/min.wsp',
'./http-client/experimental/with-metric-id/puppetdb/command/replace_facts/full-response/max.wsp',
'./http-client/experimental/with-metric-id/puppetdb/command/replace_facts/full-response/mean.wsp',
'./http-client/experimental/with-metric-id/puppetdb/query/full-response/min.wsp',
'./http-client/experimental/with-metric-id/puppetdb/resource/search/full-response/count.wsp',
'./http-client/experimental/with-metric-id/puppetdb/resource/search/full-response/p75.wsp',
'./http-client/experimental/with-metric-id/puppetdb/facts/find/full-response/min.wsp',
'./http-client/experimental/with-metric-id/puppetdb/facts/find/full-response/count.wsp',
'./http-client/experimental/with-metric-id/puppetdb/facts/find/full-response/stddev.wsp',
'./http-client/experimental/with-metric-id/puppetdb/facts/find/full-response/p75.wsp',
'./functions/count.wsp',
'./functions/max.wsp',
'./functions/p75.wsp',
'./functions/p95.wsp',
'./functions/p50.wsp',
'./puppetdb/command/submit/min.wsp',
'./puppetdb/command/submit/count.wsp',
'./puppetdb/command/submit/mean.wsp',
'./puppetdb/command/submit/stddev.wsp',
'./puppetdb/command/submit/p95.wsp',
'./puppetdb/command/submit/p50.wsp',
'./puppetdb/catalog/save/max.wsp',
'./puppetdb/catalog/save/stddev.wsp',
'./puppetdb/catalog/save/p75.wsp',
'./puppetdb/catalog/save/p95.wsp',
'./puppetdb/resource/search/min.wsp',
'./puppetdb/resource/search/count.wsp',
'./puppetdb/resource/search/mean.wsp',
'./puppetdb/resource/search/stddev.wsp',
'./puppetdb/resource/search/p75.wsp',
'./puppetdb/resource/search/p95.wsp',
'./puppetdb/report/process/max.wsp',
'./puppetdb/report/process/mean.wsp',
'./puppetdb/report/process/p95.wsp',
'./puppetdb/facts/find/max.wsp',
'./puppetdb/facts/find/mean.wsp',
'./puppetdb/facts/find/stddev.wsp',
'./puppetdb/facts/find/p75.wsp',
'./http/puppet-v3-report-/*/-requests/min.wsp',
'./http/puppet-v3-report-/*/-requests/count.wsp',
'./http/puppet-v3-report-/*/-requests/max.wsp',
'./http/puppet-v3-report-/*/-requests/stddev.wsp',
'./http/puppet-v3-report-/*/-requests/p75.wsp',
'./http/puppet-v3-report-/*/-requests/p95.wsp',
'./http/puppet-v3-report-/*/-requests/p50.wsp',
'./http/puppet-v3-file_content-/*/-requests/count.wsp',
'./http/puppet-v3-file_content-/*/-requests/max.wsp',
'./http/puppet-v3-file_content-/*/-requests/p75.wsp',
'./http/puppet-v3-static_file_content-/*/-percentage.wsp',
'./http/puppet-v3-static_file_content-/*/-requests/mean.wsp',
'./http/puppet-v3-static_file_content-/*/-requests/stddev.wsp',
'./http/puppet-v3-environments-percentage.wsp',
'./http/active-histo/max.wsp',
'./http/active-histo/mean.wsp',
'./http/active-histo/p50.wsp',
'./http/puppet-v3-file_metadatas-/*/-percentage.wsp',
'./http/puppet-v3-file_metadatas-/*/-requests/min.wsp',
'./http/puppet-v3-file_metadatas-/*/-requests/count.wsp',
'./http/puppet-v3-file_metadatas-/*/-requests/mean.wsp',
'./http/puppet-v3-file_metadatas-/*/-requests/p75.wsp',
'./http/puppet-v3-environment_classes-/*/-percentage.wsp',
'./http/puppet-v3-environment_classes-/*/-requests/mean.wsp',
'./http/puppet-v3-environment_classes-/*/-requests/stddev.wsp',
'./http/puppet-v3-environment_classes-/*/-requests/p95.wsp',
'./http/total-requests/min.wsp',
'./http/total-requests/count.wsp',
'./http/total-requests/max.wsp',
'./http/total-requests/stddev.wsp',
'./http/total-requests/p75.wsp',
'./http/total-requests/p50.wsp',
'./http/puppet-v3-file_metadata-/*/-percentage.wsp',
'./http/puppet-v3-file_metadata-/*/-requests/mean.wsp',
'./http/puppet-v3-file_metadata-/*/-requests/stddev.wsp',
'./http/puppet-v3-file_metadata-/*/-requests/p75.wsp',
'./http/puppet-v3-file_metadata-/*/-requests/p95.wsp',
'./http/puppet-v3-environments-requests/count.wsp',
'./http/puppet-v3-environments-requests/p75.wsp',
'./http/puppet-v3-environments-requests/p50.wsp',
'./http/puppet-v3-node-/*/-requests/p75.wsp',
'./http/puppet-v3-node-/*/-requests/p95.wsp',
'./http/puppet-v3-catalog-/*/-percentage.wsp',
'./http/puppet-v3-catalog-/*/-requests/max.wsp',
'./http/puppet-v3-catalog-/*/-requests/p75.wsp',
'./http/puppet-v3-catalog-/*/-requests/p95.wsp',
'./http/puppet-v3-file_bucket_file-/*/-percentage.wsp',
'./http/puppet-v3-file_bucket_file-/*/-requests/max.wsp',
'./http/puppet-v3-file_bucket_file-/*/-requests/p95.wsp',
'./http/puppet-v3-file_bucket_file-/*/-requests/p50.wsp',
]

template = """- match: 'puppetlabs\.(.*)\.{0}'
  match_type: regex
  name: 'puppetlabs_{1}'
"""

print("mappings:")

for m in metrics:
    graphite_metric = (
        m.replace('./', '')
        .replace('-/*/', '<>')
        .replace('/', '|')
        .replace('<>', '-/\*/')
        .replace('.wsp', '')
        .split('|')
    )
    match = '\\.'.join(graphite_metric)

    prometheus_metric = (
            m.replace('./', '')
            .replace('-/*/', '')
            .replace('experimental/with-metric-id/', '')
            .replace('.wsp', '')
            .replace('-', '_')
            .split('/')
    )
    name = '_'.join(prometheus_metric)

    print(template.format(match, name))
