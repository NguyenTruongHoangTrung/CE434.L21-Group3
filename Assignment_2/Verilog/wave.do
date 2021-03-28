onerror {resume}
quietly WaveActivateNextPane {} 0
add wave -noupdate -expand -group Input /rgb2grayscale_tb/dut/clk
add wave -noupdate -expand -group Input /rgb2grayscale_tb/dut/din_valid
add wave -noupdate -expand -group Input -radix unsigned /rgb2grayscale_tb/dut/R
add wave -noupdate -expand -group Input -radix unsigned /rgb2grayscale_tb/dut/G
add wave -noupdate -expand -group Input -radix unsigned /rgb2grayscale_tb/dut/B
add wave -noupdate -expand -group Output -radix unsigned /rgb2grayscale_tb/dut/grayscale
add wave -noupdate -expand -group Output /rgb2grayscale_tb/dut/dout_valid
add wave -noupdate -expand -group Extend -radix unsigned /rgb2grayscale_tb/dut/R_16
add wave -noupdate -expand -group Extend -radix unsigned /rgb2grayscale_tb/dut/G_16
add wave -noupdate -expand -group Extend -radix unsigned /rgb2grayscale_tb/dut/B_16
add wave -noupdate -expand -group {State 0} -radix unsigned /rgb2grayscale_tb/dut/s0_0
add wave -noupdate -expand -group {State 0} -radix unsigned /rgb2grayscale_tb/dut/s0_1
add wave -noupdate -expand -group {State 0} -radix unsigned /rgb2grayscale_tb/dut/s0_2
add wave -noupdate -expand -group {State 0} -radix unsigned /rgb2grayscale_tb/dut/s0_3
add wave -noupdate -expand -group {State 0} -radix unsigned /rgb2grayscale_tb/dut/s0_4
add wave -noupdate -expand -group {State 0} -radix unsigned /rgb2grayscale_tb/dut/s0_5
add wave -noupdate -expand -group {State 0} -radix unsigned /rgb2grayscale_tb/dut/s0_din_valid
add wave -noupdate -expand -group {State 1} -radix unsigned /rgb2grayscale_tb/dut/s1_0
add wave -noupdate -expand -group {State 1} -radix unsigned /rgb2grayscale_tb/dut/s1_1
add wave -noupdate -expand -group {State 1} -radix unsigned /rgb2grayscale_tb/dut/s1_2
add wave -noupdate -expand -group {State 1} -radix unsigned /rgb2grayscale_tb/dut/s1_din_valid
add wave -noupdate -expand -group {State 2} -radix unsigned /rgb2grayscale_tb/dut/s2_0
add wave -noupdate -expand -group {State 2} -radix unsigned /rgb2grayscale_tb/dut/s2_1
add wave -noupdate -expand -group {State 2} -radix unsigned /rgb2grayscale_tb/dut/s2_din_valid
add wave -noupdate -expand -group {State 3} -radix unsigned /rgb2grayscale_tb/dut/s3_0
TreeUpdate [SetDefaultTree]
WaveRestoreCursors {{Cursor 1} {0 ps} 0}
quietly wave cursor active 0
configure wave -namecolwidth 190
configure wave -valuecolwidth 100
configure wave -justifyvalue left
configure wave -signalnamewidth 0
configure wave -snapdistance 10
configure wave -datasetprefix 0
configure wave -rowmargin 4
configure wave -childrowmargin 2
configure wave -gridoffset 0
configure wave -gridperiod 1
configure wave -griddelta 40
configure wave -timeline 0
configure wave -timelineunits ns
update
WaveRestoreZoom {0 ps} {1170262 ps}
