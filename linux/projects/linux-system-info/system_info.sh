#!/bin/bash
print_header() {
    echo "======================================"
    echo "      Linux System Information       "
    echo "======================================"
}
echo -e "\n"

echo "==========================================="
echo " Welcome to Linux System Information Tool "
echo "==========================================="
echo

read -p "What is your name? " name
echo
echo "Hello, $name! 👋"
echo "Here is your Linux system information."
echo
print_header

Username=$(whoami)
SystemDate=$(date)
SystemTime=$(date +%T)
CurrentGroups=$(groups)
CurrentKernelVersion=$(uname -r)
Hostname=$(hostname)
SystemUptime=$(uptime)
Distribution=$(grep PRETTY_NAME /etc/os-release | cut -d= -f2 | tr -d '"')
Architecture=$(uname -m)
CurrentDirectory=$(pwd)

Green='\033[0;32m'
Blue='\033[0;34m'
NC='\033[0m'

echo -e "${Green}Current User: ${NC}$Username"
echo -e "${Green}Current Date: ${NC}$SystemDate"
echo -e "${Green}Current Time: ${NC}$SystemTime"
echo -e "${Green}Current Groups:${NC} ${CurrentGroups}"
echo -e "${Green}Current Kernel Version: ${NC}$CurrentKernelVersion"
echo -e "${Green}Hostname: ${NC}$Hostname"
echo -e "${Green}System Uptime:${NC} ${SystemUptime}"
echo -e "${Green}Distribution:${NC} ${Distribution}"
echo -e "${Green}Architecture:${NC} ${Architecture}"
echo -e "${Green}Current Directory:${NC} ${CurrentDirectory}"

echo "======================================"