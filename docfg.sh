#! /bin/bash

# Set MySQL
echo "### MySQL ###" >> ~/.zshrc
echo "export mysql_host=" >> ~/.zshrc
echo "export mysql_port=" >> ~/.zshrc
echo "export mysql_user=" >> ~/.zshrc
echo "export mysql_password=" >> ~/.zshrc
echo "export mysql_database=" >> ~/.zshrc

source ~/.zshrc
