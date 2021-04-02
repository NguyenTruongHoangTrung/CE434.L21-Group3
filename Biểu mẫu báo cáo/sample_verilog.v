// Module infomation
//----------------------------------------------------//
// Name   	: sample_verilog.v
// Author 	: Cuong.TV 	Email: cuongtv@uit.edu.vn
// Date    	: 22/11/2016
// Revision : 1.0
// Copyright by ViRos Team
//---------------------------------------------------//
// Description (mo ta ve module)
//
//
// Revision
//  +-------------+---------------+-------------------+
//	| Date        | Author	      | Changes           |
//  +-------------+---------------+-------------------+
//  | 22/11/2016  | Cuong.TV      | Initt 1's Release |
//  +-------------+---------------+-------------------+
// 	|
//  +-------------+---------------+-------------------+
//  |
//  +-------------+---------------+-------------------+

module sample_verilog
	#(
	// Khai bao cac parameter cho module
		parameter DATA_WIDTH = 12
	)
	(
	// Khai bao portmap cho modue
		input	clock	,
		input	reset	,
	// Cac tin hieu ngo vao
		input	[DATA_WIDTH-1:0]	data_in			,	
		input						datavalid_in	,
	// ouput 
		output reg [DATA_WIDTH-1:0]	data_out		,
		output reg  				datavalid_out		
	);
	
// Khai bao cac tin hieu noi
// Reg/wire

// Cac lenh gan assignt


// cac instance
// Vi du cach instance

sample_verilog
	#(
	// Khai bao cac parameter cho module
		.DATA_WIDTH (12)
	)
	sample_verilog_inst
	(
	// Khai bao portmap cho modue
		.clock	(clock),
		.reset	(reset),
	// Cac tin hieu ngo vao
		.data_in		(data_in		),	
		.datavalid_in	(datavalid_in	),
	// ouput 
		.data_out		(data_out		),
		.datavalid_out	(datavalid_out	)	
	);

// Cac phat bieu always	



endmodule