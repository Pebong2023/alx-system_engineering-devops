# Adjust the OS configuration to enable successful login for the holberton user and error-free file opening

exec { 'update soft limit for holberton user':
    command  => 'sudo sed -i "s/holberton\ssoft.*/holberton\tsoft\tnofile\t10000/" /etc/security/limits.conf',
    provider => shell,
}

exec { 'update hard limit for holberton user':
    command  => 'sudo sed -i "s/holberton\shard.*/holberton\thard\tnofile\t100000/" /etc/security/limits.conf',
    provider => shell,
}
