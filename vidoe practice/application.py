from configparser import ConfigParser

file = 'config.ini'

# ConfigParser parses the config file
config = ConfigParser()
config.read(file)

# Accessing elements
print(config.sections())
print(config['account'])
print(list(config['account']))

print(config['account']['pin'])

# Updating the config
config.add_section('bank')
config.set('bank', 'name', 'hsbc')

with  open(file, 'w') as configfile:
    config.write(configfile)
