# import
import subprocess


###############################
# Design pattern SRC/TEST/ETC #
###############################

# Check path
subprocess.call('ls -la', shell=True)

# Run main app in source
subprocess.call('python src/webapi.py', shell=True)
