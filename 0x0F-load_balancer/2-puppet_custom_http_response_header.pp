# Using Puppet to automate task of creating custom HTTP header response
# 2-puppet_custom_http_response_header.pp

# Installing puppetlabs  module
package { 'puppet-module-puppetlabs-stdlib':
  ensure => 'installed',
}

# Updating the package of repo
exec { 'update':
  command => '/usr/bin/apt-get update',
}

# Installing Nginx package
package { 'nginx':
  ensure => 'installed',
}

# Configuring Nginx with custom HTTP header
class { 'stdlib': }

file_line { 'custom_http_header':
  path  => '/etc/nginx/nginx.conf',
  line  => "add_header X-Served-By ${hostname};",
  match => 'http {',
}

notify { 'custom_http_header':
  require => File_line['custom_http_header'],
}

# Restarting Nginx to apply modifications
exec { 'run':
  command => '/usr/sbin/service nginx restart',
}
