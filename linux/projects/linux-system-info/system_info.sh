#!/bin/bash
echo "======================================"
echo "         System Information           "
echo "======================================"

echo "Current User: $(whoami)"
echo "Current Date: $(date)"
echo "Current Time: $(date +%T)"
echo "Current Group: $(groups)"
echo "Current kenel Version: $(uname -r)"