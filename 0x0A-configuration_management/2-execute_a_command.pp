# Creating manifest killing process killmenow

exec { 'pkill':
  command  => 'pkill killmenow',
  provider => 'shell',
}
