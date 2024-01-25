# Adjust the configuration to prevent failed requests

exec { 'adjust nginx request limit':
    command  => 'sudo sed -i "s/15/4096/g" /etc/default/nginx && sudo service nginx restart',
    provider => shell,
}
