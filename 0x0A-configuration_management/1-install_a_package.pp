#!/usr/bin/pup
# Installing specific version of flask (2.1.0) using puppet
package { 'Flask':
ensure   => '2.1.0',
provider => 'pip3',}
