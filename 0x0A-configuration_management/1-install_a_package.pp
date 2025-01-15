#!/usr/bin/pup
# Define a package resource for Flask
package { 'Flask':
  ensure   => '2.1.0', # Ensure version 2.1.0 is installed
  provider => 'pip3',  # Use pip3 as the package provider
}
