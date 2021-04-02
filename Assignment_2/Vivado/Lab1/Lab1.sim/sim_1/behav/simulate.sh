#!/bin/bash -f
xv_path="/opt/Xilinx/Vivado/2017.2"
ExecStep()
{
"$@"
RETVAL=$?
if [ $RETVAL -ne 0 ]
then
exit $RETVAL
fi
}
ExecStep $xv_path/bin/xsim rgb2grayscale_tb_behav -key {Behavioral:sim_1:Functional:rgb2grayscale_tb} -tclbatch rgb2grayscale_tb.tcl -view /home/viet/Documents/UIT/CE434.L21-Group3/Assignment_2/Vivado/Lab1/Output/rgb2grayscale_tb_behav.wcfg -log simulate.log
