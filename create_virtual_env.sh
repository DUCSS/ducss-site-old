#!/bin/bash
txtred='\e[00;31m' # Red
txtgrn='\e[00;32m' # Green
txtylw='\e[00;33m' # Yellow
txtpur='\e[0;35m'  # Purple
txtrst='\e[00m'    # Text Reset
function success() {
    echo -e ${txtgrn}$1${txtrst};
}
function info() {
    echo -e ${txtylw}$1${txtrst};
}
function warn() {
    echo -e ${txtpur}$1${txtrst};
}
function error() {
    echo -e ${txtred}$1${txtrst};
}
function run() 
{
    # Run the command
    info "Running: $1"
    eval $1
    # Check if it succeeded
    if [ "$?" != 0 ]; then
        error "$1 [FAILED]"
        exit 1
    else
        success "$1 [OK]"
    fi
}

# The location of this script
script_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

rm -rf env
virtualenv env
source env/bin/activate

run "pip install -U setuptools"
run "pip install -r ${script_dir}/requirements.txt"
